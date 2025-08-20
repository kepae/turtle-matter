"""
Vocabulary data models and extraction logic for turtle-matter.

This module contains the core data structures used to represent vocabulary terms
and vocabulary data in an intermediate format, as well as the extraction logic
for processing RDF graphs.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import click
import frontmatter
import markdown
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS

# Schema.org namespace
SCHEMA = Namespace("https://schema.org/")


@dataclass
class VocabularyTerm:
    """Represents a vocabulary term (class or property)."""

    uri: str
    local_name: str
    term_type: str  # 'Class' or 'Property'
    label: str | None = None
    comment: str | None = None
    subclass_of: list[str] = field(default_factory=list)
    subproperty_of: list[str] = field(default_factory=list)
    domain: list[str] = field(default_factory=list)
    range: list[str] = field(default_factory=list)
    documentation: dict[str, Any] = field(default_factory=dict)
    related_properties: list["VocabularyTerm"] = field(default_factory=list)


@dataclass
class VocabularyData:
    """Complete vocabulary data in intermediate format."""

    title: str
    namespace: str | None
    base_uri: str
    classes: list[VocabularyTerm]
    properties: list[VocabularyTerm]
    jsonld_context: dict[str, Any]


class VocabularyExtractor:
    """Extracts vocabulary data from RDF graphs."""

    def __init__(self, target_namespaces: list[str] | None = None):
        self.target_namespaces = (
            target_namespaces if target_namespaces is not None else []
        )

    def matches_target_namespaces(self, uri_str: str) -> bool:
        """Check if URI matches any of the target namespaces."""
        if not self.target_namespaces:
            return True
        return any(uri_str.startswith(ns) for ns in self.target_namespaces)

    def get_local_name(self, uri_str: str) -> str:
        """Extract local name from URI."""
        if "#" in uri_str:
            return uri_str.split("#")[-1]
        elif "/" in uri_str:
            return uri_str.split("/")[-1]
        return uri_str

    # Blank node detection: https://en.wikipedia.org/wiki/Blank_node
    def is_blank_node(self, uri_str: str) -> bool:
        """Check if URI is a blank node (auto-generated identifier)."""
        # Blank nodes often start with 'n' followed by hex characters
        # or contain long random-looking strings
        local_name = self.get_local_name(uri_str)
        return len(local_name) > 30 and (
            local_name.startswith("n")
            or all(
                c in "0123456789abcdef"
                for c in local_name.replace("n", "").replace("b", "")
            )
        )

    def load_documentation(self, docs_dir: Path) -> dict[str, dict[str, Any]]:
        """Load companion documentation from markdown files."""
        docs = {}

        if not docs_dir or not docs_dir.exists():
            return docs

        for md_file in docs_dir.glob("**/*.md"):
            try:
                with open(md_file, encoding="utf-8") as f:
                    md = frontmatter.load(f)

                # Extract the term URI from frontmatter
                term_uri = md.metadata.get("term")
                if term_uri:
                    docs[term_uri] = {
                        "content": md.content,
                        "metadata": md.metadata,
                        "file_path": str(md_file),
                    }
            except Exception as e:
                click.echo(f"Warning: Could not parse {md_file}: {e}", err=True)

        return docs

    def enrich_with_documentation(
        self, vocab_data: VocabularyData, docs_dir: Path
    ) -> VocabularyData:
        """Enrich vocabulary data with companion documentation."""
        if not docs_dir:
            return vocab_data

        docs = self.load_documentation(docs_dir)

        # Enrich classes with documentation
        for cls in vocab_data.classes:
            if cls.uri in docs:
                doc_data = docs[cls.uri].copy()
                # Convert markdown content to HTML
                if "content" in doc_data:
                    doc_data["content_html"] = markdown.markdown(
                        doc_data["content"],
                        extensions=["tables", "fenced_code", "codehilite"],
                    )
                cls.documentation = doc_data

        # Enrich properties with documentation
        for prop in vocab_data.properties:
            if prop.uri in docs:
                doc_data = docs[prop.uri].copy()
                # Convert markdown content to HTML
                if "content" in doc_data:
                    doc_data["content_html"] = markdown.markdown(
                        doc_data["content"],
                        extensions=["tables", "fenced_code", "codehilite"],
                    )
                prop.documentation = doc_data

        return vocab_data

    def extract_from_graph(
        self, graph: Graph, full_context: bool = False
    ) -> VocabularyData:
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
                        term_type="Class",
                        label=str(graph.value(cls, RDFS.label))
                        if graph.value(cls, RDFS.label)
                        else None,
                        comment=str(graph.value(cls, RDFS.comment))
                        if graph.value(cls, RDFS.comment)
                        else None,
                        subclass_of=sorted(
                            [
                                str(o)
                                for o in graph.objects(cls, RDFS.subClassOf)
                                if not self.is_blank_node(str(o))
                            ]
                        ),
                    )
                    classes.append(term)

        # Extract properties
        properties = []
        for prop_type in [RDF.Property, OWL.ObjectProperty, OWL.DatatypeProperty]:
            for prop in graph.subjects(RDF.type, prop_type):
                if self.matches_target_namespaces(str(prop)):
                    # Extract domain from both rdfs:domain and schema:domainIncludes
                    domain_list = []
                    domain_list.extend(
                        [
                            str(o)
                            for o in graph.objects(prop, RDFS.domain)
                            if not self.is_blank_node(str(o))
                        ]
                    )
                    domain_list.extend(
                        [
                            str(o)
                            for o in graph.objects(prop, SCHEMA.domainIncludes)
                            if not self.is_blank_node(str(o))
                        ]
                    )

                    # Extract range from both rdfs:range and schema:rangeIncludes
                    range_list = []
                    range_list.extend(
                        [
                            str(o)
                            for o in graph.objects(prop, RDFS.range)
                            if not self.is_blank_node(str(o))
                        ]
                    )
                    range_list.extend(
                        [
                            str(o)
                            for o in graph.objects(prop, SCHEMA.rangeIncludes)
                            if not self.is_blank_node(str(o))
                        ]
                    )

                    term = VocabularyTerm(
                        uri=str(prop),
                        local_name=self.get_local_name(str(prop)),
                        term_type="Property",
                        label=str(graph.value(prop, RDFS.label))
                        if graph.value(prop, RDFS.label)
                        else None,
                        comment=str(graph.value(prop, RDFS.comment))
                        if graph.value(prop, RDFS.comment)
                        else None,
                        domain=sorted(set(domain_list)),
                        range=sorted(set(range_list)),
                    )
                    properties.append(term)

        # Remove duplicates and sort
        classes = sorted(
            {cls.uri: cls for cls in classes}.values(), key=lambda x: x.local_name
        )
        properties = sorted(
            {prop.uri: prop for prop in properties}.values(), key=lambda x: x.local_name
        )

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
        context = {
            "@vocab": self.target_namespaces[0] if self.target_namespaces else ""
        }

        # Track which prefixes are actually used
        used_uris = set()
        for cls in classes:
            used_uris.update(cls.subclass_of)
        for prop in properties:
            used_uris.update(prop.domain)
            used_uris.update(prop.range)

        # Map common prefixes
        prefix_map = {
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
            "http://www.w3.org/2000/01/rdf-schema#": "rdfs",
            "http://www.w3.org/2002/07/owl#": "owl",
            "https://schema.org/": "schema",
        }

        # Only add prefixes that are actually used
        for uri in used_uris:
            for namespace, prefix in prefix_map.items():
                if uri.startswith(namespace) and prefix not in context:
                    context[prefix] = namespace

        jsonld_context: dict[str, Any] = {"@context": context}

        # Add term definitions to context
        for cls in classes:
            term_def = {"@id": cls.uri, "@type": "@id"}

            # Add semantic relationships if full context requested
            if full_context:
                if cls.subclass_of:
                    if len(cls.subclass_of) == 1:
                        term_def["rdfs:subClassOf"] = {"@id": cls.subclass_of[0]}
                    else:
                        term_def["rdfs:subClassOf"] = [
                            {"@id": parent} for parent in cls.subclass_of
                        ]

            jsonld_context["@context"][cls.local_name] = term_def

        for prop in properties:
            term_def = {"@id": prop.uri}

            # Add semantic relationships if full context requested
            if full_context:
                if prop.domain:
                    if len(prop.domain) == 1:
                        term_def["rdfs:domain"] = {"@id": prop.domain[0]}
                    else:
                        term_def["rdfs:domain"] = [
                            {"@id": domain} for domain in prop.domain
                        ]

                if prop.range:
                    if len(prop.range) == 1:
                        term_def["rdfs:range"] = {"@id": prop.range[0]}
                    else:
                        term_def["rdfs:range"] = [
                            {"@id": range_val} for range_val in prop.range
                        ]

            jsonld_context["@context"][prop.local_name] = term_def

        return VocabularyData(
            title="Vocabulary",
            namespace=self.target_namespaces[0] if self.target_namespaces else None,
            base_uri=self.target_namespaces[0] if self.target_namespaces else "",
            classes=classes,
            properties=properties,
            jsonld_context=jsonld_context,
        )
