"""Requires claims to remain traceable to explicit evidence."""

def apply(claims):
    return [{"claim": claim, "evidence_required": True} for claim in claims]
