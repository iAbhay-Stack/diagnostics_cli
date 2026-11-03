from dataclasses import dataclass


@dataclass
class Event:
    timestamp: str
    service: str
    level: str
    latency_ms: int | None
    status_code: int


@dataclass
class ServiceStats:
    service: str
    total: int
    errors: int
    warnings: int
    average_latency: float
    max_latency: int
