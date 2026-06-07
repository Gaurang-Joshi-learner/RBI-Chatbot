def normalize_documents(snapshot):
    """
    Accepts snapshot in dict or list format and
    always returns a dict {doc_id: doc}
    """

    if snapshot is None:
        return {}

    # Case 1: Proper snapshot dict
    if isinstance(snapshot, dict):
        docs = snapshot.get("documents", {})
        if isinstance(docs, dict):
            return docs

    # Case 2: List of documents
    if isinstance(snapshot, list):
        normalized = {}
        for doc in snapshot:
            doc_id = doc.get("doc_id")
            if doc_id:
                normalized[doc_id] = doc
        return normalized

    return {}


def detect_changes(old_snapshot, new_snapshot):
    old_docs = normalize_documents(old_snapshot)
    new_docs = normalize_documents(new_snapshot)

    added = []
    removed = []
    unchanged = []

    for doc_id, doc in new_docs.items():
        if doc_id not in old_docs:
            added.append(doc)
        else:
            unchanged.append(doc)

    for doc_id, doc in old_docs.items():
        if doc_id not in new_docs:
            removed.append(doc)

    return {
        "added": added,
        "removed": removed,
        "unchanged": unchanged,
        "counts": {
            "added": len(added),
            "removed": len(removed),
            "unchanged": len(unchanged),
        },
    }
