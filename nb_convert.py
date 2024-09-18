import os
import subprocess
import shutil
import sys
from pathlib import Path


def parse_name_and_date(base: str):
    name = base.split("-")[-1]
    date = "-".join(base.split("-")[:3])
    return name, date


def move_image_files(img_dir: Path, img_dir_output: Path):
    if os.path.exists(img_dir):
        shutil.rmtree(img_dir)
    if os.path.exists(img_dir_output):
        shutil.move(img_dir_output, img_dir)


def process_md_file(md_file: Path, name: str):
    with open(md_file, "r") as fin:
        data = fin.read().splitlines(True)

    for i, l in enumerate(data):
        if l.startswith("![png]"):
            loc = l.split("[png]")[1][1:-2].split("/")[1]
            path = f"assets/notebooks/{name}/{loc}"
            data[i] = f'{{% include figure.html path="{path}" width="65%" %}}'
        else:
            data[i] = l.replace("$", "$$")

    with open(md_file, "w") as fout:
        fout.writelines(data)


def main():
    notebook = sys.argv[1]
    base = os.path.basename(notebook).lower().split(".")[0]
    name, date = parse_name_and_date(base)
    print(f"Converting {notebook} -> {name} (created on {date})")

    post_dir = Path("_posts/")
    subprocess.run(
        f"jupyter nbconvert ./{notebook} --to markdown --output-dir {post_dir}",
        check=True,
        shell=True,
    )

    img_dir = Path(f"assets/notebooks/{name}")
    img_dir_output = Path(post_dir / f"{base}_files")
    move_image_files(img_dir, img_dir_output)
    print(f"Moved image files from {img_dir_output} to {img_dir}")

    md_file = post_dir / f"{base}.md"
    process_md_file(md_file, name)


if __name__ == "__main__":
    main()
