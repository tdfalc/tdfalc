from pathlib import Path
from datetime import datetime as dt
import argparse
import markdown
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name


def convert_markdown_to_html(input_file: str, output_file: str = None) -> None:
    input_path = Path(input_file)
    output_file = output_file or input_path.with_suffix(".html")

    with open(input_file, "r", encoding="utf-8") as md_file:
        markdown_text = md_file.read()

    current_date = dt.now().strftime("%Y-%m-%d")
    updated_markdown = markdown_text.replace("Last updated:", f"Last updated: {current_date}")

    extensions = ["tables", "fenced_code", "codehilite"]
    body_html = markdown.markdown(updated_markdown, extensions=extensions)

    # Use a style that better highlights function calls
    pygments_style = get_style_by_name("monokai")
    pygments_css = HtmlFormatter(style=pygments_style).get_style_defs(".codehilite")

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
      
    </head>
    <body>{body_html}</body>
    </html>
    """

    with open(output_file, "w", encoding="utf-8") as html_file:
        html_file.write(html_template)

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
