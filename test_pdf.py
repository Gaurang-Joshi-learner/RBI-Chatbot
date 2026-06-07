from app.utils.pdf_utils import download_pdf

url = "https://rbidocs.rbi.org.in/rdocs/notification/PDFs/174MD.PDF"
path, h = download_pdf(url, "test_rbi")

print(path, h)
