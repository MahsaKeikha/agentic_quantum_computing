from orchestration.orchestrator import run
from safety.policy import check


def valid_context():
    return {
        "problem_formulation_reviewed": True,
        "circuit_architecture_reviewed": True,
        "backend_assumptions_reviewed": True,
        "noise_model_reviewed": True,
        "simulation_or_hardware_results_verified": True,
        "evidence_provenance_reviewed": True,
        "uncertainty_reviewed": True,
        "reproducibility_reviewed": True,
        "human_approval": True,
    }


def test_smoke_and_authority_boundaries():
    result = run(valid_context())
    assert result["system"] == "F82"
    assert result["human_review_required"] is True
    assert result["autonomous_scientific_authority"] is False
    assert result["unreviewed_hardware_execution"] is False


def test_complete_review_can_release_research_package():
    assert run(valid_context())["release_allowed"] is True


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_quantum_advantage_claim_is_not_autonomously_authorized():
    assert check(valid_context(), "claim_quantum_advantage")["allowed"] is False


def test_backend_mismatch_blocks_release():
    context = valid_context()
    context["backend_mismatch"] = True
    assert run(context)["release_allowed"] is False


def test_noise_model_gap_blocks_release():
    context = valid_context()
    context["noise_model_inadequate"] = True
    assert run(context)["release_allowed"] is False


def test_unreproduced_result_blocks_release():
    context = valid_context()
    context["result_not_reproduced"] = True
    assert run(context)["release_allowed"] is False


def test_unsupported_advantage_claim_blocks_release():
    context = valid_context()
    context["unsupported_advantage_claim"] = True
    assert run(context)["release_allowed"] is False
