import os
import shutil

CATEGORY_MAP = {
    "documents": [".txt", ".pdf", ".docx", ".xlsx"],
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "archives": [".zip", ".tar", ".gz", ".rar"]
}

SOURCE_DIR = "./sample_files"

# Task 1: Organize files by extension

def organize_files(source_dir: str):
    if not os.path.isdir(source_dir):
        raise FileNotFoundError(f"Directory not found: {source_dir}")

    for filename in os.listdir(source_dir):
        full_path = os.path.join(source_dir, filename)
        if os.path.isfile(full_path):
            _, ext = os.path.splitext(filename)
            moved = False
            for category, extensions in CATEGORY_MAP.items():
                if ext.lower() in extensions:
                    category_dir = os.path.join(source_dir, category)
                    os.makedirs(category_dir, exist_ok=True)
                    shutil.move(full_path, os.path.join(category_dir, filename))
                    moved = True
                    break
            if not moved:
                other_dir = os.path.join(source_dir, "other")
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(full_path, os.path.join(other_dir, filename))

# Task 2: Search text files for a keyword

def search_text_files(source_dir: str, keyword: str):
    matches = []
    for root, _, files in os.walk(source_dir):
        for filename in files:
            if filename.lower().endswith(".txt"):
                filepath = os.path.join(root, filename)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    if keyword.lower() in content.lower():
                        matches.append(filepath)
    return matches

if __name__ == "__main__":
    print("This file contains starter functions for file organization and text search.")
    print("Update the script to accept user input and run the tasks from a single program.")
