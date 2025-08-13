"""
Vocabulary data models and extraction logic for turtle-matter.

This module contains the core data structures used to represent vocabulary terms
and vocabulary data in an intermediate format, as well as the extraction logic
for processing RDF graphs.
"""

from dataclasses import dataclass
from typing import Dict, List, Any, Optional
from pathlib import Path

from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, OWL
from rdflib import URIRef
import frontmatter
import markdown
import click

# Schema.org namespace
SCHEMA = Namespace("https://schema.org/")


@dataclass
class VocabularyTerm:
    """Represents a vocabulary term (class or property)."""
    uri: str
    local_name: str
    term_type: str  # 'Class' or 'Property'
    label: Optional[str] = None
    comment: Optional[str] = None
    subclass_of: List[str] = None
    subproperty_of: List[str] = None
    domain: List[str] = None
    range: List[str] = None
    documentation: Dict[str, Any] = None
    related_properties: List['VocabularyTerm'] = None  # Properties that apply to this class
    
    def __post_init__(self):
        # Initialize mutable defaults
        if self.subclass_of is None:
            self.subclass_of = []
        if self.subproperty_of is None:
            self.subproperty_of = []
        if self.domain is None:
            self.domain = []
        if self.range is None:
            self.range = []
        if self.documentation is None:
            self.documentation = {}
        if self.related_properties is None:
            self.related_properties = []


@dataclass 
class VocabularyData:
    """Complete vocabulary data in intermediate format."""
    title: str
    namespace: Optional[str]
    base_uri: str
    classes: List[VocabularyTerm]
    properties: List[VocabularyTerm]
    jsonld_context: Dict[str, Any]


