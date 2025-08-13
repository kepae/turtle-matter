#!/bin/bash

# Generate all vocabulary formats
RDF_FILE="test_data/croissant/croissant.ttl"
NAMESPACE="http://mlcommons.org/croissant/"
DOCS_DIR="test_data/croissant/docs"
OUTPUT_DIR="test_data/croissant/outputs"

mkdir -p $OUTPUT_DIR

echo "Generating all formats for croissant vocabulary..."

uv run python main.py $RDF_FILE --emit html --namespace $NAMESPACE --docs-dir $DOCS_DIR > $OUTPUT_DIR/croissant.html
uv run python main.py $RDF_FILE --emit markdown --namespace $NAMESPACE --docs-dir $DOCS_DIR > $OUTPUT_DIR/croissant.md
uv run python main.py $RDF_FILE --emit jsonld --namespace $NAMESPACE > $OUTPUT_DIR/croissant-context.json
uv run python main.py $RDF_FILE --namespace $NAMESPACE > $OUTPUT_DIR/croissant-analysis.txt

echo "Done! Generated files in $OUTPUT_DIR/"