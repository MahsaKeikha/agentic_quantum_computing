"""Deterministic F82 orchestration with fail-closed research governance."""

from AGENTS.circuit_architecture_agent import run as architect
from AGENTS.evidence_agent import run as assess_evidence
from AGENTS.noise_error_agent import run as assess_error
from AGENTS.problem_formulation_agent import run as formulate
from AGENTS.reviewer_agent import run as review
from safety.policy import check


def run(context: dict) -> dict:
    outputs = [
        formulate(context),
        architect(context),
        assess_error(context),
        assess_evidence(context),
        review(context),
    ]
    governance = check(context)
    return {
        "system": "F82",
        "outputs": outputs,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_review_required": True,
        "autonomous_scientific_authority": False,
        "unreviewed_hardware_execution": False,
    }
