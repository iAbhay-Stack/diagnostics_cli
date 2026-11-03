from diagnostics.config import Config


def test_config():
    config = Config(
        verbose=True,
        report_type="json",
        output="report.json",
        events="events.json",
    )

    assert config.verbose is True
    assert config.report_type == "json"
    assert config.output == "report.json"
