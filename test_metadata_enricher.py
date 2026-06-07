from app.services.metadata.metadata_enricher import enrich_document_metadata

# Sample extracted text (real RBI text)
sample_text = """
MASTER DIRECTIONS - RELIEF/SAVINGS BONDS

RBI/IDMD/2018-19/61
IDMD.CDD No.21/13.01.299/2018-19
July 2, 2018

The Chairman / Managing Director
State Bank of India
All Nationalized Banks

Master Directions on Relief/Savings Bonds
The rules and regulations applicable to Relief/Savings Bonds
have been updated with instructions issued up to June 30, 2018.

These directions are issued by the Department of Banking Regulation (DBR)
with effect from July 2, 2018.
"""

metadata = enrich_document_metadata(
    doc_id="test123",
    title="Master Directions on Relief/Savings Bonds",
    full_text=sample_text,
    document_type="MASTER_DIRECTION",
    source="RBI",
    url="https://www.rbi.org.in/example"
)

print("\n===== METADATA OUTPUT =====\n")
for k, v in metadata.items():
    print(f"{k}: {v}")
