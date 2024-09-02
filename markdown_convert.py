from typing import Optional
from pathlib import Path
from datetime import datetime as dt
import argparse

import markdown


def convert_markdown_to_html(input_file: str, output_file: Optional[str] = None) -> None:
    """Convert a Markdown file to a complete HTML document and save it to an output file.

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str, optional): Path to the output HTML file. If not provided,
                                     it will use the same directory and name as the input file.
    """
    # Determine the output file path
    if output_file is None:
        input_path = Path(input_file)
        output_file = input_path.with_suffix(".html")

    # Read the Markdown file
    with open(input_file, "r", encoding="utf-8") as md_file:
        markdown_text = md_file.read()

    # Current date for the update
    current_date = dt.now().strftime("%Y-%m-%d")

    # Update the "Last updated" line
    lines = markdown_text.splitlines()
    updated_lines = []
    for line in lines:
        if "Last updated" in line:
            updated_lines.append(f"_Last updated: {current_date}_")
        else:
            updated_lines.append(line)
    updated_markdown_text = "\n".join(updated_lines)

    # Convert Markdown to HTML
    body_html = markdown.markdown(updated_markdown_text, extensions=["markdown.extensions.tables"])

    # Create a complete HTML document
    complete_html = f"""<!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body>
            {body_html}
        </body>
    </html>"""

    # Write the complete HTML output to a file
    with open(output_file, "w", encoding="utf-8") as html_file:
        html_file.write(complete_html)

    print(f"Converted '{input_file}' to '{output_file}' successfully.")


if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Convert a Markdown file to a complete HTML document")
    parser.add_argument("input_file", type=str, help="Path to the input Markdown file")
    parser.add_argument("--output_file", type=str, default=None, help="Optional path to the output HTML file")

    # Parse arguments
    args = parser.parse_args()

    # Call the conversion function
    convert_markdown_to_html(args.input_file, args.output_file)
