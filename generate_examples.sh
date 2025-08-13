#!/bin/bash

echo "Generating examples..."

# Croissant example
echo "Processing croissant..."
RDF_FILE="docs/examples/croissant/inputs/croissant.ttl"
NAMESPACE="http://mlcommons.org/croissant/"
DOCS_DIR="docs/examples/croissant/inputs/docs"
OUTPUTS_DIR="docs/examples/croissant/outputs"

mkdir -p $OUTPUTS_DIR
uv run python main.py $RDF_FILE --emit html --namespace $NAMESPACE --docs-dir $DOCS_DIR --title "Croissant" > $OUTPUTS_DIR/croissant.html
uv run python main.py $RDF_FILE --emit markdown --namespace $NAMESPACE --docs-dir $DOCS_DIR --title "Croissant" > $OUTPUTS_DIR/croissant.md
uv run python main.py $RDF_FILE --emit jsonld --namespace $NAMESPACE > $OUTPUTS_DIR/croissant-context.json

# PROV example  
echo "Processing prov..."
RDF_FILE="docs/examples/prov/inputs/prov.ttl"
NAMESPACE="http://www.w3.org/ns/prov#"
OUTPUTS_DIR="docs/examples/prov/outputs"

mkdir -p $OUTPUTS_DIR
uv run python main.py $RDF_FILE --emit html --namespace $NAMESPACE --title "PROV Ontology" > $OUTPUTS_DIR/prov.html
uv run python main.py $RDF_FILE --emit markdown --namespace $NAMESPACE --title "PROV Ontology" > $OUTPUTS_DIR/prov.md
uv run python main.py $RDF_FILE --emit jsonld --namespace $NAMESPACE > $OUTPUTS_DIR/prov-context.json

echo "Done! All examples generated."