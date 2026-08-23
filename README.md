# F82 Agentic Quantum Computing

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed five-agent reference architecture for quantum computing research across problem formulation, circuit architecture, backend and noise assumptions, evidence review, reproducibility, and qualified human scientific review.

F82 is designed as a research reference for teams evaluating quantum algorithms or experiments without collapsing theoretical possibility, noiseless simulation, noisy simulation, and hardware execution into the same level of evidence.

The repository supports research analysis. It does not autonomously claim quantum advantage, experimental confirmation, practical superiority, or hardware validation, and it does not execute unreviewed quantum hardware jobs.

## Research lifecycle

```text
research problem
      |
      v
problem formulation
      |
      v
circuit architecture
      |
      v
noise + backend review
      |
      v
evidence + reproducibility
      |
      v
qualified human review
```

The workflow is fail closed. A compelling circuit or simulation is not sufficient if backend assumptions, noise behavior, classical baselines, provenance, or reproducibility remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Problem Formulation Agent | Defines the computational problem, objective, assumptions, constraints and comparison target | What problem is being solved, under which assumptions, and compared with what? |
| Circuit Architecture Agent | Structures the quantum algorithm and circuit implementation | Is the circuit logically valid and compatible with the intended model and backend constraints? |
| Noise and Error Agent | Reviews device noise, readout, decoherence, sampling and mitigation assumptions | Are the dominant error mechanisms characterized well enough for the stated claim? |
| Evidence Agent | Tracks simulation, hardware, literature and comparative evidence | What evidence actually supports the result, and at what maturity level? |
| Reviewer Agent | Applies qualified scientific review and final research authority | Are the conclusions proportional to the verified evidence and uncertainty? |

No single agent can independently declare quantum advantage or experimental confirmation.

## Repository structure

```text
AGENTS/
├── problem_formulation_agent.py
├── circuit_architecture_agent.py
├── noise_error_agent.py
├── evidence_agent.py
└── reviewer_agent.py

SKILLS/
├── problem_decomposition.py
├── circuit_reasoning.py
├── error_reasoning.py
├── evidence_discipline.py
└── human_review.py

TOOLS/
├── assumption_tracker.py
├── circuit_register.py
├── noise_model.py
├── evidence_register.py
└── review_gate.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The separation between agents, tools, state, evaluation and governance is intended to keep quantum research claims traceable.

## Problem formulation

Quantum research should begin with a precise problem statement rather than with a preferred algorithm.

A useful problem record can include:

```text
problem_id
problem_class
input_definition
output_definition
objective
constraints
problem_size
quantum_model
classical_baseline
resource_metric
success_metric
assumptions
claim_type
```

The `TOOLS/assumption_tracker.py` layer keeps assumptions explicit so they can be challenged later.

## Classical baseline requirement

Comparative quantum claims require an appropriate classical baseline.

The baseline should be documented with enough detail to determine whether the comparison is meaningful. Depending on the study, that can include:

- classical algorithm
- implementation language
- hardware
- optimization level
- approximation quality
- runtime definition
- memory usage
- parallelism
- preprocessing
- stopping criteria
- error tolerance

A weak or obsolete baseline can create a misleading appearance of quantum advantage.

The system therefore blocks comparative claims when the classical comparison is missing or materially inadequate.

## Circuit architecture

The Circuit Architecture Agent records the structure of the proposed quantum computation.

`TOOLS/circuit_register.py` provides the reference circuit record.

Useful fields include:

```text
circuit_id
algorithm_family
logical_qubits
physical_qubits_if_mapped
gate_set
circuit_depth
two_qubit_gate_count
measurement_scheme
initial_state
ansatz_or_oracle
connectivity_assumptions
transpilation_settings
backend_target
software_version
```

The circuit should be evaluated at the level relevant to the claim. A high-level algorithm sketch is not equivalent to a transpiled circuit executable on a specific device.

## Logical versus physical resources

Quantum algorithms often describe logical resources while near-term hardware executes noisy physical operations.

The README explicitly distinguishes:

```text
logical algorithm resources
        !=
