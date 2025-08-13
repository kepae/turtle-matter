#!/bin/bash

# Generate all vocabulary formats
TURTLE_FILE="test_data/croissant/croissant.ttl"
NAMESPACE="http://mlcommons.org/croissant/"
DOCS_DIR="test_data/croissant/docs"
OUTPUT_DIR="test_data/croissant/outputs"

mkdir -p $OUTPUT_DIR

echo "Generating all formats for croissant vocabulary..."

uv run python main.py $TURTLE_FILE --format html --namespace $NAMESPACE --docs-dir $DOCS_DIR > $OUTPUT_DIR/croissant.html
uv run python main.py $TURTLE_FILE --format markdown --namespace $NAMESPACE --docs-dir $DOCS_DIR > $OUTPUT_DIR/croissant.md
uv run python main.py $TURTLE_FILE --format jsonld --namespace $NAMESPACE > $OUTPUT_DIR/croissant-context.json
uv run python main.py $TURTLE_FILE --namespace $NAMESPACE > $OUTPUT_DIR/croissant-analysis.txt

echo "Done! Generated files in $OUTPUT_DIR/"