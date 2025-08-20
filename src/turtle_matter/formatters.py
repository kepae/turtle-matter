"""
Vocabulary formatters for turtle-matter.

This module contains formatter classes that convert vocabulary data
into various output formats (HTML, Markdown, JSON-LD).
"""

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from . import __version__
from .vocabulary import VocabularyData

# Template configuration
TEMPLATE_DIR = Path(__file__).parent / "templates"


class HTMLFormatter:
    """Formats vocabulary data as HTML."""

    def format(self, vocab_data: VocabularyData) -> str:
        """Generate HTML from vocabulary data."""

        # Set up Jinja2 environment to load templates
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template("vocabulary_template.html")

        return template.render(vocab_data=vocab_data, version=__version__)


class MarkdownFormatter:
    """Formats vocabulary data as Markdown with JSON-LD frontmatter."""

    def format(self, vocab_data: VocabularyData) -> str:
        """Generate Markdown from vocabulary data."""

        # Create frontmatter with JSON-LD context
        frontmatter = "---\n"
        frontmatter += f"title: {vocab_data.title}\n"
        if vocab_data.namespace:
            frontmatter += f"namespace: {vocab_data.namespace}\n"
        frontmatter += f"generator: turtle-matter v{__version__}\n"
        frontmatter += "jsonld_context: |\n"

        # Indent JSON-LD context for YAML
        jsonld_str = json.dumps(vocab_data.jsonld_context, indent=2)
        for line in jsonld_str.split("\n"):
            frontmatter += f"  {line}\n"

        frontmatter += "---\n\n"

        # Generate markdown content
        content = f"# {vocab_data.title}\n\n"
        if vocab_data.namespace:
            content += f"**Namespace:** {vocab_data.namespace}\n\n"
        else:
            content += "**Scope:** All terms\n\n"

        if vocab_data.classes:
            content += f"## Classes ({len(vocab_data.classes)})\n\n"
            for cls in vocab_data.classes:
                content += f"### {cls.label or cls.local_name}\n\n"
                content += f"**URI:** `{cls.uri}`\n\n"
                if cls.comment:
                    content += f"**Description:** {cls.comment}\n\n"
                if cls.subclass_of:
                    content += "**Subclass of:**\n"
                    for parent in cls.subclass_of:
                        content += f"- [{parent}]({parent})\n"
                    content += "\n"

                # Add related properties if available
                if cls.related_properties:
                    content += "**Properties:**\n"
                    for prop in cls.related_properties:
                        range_info = ""
                        if prop.range:
                            range_names = sorted([r.split("/")[-1] for r in prop.range])
                            range_info = f" (→ {', '.join(range_names)})"
                        content += (
                            f"- [{prop.local_name}](#{prop.local_name}){range_info}\n"
                        )
                    content += "\n"

                # Add companion documentation if available
                if cls.documentation and cls.documentation.get("content"):
                    content += "**Documentation:**\n\n"
                    content += cls.documentation["content"] + "\n\n"

                content += "---\n\n"

        if vocab_data.properties:
            content += f"## Properties ({len(vocab_data.properties)})\n\n"
            for prop in vocab_data.properties:
                content += f"### {prop.label or prop.local_name}\n\n"
                content += f"**URI:** `{prop.uri}`\n\n"
                if prop.comment:
                    content += f"**Description:** {prop.comment}\n\n"
                if prop.domain:
                    content += "**Domain:**\n"
                    for domain in prop.domain:
                        content += f"- [{domain}]({domain})\n"
                    content += "\n"
                if prop.range:
                    content += "**Range:**\n"
                    for rng in prop.range:
                        content += f"- [{rng}]({rng})\n"
                    content += "\n"

                # Add companion documentation if available
                if prop.documentation and prop.documentation.get("content"):
                    content += "**Documentation:**\n\n"
                    content += prop.documentation["content"] + "\n\n"

                content += "---\n\n"

        # Add footer
        content += "---\n\n"
        content += f"🐢 *Generated with [turtle-matter](https://github.com/kepae/turtle-matter) v{__version__}*\n"

        return frontmatter + content


class JSONLDFormatter:
    """Formats vocabulary data as pure JSON-LD context."""

    def format(self, vocab_data: VocabularyData) -> str:
        """Generate JSON-LD context from vocabulary data."""
        return json.dumps(vocab_data.jsonld_context, indent=2)
