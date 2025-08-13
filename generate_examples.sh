#!/bin/bash

# Generate examples for GitHub Pages
RDF_FILE="docs/examples/croissant/inputs/croissant.ttl"
NAMESPACE="http://mlcommons.org/croissant/"
DOCS_DIR="docs/examples/croissant/inputs/docs"
EXAMPLES_OUTPUTS_DIR="docs/examples"

mkdir -p $EXAMPLES_OUTPUTS_DIR

echo "Generating examples for GitHub Pages..."

uv run python main.py $RDF_FILE --emit html --namespace $NAMESPACE --docs-dir $DOCS_DIR --title "Croissant" > $EXAMPLES_OUTPUTS_DIR/croissant.html
uv run python main.py $RDF_FILE --emit markdown --namespace $NAMESPACE --docs-dir $DOCS_DIR --title "Croissant" > $EXAMPLES_OUTPUTS_DIR/croissant.md
uv run python main.py $RDF_FILE --emit jsonld --namespace $NAMESPACE > $EXAMPLES_OUTPUTS_DIR/croissant-context.json
uv run python main.py $RDF_FILE --namespace $NAMESPACE > $EXAMPLES_OUTPUTS_DIR/croissant-analysis.txt

echo "Done! Examples generated in $EXAMPLES_OUTPUTS_DIR"