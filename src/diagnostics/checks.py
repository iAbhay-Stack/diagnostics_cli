import os

IMPORTANT_VARS = [
    "PATH",
    "HOME",
    "USER",
    "USERNAME",
]


def inspect_environment():

    result = {}

    for var in IMPORTANT_VARS:
        result[var] = os.getenv(var)

    return result


import shutil

TOOLS = [
    "git",
    "python",
    "pip",
    "docker",
    "node",
    "npm",
    "code",
]


def detect_tools():

    return {tool: shutil.which(tool) is not None for tool in TOOLS}
