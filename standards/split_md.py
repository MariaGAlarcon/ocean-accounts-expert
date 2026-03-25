import os
import re

INPUT_DIR = "."
OUTPUT_ROOT = "output"

os.makedirs(OUTPUT_ROOT, exist_ok=True)

# Match ONLY markdown headings that contain "Chapter"
# Examples:
# ##### Chapter 1
# ###### Chapter 1: Introduction
# ##### Chapter II
CHAPTER_PATTERN = re.compile(
    r"\n(?=#+\s+Chapter\s+[IVX0-9]+)",
    re.IGNORECASE
)

for filename in os.listdir(INPUT_DIR):
    if not filename.lower().endswith(".md"):
        continue
    if filename == "split_md.py":
        continue

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    parts = re.split(CHAPTER_PATTERN, text)

    base_name = os.path.splitext(filename)[0]
    output_dir = os.path.join(OUTPUT_ROOT, base_name)
    os.makedirs(output_dir, exist_ok=True)

    count = 0
    for i, part in enumerate(parts, start=1):
        if not part.strip():
            continue

        title_match = re.search(
            r"#+\s+(Chapter\s+[IVX0-9]+[^\n]*)",
            part,
            re.IGNORECASE
        )
        title = title_match.group(1) if title_match else f"Section_{i}"

        safe_title = re.sub(r"[^\w\-]+", "_", title).strip("_")

        out_name = f"{i:03d}_{safe_title}.md"
        out_path = os.path.join(output_dir, out_name)

        with open(out_path, "w", encoding="utf-8") as out:
            out.write(part.strip())

        count += 1

    print(f"{filename}: split into {count} chapters")

print("Done.")