physical hardware resources
```

For fault-tolerant claims, resource estimates should document assumptions about:

- error-correcting code
- logical error target
- physical error rates
- code distance
- magic-state or non-Clifford overhead
- connectivity
- syndrome extraction
- runtime overhead
- physical qubit count

The repository does not assume a logical-qubit count maps directly to deployable physical hardware.

## Backend compatibility

A circuit can be mathematically valid but unsuitable for a target backend.

Backend review can include:

- supported gate set
- native connectivity
- qubit count
- measurement model
- reset support
- dynamic-circuit support
- mid-circuit measurement
- classical feedforward
- coherence constraints
- calibration state
- queue or execution constraints

A backend mismatch is a release blocker when the result is presented as hardware-relevant.

## Transpilation and compilation

Transpilation can materially change circuit depth, two-qubit gate count and expected error.

A reproducible hardware-oriented study should record:

- compiler/transpiler
- version
- optimization level
- routing strategy
- layout selection
- seed where relevant
- native gate decomposition
- resulting circuit depth
- resulting two-qubit gate count

Results should be tied to the compiled circuit actually executed rather than only the abstract source circuit.

## Simulation evidence

Simulation is valuable, but the evidence level depends on the simulator.

Useful distinctions include:

- ideal statevector simulation
- ideal shot-based simulation
- noisy simulation
- approximate simulation
- tensor-network simulation
- stabilizer simulation
- hardware-calibrated noise simulation

The result should state which simulator was used, its assumptions, numerical approximations, and whether the circuit size was within a regime where the simulation itself remained trustworthy.

Ideal simulation does not establish hardware feasibility.

## Hardware evidence

Hardware execution should preserve enough provenance to reproduce or interpret the experiment.

Useful evidence can include:

```text
provider
backend
execution_date
backend_configuration
calibration_snapshot
qubit_mapping
compiled_circuit
shots
job_identifier
raw_counts
postprocessing
mitigation
software_version
```

Hardware behavior can drift over time. A result from one calibration state should not be treated as timeless evidence for the backend.

## Noise model

`TOOLS/noise_model.py` provides the reference abstraction for error assumptions.

A noise review can consider:

- single-qubit gate error
- two-qubit gate error
- readout error
- state-preparation error
- amplitude damping
- dephasing
- leakage
- crosstalk
- coherent error
- drift
- idle error
- correlated error

A simplified noise model may be useful for research, but its limitations should remain visible.

## Decoherence

Circuit duration should be interpreted relative to hardware coherence behavior.

Relevant quantities can include T1, T2, gate duration, measurement duration and idle time.

The workflow should not conclude that a circuit is practical merely because its logical depth is modest if the compiled execution remains long relative to device coherence or accumulates substantial error.

## Readout error

Measurement error can materially affect observed distributions.

If readout mitigation is applied, record:

- calibration method
- calibration time
- model assumptions
- correction procedure
- whether mitigation data were independent of final evaluation
- uncertainty introduced by the correction

Mitigated results should not be described as equivalent to error-free measurements.

## Shot noise and sampling uncertainty

Finite sampling creates statistical uncertainty even on ideal hardware.

For shot-based results, report the number of shots and appropriate uncertainty or confidence intervals where relevant.

A small change in estimated probability should not be interpreted as a meaningful improvement when it is within sampling uncertainty.

## Error mitigation versus error correction

F82 distinguishes error mitigation from fault-tolerant quantum error correction.

Error mitigation can reduce bias under assumptions but does not create a fully fault-tolerant logical computation.

Examples can include:

- readout mitigation
- zero-noise extrapolation
- probabilistic error cancellation
- symmetry verification
- postselection

Quantum error correction introduces encoded logical qubits, syndrome measurements, correction logic and substantial resource overhead.

The two concepts should not be conflated in claims or documentation.

## Variational algorithms

For variational quantum algorithms, performance depends on both the quantum circuit and the classical optimization loop.

A reproducible study should record:

- ansatz
- initialization
- optimizer
- optimizer settings
- stopping rule
- random seed
- objective estimator
- shot budget
- gradient method
- parameter bounds
- number of optimization iterations

Optimization instability, barren plateaus, local minima or noise sensitivity should be included in uncertainty analysis where relevant.

## Benchmarking

Quantum benchmarking should define the target clearly.

Possible benchmark dimensions include:

- fidelity
- circuit depth
- gate count
- execution time
- sampling quality
- success probability
- approximation ratio
- energy error
- logical error rate
- physical resource estimate

A benchmark metric should correspond to the scientific question rather than being selected only because it favors the quantum method.

## Quantum advantage claims

Claims of quantum advantage, superiority or speedup require particularly strong evidence.

The review should distinguish among:

- asymptotic theoretical speedup
- oracle/query complexity advantage
- resource-estimate advantage
- simulated performance advantage
- hardware demonstration
- practical wall-clock advantage
- economic advantage

These are different claims and require different evidence.

F82 blocks unsupported statements that collapse them into one category.

## Experimental confirmation boundary

A simulation result is not experimental confirmation.

A hardware run is also not automatically confirmation of a broad scientific claim if the experiment lacks controls, adequate statistics, independent replication or an appropriate baseline.

The system therefore tracks the maturity of each result explicitly.

## Evidence provenance

`TOOLS/evidence_register.py` records evidence lineage.

Useful fields include:

```text
evidence_id
claim
source_type
source
backend_or_simulator
circuit_version
dataset_or_input
execution_date
analysis_version
uncertainty
limitations
replication_state
review_state
```

The repository should never fabricate papers, hardware jobs, calibration records, benchmark results, or independent replication.

## Literature evidence

Published quantum results should be interpreted in context.

Evidence review can consider:

- theoretical versus experimental work
- simulator versus hardware result
- system size
- hardware generation
- baseline quality
- error assumptions
- replication
- peer review
- known critiques
- later improvements in classical algorithms

Quantum-computing comparisons can become stale when classical algorithms improve, so baseline provenance matters.

## Uncertainty

Material uncertainty can arise from:

- sampling
- calibration drift
- noise-model mismatch
- compiler choices
- optimizer randomness
- backend mapping
- measurement mitigation
- finite-size effects
- model assumptions
- classical baseline uncertainty

The final synthesis should state uncertainty explicitly rather than converting it into a single confident number.

## Reproducibility

A reproducible quantum study should version at minimum:

- problem definition
- assumptions
- circuit source
- circuit version
- compiler and transpiler
- backend or simulator
- calibration snapshot where available
- noise model
- qubit mapping
- shot count
- optimizer settings where applicable
- seeds
- classical baseline
- raw results
- postprocessing
- mitigation
- software environment

A changed backend, calibration, transpiler or mitigation pipeline should create a new evidence version.

## Independent replication

Important claims should distinguish rerunning the same code from independent replication.

Replication can require separation in one or more dimensions:

- backend
- device generation
- research group
- software implementation
- compiler
- dataset or problem instance
- experimental date

The appropriate standard depends on the claim.

## Fail-closed research governance

The research release gate blocks advancement when required evidence remains unresolved.

Reference blockers include:

- problem formulation incomplete
- assumptions missing
- circuit architecture unreviewed
- backend mismatch
- transpilation provenance missing
- circuit verification failed
- noise model inadequate
- shot uncertainty uncharacterized
- readout or mitigation assumptions undocumented
- hardware calibration provenance missing
- classical baseline missing for comparative claims
- comparative baseline materially unfair
- computation unreproduced
- evidence provenance missing
- contradictory evidence unresolved
- uncertainty uncharacterized
- independent confirmation missing where the claim requires it
- unsupported quantum-advantage claim
- unsupported experimental-confirmation claim
- unreviewed hardware execution requested
- qualified human approval missing

Human approval occurs after technical gates. It does not convert missing evidence into validated evidence.

## Human scientific authority

F82 must not autonomously:

- claim quantum advantage
- claim practical superiority
- claim experimental confirmation
- claim a result is proven beyond the available evidence
- fabricate citations or experimental results
- hide uncertainty
- execute unreviewed hardware jobs
- represent simulator output as hardware evidence
- represent error mitigation as fault tolerance
- suppress contradictory evidence

Final scientific interpretation remains with qualified researchers.

## End-to-end reference workflow

A typical F82 workflow follows this sequence:

1. Define the computational problem and intended claim.
2. Record assumptions and the appropriate classical baseline.
3. Define the quantum algorithm and circuit architecture.
4. Check logical correctness and resource requirements.
5. Map the circuit to backend constraints if hardware relevance is claimed.
6. Record transpilation and compiled-circuit characteristics.
7. Define the simulator or hardware evidence level.
8. Review noise, decoherence, readout, sampling and mitigation assumptions.
9. Run or register verified simulation or reviewed hardware results.
10. Compare against an appropriate classical baseline.
11. Characterize uncertainty and robustness.
12. Preserve evidence provenance and reproducibility information.
13. Review independent confirmation requirements.
14. Apply fail-closed research gates.
15. Require qualified human scientific approval before strong claims are released.

## Evaluation and held-out governance suite

The repository includes held-out evaluation under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test research discipline as well as technical plausibility.

Useful dimensions include:

- assumption tracking
- backend mismatch detection
- circuit verification enforcement
- noise-model review
- simulator/hardware distinction
- calibration provenance
- shot-uncertainty enforcement
- classical-baseline enforcement
- evidence-provenance enforcement
- reproducibility enforcement
- quantum-advantage claim blocking
- experimental-confirmation claim blocking
- hardware-execution gating
- human-review enforcement

Strong held-out cases should intentionally contain impressive-looking results with hidden baseline, noise, provenance or reproducibility problems.

## Failure states

Useful explicit states include:

```text
PROBLEM FORMULATION INCOMPLETE
ASSUMPTIONS MISSING
CIRCUIT UNVERIFIED
BACKEND MISMATCH
TRANSPILATION PROVENANCE MISSING
NOISE MODEL INADEQUATE
SHOT UNCERTAINTY UNCHARACTERIZED
CALIBRATION PROVENANCE MISSING
CLASSICAL BASELINE REQUIRED
COMPARISON NOT FAIR
EVIDENCE PROVENANCE MISSING
RESULT NOT REPRODUCED
CONTRADICTORY EVIDENCE UNRESOLVED
UNCERTAINTY UNCHARACTERIZED
QUANTUM ADVANTAGE NOT ESTABLISHED
EXPERIMENTAL CONFIRMATION NOT ESTABLISHED
HARDWARE EXECUTION REQUIRES REVIEW
HUMAN APPROVAL REQUIRED
```

The system should fail visibly rather than silently weaken the research standard.

## Observability

The `observability/` layer can track research workflow state.

Useful signals include:

- assumptions unresolved
- circuit version
- backend target
- circuit depth
- two-qubit gate count
- simulator versus hardware state
- noise-model status
- calibration age
- shot count
- mitigation status
- baseline status
- evidence completeness
- reproducibility state
- human-review state

Operational traces support auditability but do not substitute for scientific evidence.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run the repository checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11 and 3.12.

## L3 Gold Standard

F82 follows the library's L3 Gold Standard structure through specialist agents, deterministic evidence tools, explicit state and orchestration, held-out governance evaluation, observability, CI, fail-closed research gates and mandatory qualified human review.

This maturity designation describes repository architecture and governance. It is not evidence of quantum advantage, hardware superiority, fault tolerance, experimental confirmation, commercial readiness, or scientific consensus.

## Extending F82

Common extensions include:

- Qiskit-compatible adapters
- Cirq-compatible adapters
- PennyLane-compatible workflows
- cloud quantum backend adapters
- simulator integrations
- transpiler registries
- circuit optimization tools
- calibration snapshot stores
- experiment tracking
- benchmark registries
- classical solver integrations
- resource-estimation tools
- fault-tolerant resource models
- hardware job provenance
- reproducibility archives

New integrations should preserve backend provenance, circuit versioning, assumptions, uncertainty, evidence maturity and human scientific review.

## Example applications

F82 can serve as a reference architecture for research involving:

- variational quantum algorithms
- quantum optimization research
- quantum simulation
- quantum chemistry algorithms
- quantum machine learning research
- quantum error mitigation
- quantum error correction studies
- circuit compilation
- backend benchmarking
- quantum resource estimation
- classical versus quantum comparative studies

The appropriate evidence standard depends on the claim being made.

## Design principles

1. Define the scientific claim before selecting the quantum algorithm.
2. Track assumptions explicitly.
3. Separate logical circuits from compiled hardware circuits.
4. Separate ideal simulation, noisy simulation and hardware evidence.
5. Treat noise, sampling and calibration as part of the result.
6. Use appropriate classical baselines for comparative claims.
7. Distinguish mitigation from error correction and fault tolerance.
8. Preserve complete execution and evidence provenance.
9. Fail closed on unsupported advantage or confirmation claims.
10. Keep final scientific authority with qualified human researchers.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted and extended subject to its license terms.

## Author

Mahsa Keikha

## Responsible use

Use F82 as a quantum-computing research and multi-agent governance reference. Validate circuit correctness, backend assumptions, noise models, classical comparisons, uncertainty, reproducibility and evidence provenance against the actual research problem before relying on conclusions.