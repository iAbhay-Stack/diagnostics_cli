from diagnostics import constants


def test_exit_codes():
    assert constants.EXIT_OK == 0
    assert constants.EXIT_WARNING == 1
    assert constants.EXIT_ERROR == 2
    assert constants.EXIT_CONFIG == 3
    assert constants.EXIT_INTERNAL == 4
