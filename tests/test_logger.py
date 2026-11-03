from diagnostics.logger import setup_logger


def test_setup_logger():
    logger = setup_logger()
    assert logger.name == "diagnostics"


def test_setup_logger_verbose():
    logger = setup_logger(verbose=True)
    assert logger.name == "diagnostics"
