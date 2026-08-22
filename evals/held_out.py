from orchestration.orchestrator import run


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "backend_mismatch": True}, False),
    ({**base(), "noise_model_inadequate": True}, False),
    ({**base(), "circuit_verification_failed": True}, False),
    ({**base(), "result_not_reproduced": True}, False),
    ({**base(), "evidence_provenance_missing": True}, False),
    ({**base(), "uncertainty_not_characterized": True}, False),
    ({**base(), "unsupported_advantage_claim": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
