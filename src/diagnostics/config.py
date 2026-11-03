from dataclasses import dataclass


@dataclass
class Config:
    verbose: bool
    report_type: str
    output: str | None
    events: str | None
