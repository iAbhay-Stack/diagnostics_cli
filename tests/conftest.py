import json

import pytest


@pytest.fixture
def sample_event_file(tmp_path):
    data = {
        "generated_for": "pytest",
        "events": [
            {
                "timestamp": "2026-08-01T09:00:00Z",
                "service": "billing-api",
                "level": "INFO",
                "latency_ms": 100,
                "status_code": 200,
            },
            {
                "timestamp": "2026-08-01T09:01:00Z",
                "service": "billing-api",
                "level": "ERROR",
                "latency_ms": 500,
                "status_code": 500,
            },
        ],
    }

    file = tmp_path / "events.json"

    file.write_text(json.dumps(data))

    return file
