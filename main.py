#!/usr/bin/env python3
"""
turtle-matter: Generate vocabulary documentation from Turtle files
"""

import click
from pathlib import Path
from typing import Optional
from rdflib import Graph
from rdflib.namespace import RDF, RDFS, OWL

from vocabulary import VocabularyTerm, VocabularyData, VocabularyExtractor
from formatters import HTMLFormatter, MarkdownFormatter, JSONLDFormatter

@click.command()
@click.argument('turtle_file', type=click.Path(exists=True, path_type=Path))
@click.option('--format', '-f', type=click.Choice(['html', 'markdown', 'jsonld', 'analysis']), 
              default='analysis', help='Output format')
@click.option('--namespace', help='Target namespace to extract terms from')
@click.option('--full-context', is_flag=True, help='Include semantic relationships (subClassOf, domain, range) in JSON-LD context')
@click.option('--docs-dir', '-d', type=click.Path(exists=True, path_type=Path), 
              help='Directory containing companion markdown documentation files')
def main(turtle_file: Path, format: str, namespace: Optional[str], full_context: bool, docs_dir: Optional[Path]):
    """Generate vocabulary documentation from Turtle file."""
    
    # Load the turtle file
    graph = Graph()
    graph.parse(turtle_file, format='turtle')
    
    # Extract vocabulary data
    target_namespaces = [namespace] if namespace else []
    extractor = VocabularyExtractor(target_namespaces)
    vocab_data = extractor.extract_from_graph(graph, full_context)
    
    # Enrich with companion documentation if provided
    if docs_dir:
        vocab_data = extractor.enrich_with_documentation(vocab_data, docs_dir)
    
    # Format and output
    if format == 'html':
        formatter = HTMLFormatter()
        click.echo(formatter.format(vocab_data))
    elif format == 'markdown':
        formatter = MarkdownFormatter()
        click.echo(formatter.format(vocab_data))
    elif format == 'jsonld':
        formatter = JSONLDFormatter()
        click.echo(formatter.format(vocab_data))
    elif format == 'analysis':  # analysis
        # Show status messages for analysis mode only
        click.echo(f"Loading Turtle file: {turtle_file}")
        if vocab_data.namespace:
            click.echo(f"Target namespace: {vocab_data.namespace}")
        else:
            click.echo("No target namespace specified - will show all terms")
        
        click.echo(f"Loaded {len(graph)} triples")
        
        # Show basic info about what's in the graph
        click.echo("\nNamespaces found:")
        for prefix, ns in graph.namespaces():
            click.echo(f"  {prefix}: {ns}")
        
        # Analyze vocabulary content
        click.echo("\nVocabulary Analysis:")
        
        # Find ontologies
        ontologies = list(graph.subjects(RDF.type, OWL.Ontology))
        if ontologies:
            click.echo(f"  Ontologies: {len(ontologies)}")
            for ont in ontologies:
                click.echo(f"    - {ont}")
        
        filter_suffix = " (filtered)" if vocab_data.namespace else ""
        click.echo(f"  Classes{filter_suffix}: {len(vocab_data.classes)}")
        for cls in vocab_data.classes:
            if cls.label:
                click.echo(f"    - {cls.uri} ({cls.label})")
            else:
                click.echo(f"    - {cls.uri}")
        
        click.echo(f"  Properties{filter_suffix}: {len(vocab_data.properties)}")
        for prop in vocab_data.properties:
            if prop.label:
                click.echo(f"    - {prop.uri} ({prop.label})")
            else:
                click.echo(f"    - {prop.uri}")
    else:
        click.echo(f"Unknown format: {format}. Supported formats are: html, markdown, jsonld, analysis.")
        raise click.UsageError(f"Invalid format: {format}")


if __name__ == "__main__":
    main()