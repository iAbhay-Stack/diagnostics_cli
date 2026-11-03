import argparse
import sys

from .checks import detect_tools, inspect_environment
from .events import analyze, load_events
from .inspector import inspect_machine
from .logger import setup_logger
from .report import (
    determine_exit_code,
    generate_json_report,
    generate_text_report,
    save_report,
)
from .version import __version__


def build_parser():
    parser = argparse.ArgumentParser(
        prog="diagnostics",
        description="Developer Environment Diagnostics Tool",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON report",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose logging",
    )

    parser.add_argument(
        "--events",
        help="Path to event JSON file",
    )

    parser.add_argument(
        "--output",
        help="Save report",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    logger = setup_logger(args.verbose)

    try:
        logger.info("Diagnostics CLI Started")

        # -------------------------
        # Machine Inspection
        # -------------------------
        machine = inspect_machine()
        env = inspect_environment()
        tools = detect_tools()

        # -------------------------
        # Event Analysis
        # -------------------------
        event_summary = None

        if args.events:
            events = load_events(args.events)
            event_summary = analyze(events)

        # -------------------------
        # Generate Report
        # -------------------------
        if args.json:
            report = generate_json_report(
                machine,
                env,
                tools,
                event_summary,
            )
        else:
            report = generate_text_report(
                machine,
                env,
                tools,
                event_summary,
            )

        print(report)

        # -------------------------
        # Save Report
        # -------------------------
        if args.output:
            save_report(report, args.output)
            logger.info(f"Report saved to {args.output}")

        # -------------------------
        # Exit Code
        # -------------------------
        sys.exit(determine_exit_code(event_summary))

    except FileNotFoundError:
        logger.error("Event file not found.")
        sys.exit(3)

    except Exception as e:
        logger.exception("Unexpected error occurred.")
        print(f"Unexpected error: {e}")
        sys.exit(4)


if __name__ == "__main__":
    main()
