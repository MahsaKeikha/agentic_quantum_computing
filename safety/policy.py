"""Safety policy for F82 decision support."""

def check(context: dict) -> dict:
    return {
        "allowed": True,
        "human_review_required": True,
        "prohibited": ["unreviewed consequential execution", "fabricated evidence"]
    }
