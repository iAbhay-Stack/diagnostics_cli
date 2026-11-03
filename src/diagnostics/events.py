import json

from .models import Event


def load_events(path):

    with open(path, "r", encoding="utf8") as f:
        data = json.load(f)

    return [Event(**event) for event in data["events"]]


from collections import defaultdict


def analyze(events):

    summary = {
        "total_events": len(events),
        "errors": 0,
        "warnings": 0,
        "average_latency": 0,
        "highest_latency": 0,
        "failed_requests": 0,
        "services": {},
    }

    latency_sum = 0
    latency_count = 0

    service_data = defaultdict(list)

    for event in events:
        service_data[event.service].append(event)

        if event.level == "ERROR":
            summary["errors"] += 1

        elif event.level == "WARN":
            summary["warnings"] += 1

        if event.status_code >= 500:
            summary["failed_requests"] += 1

        if event.latency_ms is not None:
            latency_sum += event.latency_ms
            latency_count += 1
            summary["highest_latency"] = max(
                summary["highest_latency"], event.latency_ms
            )

    summary["average_latency"] = (
        round(latency_sum / latency_count, 2) if latency_count else 0
    )

    for service, items in service_data.items():
        latencies = [e.latency_ms for e in items if e.latency_ms is not None]

        summary["services"][service] = {
            "events": len(items),
            "errors": sum(e.level == "ERROR" for e in items),
            "warnings": sum(e.level == "WARN" for e in items),
            "average_latency": (
                round(sum(latencies) / len(latencies), 2) if latencies else 0
            ),
        }

    return summary
