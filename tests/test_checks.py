from diagnostics.checks import (
    detect_tools,
    inspect_environment,
)


def test_environment():
    env = inspect_environment()

    assert isinstance(env, dict)

    assert "PATH" in env


def test_tools():
    tools = detect_tools()

    assert isinstance(tools, dict)

    assert "python" in tools
    assert "git" in tools
