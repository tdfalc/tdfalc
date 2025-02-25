import os
import subprocess
import shutil
import sys
from pathlib import Path
import re
from typing import Optional


def move_files(src: Path, dest: Path):

    if os.path.exists(src):
        try:
            shutil.rmtree(src)
        except NotADirectoryError:
            pass
    if os.path.exists(src):
        shutil.move(src, dest)


def process_md_file(notebook: Path, md_file: Path, name: str) -> Optional[str]:
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

    # 2b. Replace GIF image syntax
    # This regex matches ![gif](...)
    gif_pattern = re.compile(r"!\[gif\]\((.*?)\)")

    def replace_gif(match: re.Match) -> str:
        # Extract the image path
        image_path = match.group(1)
        # Extract the filename from the path
        loc = image_path.split("/")[-1]
        # Construct the new path
        new_path = f"assets/posts/{name}/{loc}"
        # Save the gif in the file directory
        shutil.copy(notebook.parent / loc, f"assets/posts/{name}/{loc}")
        # Return the replacement string
        return f'{{% include figure.html path="{new_path}" width="100%" %}}'

    content = gif_pattern.sub(replace_gif, content)

    # 3. Replace math expressions
    # Pattern to match both inline ($x$) and display ($$x$$) math
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
    notebook = Path(sys.argv[1])
    name = os.path.basename(notebook).lower().split(".")[0]

    print(f"Converting {notebook} -> {name}")

    post_dir = Path("./_posts/")
    subprocess.run(
        f"jupyter nbconvert {notebook} --to markdown --output-dir {post_dir}",
        check=True,
        shell=True,
    )

    img_dir = Path(f"./assets/posts/{name}")
    os.makedirs(img_dir, exist_ok=True)
    img_dir_output = Path(post_dir / f"{name}_files")
    move_files(img_dir_output, img_dir)
    print(f"Moved image files from {img_dir_output} to {img_dir}")

    extracted_date = process_md_file(notebook, post_dir / f"{name}.md", name)
    md_file = post_dir / f"{extracted_date}-{name}.md"
    move_files(post_dir / f"{name}.md", md_file)


if __name__ == "__main__":
    main()
