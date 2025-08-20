#!/usr/bin/env python3
"""
CLI interface for turtle-matter.
"""

from pathlib import Path

import click
from rdflib import Graph
from rdflib.namespace import OWL, RDF

from .formatters import HTMLFormatter, JSONLDFormatter, MarkdownFormatter
from .vocabulary import VocabularyExtractor


@click.command()
@click.argument("rdf_file", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--emit",
    "-e",
    type=click.Choice(["html", "markdown", "jsonld", "analysis"]),
    default="analysis",
    help="Output format",
)
@click.option("--rdf-format", help="RDF input format (auto-detected if not specified)")
@click.option("--namespace", help="Target namespace to extract terms from")
@click.option(
    "--full-context",
    is_flag=True,
    help="Include semantic relationships (subClassOf, domain, range) in JSON-LD context",
)
@click.option(
    "--docs-dir",
    "-d",
    type=click.Path(exists=True, path_type=Path),
    help="Directory containing companion markdown documentation files",
)
@click.option("--title", help="Title for the vocabulary (defaults to filename)")
def main(
    rdf_file: Path,
    emit: str,
    rdf_format: str | None,
    namespace: str | None,
    full_context: bool,
    docs_dir: Path | None,
    title: str | None,
):
    """Generate human- and machine-readable vocabulary documentation (HTML, Markdown) from RDF file."""

    # Auto-detect RDF format if not specified
    if rdf_format is None:
        suffix = rdf_file.suffix.lower()
        format_map = {
            ".ttl": "turtle",
            ".turtle": "turtle",
            ".rdf": "xml",
            ".xml": "xml",
            ".nt": "nt",
            ".n3": "n3",
            ".jsonld": "json-ld",
            ".trig": "trig",
            ".nq": "nquads",
        }
        rdf_format = format_map.get(suffix)
        if rdf_format is None:
            click.echo(
                f"Cannot auto-detect RDF format for file extension '{suffix}'", err=True
            )
            click.echo(
                "Please specify --rdf-format with one of: turtle, xml, nt, n3, json-ld, trig, nquads",
                err=True,
            )
            raise click.ClickException(f"Unknown RDF file extension: {suffix}")
        click.echo(f"Auto-detected RDF format: {rdf_format}", err=True)

    # Load the RDF file
    graph = Graph()
    try:
        graph.parse(rdf_file, format=rdf_format)
    except Exception as e:
        click.echo(f"Error parsing RDF file: {e}", err=True)
        click.echo(
            f"Try specifying a different --rdf-format (current: {rdf_format})", err=True
        )
        raise click.ClickException(f"Failed to parse {rdf_file}") from e

    # Extract vocabulary data
    target_namespaces = [namespace] if namespace else []
    extractor = VocabularyExtractor(target_namespaces)
    vocab_data = extractor.extract_from_graph(graph, full_context)

    # Set title (use provided title or infer from filename)
    if title:
        vocab_data.title = title
    else:
        # Simple filename-based inference
        stem = rdf_file.stem  # "filename" from "filename.ttl"
        vocab_data.title = stem.replace("-", " ").replace("_", " ").title()

    # Enrich with companion documentation if provided
    if docs_dir:
        vocab_data = extractor.enrich_with_documentation(vocab_data, docs_dir)

    # Format and output
    if emit == "html":
        formatter = HTMLFormatter()
        click.echo(formatter.format(vocab_data))
    elif emit == "markdown":
        formatter = MarkdownFormatter()
        click.echo(formatter.format(vocab_data))
    elif emit == "jsonld":
        formatter = JSONLDFormatter()
        click.echo(formatter.format(vocab_data))
    elif emit == "analysis":  # analysis
        # Show status messages for analysis mode only
        click.echo(f"Loading RDF file: {rdf_file} (format: {rdf_format})")
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
        click.echo(
            f"Unknown output format: {emit}. Supported formats are: html, markdown, jsonld, analysis."
        )
        raise click.UsageError(f"Invalid output format: {emit}")


if __name__ == "__main__":
    main()
