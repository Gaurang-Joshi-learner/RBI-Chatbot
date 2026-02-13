import requests
from bs4 import BeautifulSoup


def extract_master_document_content(url: str) -> str:
    """
    Extracts main regulatory text from an RBI Master document page.
    """

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    content = (
        soup.find("div", id="divContent")
        or soup.find("div", id="content")
        or soup.find("article")
        or soup.body
    )

    if not content:
        return ""

    # Remove noisy elements
    for tag in content(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    for div in soup.find_all("div", class_=["topSection", "bottomSection"]):
        div.decompose()

    text = content.get_text(separator="\n", strip=True)

    if len(text) < 500:
        return ""

    return text
