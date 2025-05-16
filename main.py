import os
import sys
import argparse
from html_extractor import extract_translatable_html
from txt_extractor import extract_translatable_txt
from pdf_extractor import extract_translatable_pdf
from docx_extractor import extract_translatable_docx

SUPPORTED_EXTENSIONS = {
    ".html": extract_translatable_html,
    ".txt": extract_translatable_txt,
    ".pdf": extract_translatable_pdf,
    ".docx": extract_translatable_docx
}

def detect_file_type(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    return ext if ext in SUPPORTED_EXTENSIONS else None

def main():
    parser = argparse.ArgumentParser(description="Universal text extractor for translation.")
    parser.add_argument("input_file", help="Path to the input file (.html, .txt, .pdf, .docx)")
    parser.add_argument("--lang", required=True, help="Primary language code (e.g., en, es, fr)")

    args = parser.parse_args()
    input_file = args.input_file
    lang = args.lang

    ext = detect_file_type(input_file)

    if not ext:
        print(f"Unsupported file type: {input_file}")
        sys.exit(1)

    extractor_func = SUPPORTED_EXTENSIONS[ext]
    if extractor_func is None:
        print(f"Extraction for '{ext}' files is not yet implemented.")
        sys.exit(1)

    print(f"Detected format: {ext}. Running appropriate extractor...")
    extractor_func(input_file, lang)

if __name__ == "__main__":
    main()
