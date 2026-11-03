from diagnostics.report import determine_exit_code


def test_exit_ok():

    assert determine_exit_code(None) == 0


def test_exit_warning():

    summary = {
        "errors": 0,
        "warnings": 1,
    }

    assert determine_exit_code(summary) == 1


def test_exit_error():

    summary = {
        "errors": 2,
        "warnings": 0,
    }

    assert determine_exit_code(summary) == 2
