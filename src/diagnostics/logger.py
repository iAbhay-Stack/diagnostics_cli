import logging


def setup_logger(verbose: bool = False):
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(levelname)s | %(message)s",
    )

    return logging.getLogger("diagnostics")
