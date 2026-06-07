from fastapi import APIRouter, HTTPException
from pathlib import Path
from fastapi import APIRouter, Depends
from app.core.security import verify_admin_key
from app.services.preprocessing.pdf_loader import extract_text_from_pdf

router = APIRouter(prefix="/debug", tags=["Debug"])


@router.get("/pdf-extract",dependencies=[Depends(verify_admin_key)])
def debug_pdf_extract(doc_id: str):
    pdf_path = Path(f"storage/pdfs/rbi/{doc_id}.pdf")

    if not pdf_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"PDF not found for doc_id={doc_id}"
        )

    pages = extract_text_from_pdf(str(pdf_path))

    if not pages:
        return {
            "doc_id": doc_id,
            "message": "No extractable text (scanned or invalid PDF)"
        }

    return {
        "doc_id": doc_id,
        "total_pages": len(pages),
        "sample_page": pages[0]
    }


@router.get("/chunk",dependencies=[Depends(verify_admin_key)])
def debug_chunk(doc_id: str):
    pdf_path = Path(f"app/storage/pdfs/rbi/{doc_id}.pdf")

    if not pdf_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"PDF not found for doc_id={doc_id}"
        )

    pages = extract_text_from_pdf(str(pdf_path))

    if not pages:
        return {
            "doc_id": doc_id,
            "message": "No text available for chunking"
        }

    chunks = []
    for page in pages:
        chunks.append({
            "page": page["page"],
            "chunk": page["text"][:500]
        })

    return {
        "doc_id": doc_id,
        "chunks_preview": chunks[:3]
    }
from fastapi import APIRouter, HTTPException
from app.services.scraper.rbi_master_content_scrapper import extract_master_document_content
from fastapi import APIRouter, Depends
from app.core.security import verify_admin_key


router = APIRouter(prefix="/debug", tags=["Debug"])

@router.get("/html-extract",dependencies=[Depends(verify_admin_key)])
def debug_html_extract(url: str):
    text = extract_master_document_content(url)
    if not text:
        raise HTTPException(status_code=404, detail="No content extracted")
    return {
        "url": url,
        "length": len(text),
        "sample": text[:1500]
    }
