from app.services.extraction.html_extractor import extract_rbi_html_text

URL = "https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10298"

data = extract_rbi_html_text(URL)

print("===== STEP 1: EXTRACTION TEST =====")
print("TITLE:", data["title"])
print("TEXT LENGTH:", len(data["text"]))
print("\nTEXT SAMPLE:\n")
print(data["text"][:800])

assert len(data["text"]) > 2000
print("\n✅ STEP 1 PASSED: Valid RBI regulation extracted")
