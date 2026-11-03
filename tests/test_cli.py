from diagnostics.cli import build_parser


def test_parser():

    parser = build_parser()

    args = parser.parse_args([])

    assert args.verbose is False
    assert args.json is False


def test_json_flag():

    parser = build_parser()

    args = parser.parse_args(["--json"])

    assert args.json is True
