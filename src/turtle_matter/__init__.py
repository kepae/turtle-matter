"""
turtle-matter: Generate vocabulary documentation from RDF files.

A tool for generating human- and machine-readable vocabulary documentation
from RDF/Turtle files, including HTML, Markdown, and JSON-LD outputs.
"""

__version__ = "0.1.0"
__author__ = "Kevin Paeth"

# Export main API classes for programmatic use
from .formatters import HTMLFormatter, JSONLDFormatter, MarkdownFormatter
from .vocabulary import VocabularyData, VocabularyExtractor, VocabularyTerm

__all__ = [
    "VocabularyTerm",
    "VocabularyData",
    "VocabularyExtractor",
    "HTMLFormatter",
    "MarkdownFormatter",
    "JSONLDFormatter",
]
