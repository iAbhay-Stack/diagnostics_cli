from diagnostics.inspector import inspect_machine


def test_machine_information():
    info = inspect_machine()

    assert isinstance(info, dict)

    assert "python_version" in info
    assert "os" in info
    assert "disk_total_gb" in info
    assert "disk_free_gb" in info
