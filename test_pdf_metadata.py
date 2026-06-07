from app.services.preprocessing.pdf_loader import extract_text_from_pdf
from app.services.preprocessing.pdf_metadata_parser import extract_pdf_metadata

PDF_PATH = "storage/pdfs/sample.pdf"  # use any downloaded RBI PDF

pages = extract_text_from_pdf(PDF_PATH)
metadata = extract_pdf_metadata(pages)

print("\n===== PDF METADATA OUTPUT =====")
for k, v in metadata.items():
    print(f"{k}: {v}")
