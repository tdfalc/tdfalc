import os
import subprocess
import shutil
import sys
from pathlib import Path
import re
from typing import Optional


def move_files(input: Path, output: Path):

    if os.path.exists(input):
        try:
            shutil.rmtree(input)
        except NotADirectoryError:
            pass
    if os.path.exists(output):
        shutil.move(output, input)


def process_md_file(md_file: Path, name: str) -> Optional[str]:
    """
    Processes a Markdown file by replacing SVG image syntax and math expressions.
    Additionally, extracts the date from lines starting with 'date: YYYY-MM-DD'.

    Args:
        md_file (Path): The path to the Markdown file to be processed.
        name (str): The name used to construct asset paths.

    Returns:
        Optional[str]: The extracted date string if found, otherwise None.
    """
    # Read the entire file content
    with md_file.open("r", encoding="utf-8") as fin:
        content = fin.read()

    extracted_date: Optional[str] = None  # Initialize the extracted date

    # 1. Extract the date
    date_pattern = re.compile(r"^date:\s*(\d{4}-\d{2}-\d{2})\s*$", re.IGNORECASE | re.MULTILINE)
    date_match = date_pattern.search(content)
    if date_match:
        extracted_date = date_match.group(1)
        print(f"Extracted Date: {extracted_date}")
    else:
        print("No date found in the file.")

    # 2. Replace SVG image syntax
    # This regex matches ![svg](...)
    svg_pattern = re.compile(r"!\[svg\]\((.*?)\)")

    def replace_svg(match: re.Match) -> str:
        # Extract the image path
        image_path = match.group(1)
        # Extract the filename from the path
        loc = image_path.split("/")[-1]
        # Construct the new path
        new_path = f"assets/posts/{name}/{loc}"
        # Return the replacement string
        return f'{{% include figure.html path="{new_path}" width="100%" %}}'

    content = svg_pattern.sub(replace_svg, content)

    # 3. Replace math expressions
    # Pattern to match both inline ($x$) and display ($$x$$) math
    # Using non-greedy matching and DOTALL to handle multi-line display math
    math_pattern = re.compile(r"(?<!\\)(\$\$?)(.+?)(?<!\\)\1", re.DOTALL)

    def replace_math(match: re.Match) -> str:
        delimiter = match.group(1)
        content_math = match.group(2).strip()
        if delimiter == "$":
            # Inline math replacement
            return f"{{% katexmm %}} ${content_math}$ {{% endkatexmm %}}"
        else:
            # Display math replacement with tags on separate lines
            return f"{{% katexmm %}}\n$$\n{content_math}\n$$\n{{% endkatexmm %}}"

    content = math_pattern.sub(replace_math, content)

    # 4. Write the modified content back to the file
    with md_file.open("w", encoding="utf-8") as fout:
        fout.write(content)

    print(f"Processed '{md_file}' successfully.")

    return extracted_date


def main():
    notebook = sys.argv[1]
    name = os.path.basename(notebook).lower().split(".")[0]

    print(f"Converting {notebook} -> {name}")

    post_dir = Path("./_posts/")
    subprocess.run(
        f"jupyter nbconvert {notebook} --to markdown --output-dir {post_dir}",
        check=True,
        shell=True,
    )

    img_dir = Path(f"./assets/posts/{name}")
    img_dir_output = Path(post_dir / f"{name}_files")
    move_files(img_dir, img_dir_output)
    print(f"Moved image files from {img_dir_output} to {img_dir}")

    extracted_date = process_md_file(post_dir / f"{name}.md", name)
    md_file = post_dir / f"{extracted_date}-{name}.md"
    move_files(md_file, post_dir / f"{name}.md")


if __name__ == "__main__":
    main()
