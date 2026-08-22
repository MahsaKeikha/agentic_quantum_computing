"""Fail-closed research governance for F82 quantum computing."""

REQUIRED_REVIEWS = (
    "problem_formulation_reviewed",
    "circuit_architecture_reviewed",
    "backend_assumptions_reviewed",
    "noise_model_reviewed",
    "simulation_or_hardware_results_verified",
    "evidence_provenance_reviewed",
    "uncertainty_reviewed",
    "reproducibility_reviewed",
    "human_approval",
)

BLOCKED_ACTIONS = {
    "claim_quantum_advantage",
    "claim_experimental_confirmation",
    "fabricate_evidence",
    "hide_uncertainty",
    "unreviewed_hardware_execution",
}


def check(context: dict, action: str = "research_release") -> dict:
    if action in BLOCKED_ACTIONS:
        return {
            "allowed": False,
            "human_review_required": True,
            "reason": "unsupported scientific or hardware authority is outside reference-system scope",
        }

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {
            "allowed": False,
            "human_review_required": True,
            "reason": "missing required quantum research review",
            "missing": missing,
        }

    blockers = []
    if context.get("backend_mismatch"):
        blockers.append("backend or simulator assumptions do not match the claimed result")
    if context.get("noise_model_inadequate"):
        blockers.append("noise model is inadequate for the claimed interpretation")
    if context.get("circuit_verification_failed"):
        blockers.append("circuit verification failed")
    if context.get("result_not_reproduced"):
        blockers.append("result was not reproduced")
    if context.get("evidence_provenance_missing"):
        blockers.append("evidence provenance is incomplete")
    if context.get("uncertainty_not_characterized"):
        blockers.append("material uncertainty is not characterized")
    if context.get("classical_baseline_missing"):
        blockers.append("classical baseline is missing for comparative claim")
    if context.get("unsupported_advantage_claim"):
        blockers.append("quantum advantage claim is unsupported")

    if blockers:
        return {
            "allowed": False,
            "human_review_required": True,
            "reason": "quantum research-integrity blocker",
            "blockers": blockers,
        }

    return {
        "allowed": True,
        "human_review_required": True,
        "reason": "research package approved after qualified human review",
    }
