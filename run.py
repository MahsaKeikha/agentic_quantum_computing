from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "review a quantum computing research package",
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

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
