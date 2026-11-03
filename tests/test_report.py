from diagnostics.report import (
    generate_json_report,
    generate_text_report,
)


def test_text_report():
    report = generate_text_report(
        {"python_version": "3.12"},
        {},
        {},
    )

    assert "Developer Environment Diagnostics" in report
    assert "Machine Information" in report
    assert "python_version" in report

def test_json_report():

    report = generate_json_report(
        {"python_version": "3.12"},
        {},
        {},
    )

    assert '"machine"' in report
