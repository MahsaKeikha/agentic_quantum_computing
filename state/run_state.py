"""Explicit run state for reproducible orchestration."""
from dataclasses import dataclass, field

@dataclass
class RunState:
    run_id: str
    stage: str = "initialized"
    artifacts: dict = field(default_factory=dict)
    requires_human_review: bool = True
