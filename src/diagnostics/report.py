import json
from datetime import datetime


def generate_text_report(machine, env, tools, events=None):
    lines = []

    # Header
    lines.append("=" * 60)
    lines.append("Developer Environment Diagnostics")
    lines.append("=" * 60)
    lines.append(f"Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # Machine Information
    lines.append("Machine Information")
    lines.append("-" * 30)

    for key, value in machine.items():
        lines.append(f"{key:<20}: {value}")

    # Environment Variables
    lines.append("")
    lines.append("Environment Variables")
    lines.append("-" * 30)

    for key, value in env.items():
        status = "Present" if value else "Missing"
        lines.append(f"{key:<20}: {status}")

    # Developer Tools
    lines.append("")
    lines.append("Developer Tools")
    lines.append("-" * 30)

    for tool, installed in tools.items():
        status = "Installed" if installed else "Not Installed"
        lines.append(f"{tool:<20}: {status}")

    # Event Analysis
    if events:
        lines.append("")
        lines.append("Event Analysis")
        lines.append("-" * 30)

        lines.append(f"Total Events        : {events['total_events']}")
        lines.append(f"Errors              : {events['errors']}")
        lines.append(f"Warnings            : {events['warnings']}")
        lines.append(f"Failed Requests     : {events['failed_requests']}")
        lines.append(f"Average Latency     : {events['average_latency']:.2f} ms")
        lines.append(f"Highest Latency     : {events['highest_latency']} ms")

        lines.append("")
        lines.append("Service Statistics")
        lines.append("-" * 30)

        for service, stats in events["services"].items():
            lines.append(service)
            lines.append(f"  Events        : {stats['events']}")
            lines.append(f"  Errors        : {stats['errors']}")
            lines.append(f"  Warnings      : {stats['warnings']}")
            lines.append(f"  Avg Latency   : {stats['average_latency']:.2f} ms")
            lines.append("")

        # Overall Health
        lines.append("=" * 60)
        lines.append("Overall Health")

        if events["errors"] > 0:
            status = "ERROR"
        elif events["warnings"] > 0:
            status = "WARNING"
        else:
            status = "HEALTHY"

        lines.append(f"Status : {status}")

    return "\n".join(lines)


def generate_json_report(machine, env, tools, events=None):
    report = {
        "machine": machine,
        "environment": env,
        "tools": tools,
        "events": events,
    }

    return json.dumps(report, indent=4)


def save_report(report: str, filename: str):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)


def determine_exit_code(event_summary):
    if not event_summary:
        return 0

    if event_summary["errors"] > 0:
        return 2

    if event_summary["warnings"] > 0:
        return 1

    return 0
