"""
turtle-matter: Generate vocabulary documentation from RDF files.

A tool for generating human- and machine-readable vocabulary documentation 
from RDF/Turtle files, including HTML, Markdown, and JSON-LD outputs.
"""

__version__ = "0.1.0"
__author__ = "Kevin Paeth"

# Export main API classes for programmatic use
from .vocabulary import VocabularyTerm, VocabularyData, VocabularyExtractor
from .formatters import HTMLFormatter, MarkdownFormatter, JSONLDFormatter

__all__ = [
    "VocabularyTerm",
    "VocabularyData", 
    "VocabularyExtractor",
    "HTMLFormatter",
    "MarkdownFormatter",
    "JSONLDFormatter"
]