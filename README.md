# Turtle Matter 🐢

Generate human- and machine-readable HTML pages from RDF files and related markdown documentation files.

### Usage
```shell
% uv run main.py --help
Usage: main.py [OPTIONS] RDF_FILE

  Generate vocabulary documentation from RDF file.

Options:
  -e, --emit [html|markdown|jsonld|analysis]
                                  Output format
  --rdf-format TEXT               RDF input format (auto-detected if not
                                  specified)
  --namespace TEXT                Target namespace to extract terms from
  --full-context                  Include semantic relationships (subClassOf,
                                  domain, range) in JSON-LD context
  -d, --docs-dir PATH             Directory containing companion markdown
                                  documentation files
  --title TEXT                    Title for the vocabulary (defaults to
                                  filename)
  --help                          Show this message and exit.
  ```