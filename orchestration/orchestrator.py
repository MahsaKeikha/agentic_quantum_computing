"""Deterministic F82 orchestration with explicit human review."""
from AGENTS.problem_formulation_agent import run as formulate
from AGENTS.circuit_architecture_agent import run as architect
from AGENTS.noise_error_agent import run as assess_error
from AGENTS.evidence_agent import run as assess_evidence
from AGENTS.reviewer_agent import run as review


def run(context: dict) -> dict:
    outputs = [
        formulate(context),
        architect(context),
        assess_error(context),
        assess_evidence(context),
        review(context),
    ]
    return {"system": "F82", "outputs": outputs, "human_review_required": True}
