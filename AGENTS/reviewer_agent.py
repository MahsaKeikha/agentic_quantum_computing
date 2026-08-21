"""Performs final scientific and safety review."""

def run(context: dict) -> dict:
    return {"agent": "reviewer", "status": "review_required", "context": context}
