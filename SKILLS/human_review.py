"""Reusable human authority and review skill."""

def apply(output: dict, approved: bool = False) -> dict:
    return {"output": output, "approved": approved, "requires_human_review": not approved}