class VocabularyExtractor:
    """Extracts vocabulary data from RDF graphs."""
    
    def __init__(self, target_namespaces: List[str] = None):
        self.target_namespaces = target_namespaces or []
    
    def matches_target_namespaces(self, uri_str: str) -> bool:
        """Check if URI matches any of the target namespaces."""
        if not self.target_namespaces:
            return True
        return any(uri_str.startswith(ns) for ns in self.target_namespaces)
    
    def get_local_name(self, uri_str: str) -> str:
        """Extract local name from URI."""
        if '#' in uri_str:
            return uri_str.split('#')[-1]
        elif '/' in uri_str:
            return uri_str.split('/')[-1]
        return uri_str
    
    def load_documentation(self, docs_dir: Path) -> Dict[str, Dict[str, Any]]:
        """Load companion documentation from markdown files."""
        docs = {}
        
        if not docs_dir or not docs_dir.exists():
            return docs
        
        for md_file in docs_dir.glob('**/*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    md = frontmatter.load(f)
                    
                # Extract the term URI from frontmatter
                term_uri = md.metadata.get('term')
                if term_uri:
                    docs[term_uri] = {
                        'content': md.content,
                        'metadata': md.metadata,
                        'file_path': str(md_file)
                    }
            except Exception as e:
                click.echo(f"Warning: Could not parse {md_file}: {e}", err=True)
        
        return docs
    
    def enrich_with_documentation(self, vocab_data: VocabularyData, docs_dir: Path) -> VocabularyData:
        """Enrich vocabulary data with companion documentation."""
        if not docs_dir:
            return vocab_data
            
        docs = self.load_documentation(docs_dir)
        
        # Enrich classes with documentation
        for cls in vocab_data.classes:
            if cls.uri in docs:
                doc_data = docs[cls.uri].copy()
                # Convert markdown content to HTML
                if 'content' in doc_data:
                    doc_data['content_html'] = markdown.markdown(
                        doc_data['content'], 
                        extensions=['tables', 'fenced_code', 'codehilite']
                    )
                cls.documentation = doc_data
        
        # Enrich properties with documentation  
        for prop in vocab_data.properties:
            if prop.uri in docs:
                doc_data = docs[prop.uri].copy()
                # Convert markdown content to HTML
                if 'content' in doc_data:
                    doc_data['content_html'] = markdown.markdown(
                        doc_data['content'], 
                        extensions=['tables', 'fenced_code', 'codehilite']
                    )
                prop.documentation = doc_data
        
        return vocab_data
    
    def extract_from_graph(self, graph: Graph, full_context: bool = False) -> VocabularyData:
        """Extract vocabulary data from RDF graph."""
        
        # Extract classes
        classes = []
        rdf_class = URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#Class")
        
        for class_type in [rdf_class, OWL.Class, RDFS.Class]:
            for cls in graph.subjects(RDF.type, class_type):
                if self.matches_target_namespaces(str(cls)):
                    term = VocabularyTerm(
                        uri=str(cls),
                        local_name=self.get_local_name(str(cls)),
                        term_type='Class',
                        label=str(graph.value(cls, RDFS.label)) if graph.value(cls, RDFS.label) else None,
                        comment=str(graph.value(cls, RDFS.comment)) if graph.value(cls, RDFS.comment) else None,
                        subclass_of=[str(o) for o in graph.objects(cls, RDFS.subClassOf)]
                    )
                    classes.append(term)
        
        # Extract properties
        properties = []
        for prop_type in [RDF.Property, OWL.ObjectProperty, OWL.DatatypeProperty]:
            for prop in graph.subjects(RDF.type, prop_type):
                if self.matches_target_namespaces(str(prop)):
                    # Extract domain from both rdfs:domain and schema:domainIncludes
                    domain_list = []
                    domain_list.extend([str(o) for o in graph.objects(prop, RDFS.domain)])
                    domain_list.extend([str(o) for o in graph.objects(prop, SCHEMA.domainIncludes)])
                    
                    # Extract range from both rdfs:range and schema:rangeIncludes  
                    range_list = []
                    range_list.extend([str(o) for o in graph.objects(prop, RDFS.range)])
                    range_list.extend([str(o) for o in graph.objects(prop, SCHEMA.rangeIncludes)])
                    
                    term = VocabularyTerm(
                        uri=str(prop),
                        local_name=self.get_local_name(str(prop)),
                        term_type='Property',
                        label=str(graph.value(prop, RDFS.label)) if graph.value(prop, RDFS.label) else None,
                        comment=str(graph.value(prop, RDFS.comment)) if graph.value(prop, RDFS.comment) else None,
                        domain=list(set(domain_list)),  # Remove duplicates
                        range=list(set(range_list))     # Remove duplicates
                    )
                    properties.append(term)
        
        # Remove duplicates and sort
        classes = sorted(list({cls.uri: cls for cls in classes}.values()), key=lambda x: x.local_name)
        properties = sorted(list({prop.uri: prop for prop in properties}.values()), key=lambda x: x.local_name)
        
        # Add reverse lookup: find properties that apply to each class
        for cls in classes:
            cls.related_properties = []
            for prop in properties:
                # Check if this class is in the property's domain
                if cls.uri in prop.domain:
                    cls.related_properties.append(prop)
            # Sort properties by name
            cls.related_properties.sort(key=lambda x: x.local_name)
        
        # Generate JSON-LD context
        jsonld_context = {
            "@context": {
                "@vocab": self.target_namespaces[0] if self.target_namespaces else "",
                "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                "owl": "http://www.w3.org/2002/07/owl#",
                "schema": "https://schema.org/"
            }
        }
        
        # Add term definitions to context
        for cls in classes:
            term_def = {
                "@id": cls.uri,
                "@type": "@id"
            }
            
            # Add semantic relationships if full context requested
            if full_context:
                if cls.subclass_of:
                    if len(cls.subclass_of) == 1:
                        term_def["rdfs:subClassOf"] = {"@id": cls.subclass_of[0]}
                    else:
                        term_def["rdfs:subClassOf"] = [{"@id": parent} for parent in cls.subclass_of]
            
            jsonld_context["@context"][cls.local_name] = term_def
        
        for prop in properties:
            term_def = {
                "@id": prop.uri
            }
            
            # Add semantic relationships if full context requested
            if full_context:
                if prop.domain:
                    if len(prop.domain) == 1:
                        term_def["rdfs:domain"] = {"@id": prop.domain[0]}
                    else:
                        term_def["rdfs:domain"] = [{"@id": domain} for domain in prop.domain]
                
                if prop.range:
                    if len(prop.range) == 1:
                        term_def["rdfs:range"] = {"@id": prop.range[0]}
                    else:
                        term_def["rdfs:range"] = [{"@id": range_val} for range_val in prop.range]
            
            jsonld_context["@context"][prop.local_name] = term_def
        
        return VocabularyData(
            title="Vocabulary",
            namespace=self.target_namespaces[0] if self.target_namespaces else None,
            base_uri=self.target_namespaces[0] if self.target_namespaces else "",
            classes=classes,
            properties=properties,
            jsonld_context=jsonld_context
        )