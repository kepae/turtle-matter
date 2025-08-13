#!/bin/bash

# Generate examples for GitHub Pages
RDF_FILE="test_data/croissant/croissant.ttl"
NAMESPACE="http://mlcommons.org/croissant/"
DOCS_DIR="test_data/croissant/docs"
EXAMPLES_DIR="docs/examples"

mkdir -p $EXAMPLES_DIR

echo "Generating examples for GitHub Pages..."

uv run python main.py $RDF_FILE --emit html --namespace $NAMESPACE --docs-dir $DOCS_DIR --title "Croissant" > $EXAMPLES_DIR/croissant.html
uv run python main.py $RDF_FILE --emit markdown --namespace $NAMESPACE --docs-dir $DOCS_DIR --title "Croissant" > $EXAMPLES_DIR/croissant.md
uv run python main.py $RDF_FILE --emit jsonld --namespace $NAMESPACE > $EXAMPLES_DIR/croissant-context.json
uv run python main.py $RDF_FILE --namespace $NAMESPACE > $EXAMPLES_DIR/croissant-analysis.txt

echo "Done! Examples generated in $EXAMPLES_DIR/ for GitHub Pages"
echo "After pushing to GitHub, enable Pages in repo Settings → Pages → Source: main branch, /docs folder"