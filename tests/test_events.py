from diagnostics.events import (
    analyze,
    load_events,
)


def test_load_events(sample_event_file):

    events = load_events(sample_event_file)

    assert len(events) == 2


def test_event_analysis(sample_event_file):

    events = load_events(sample_event_file)

    summary = analyze(events)

    assert summary["total_events"] == 2

    assert summary["errors"] == 1

    assert summary["failed_requests"] == 1


import pytest


def test_missing_file():

    with pytest.raises(FileNotFoundError):
        load_events("missing.json")
