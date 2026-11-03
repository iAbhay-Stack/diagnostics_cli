import os
import platform
import shutil
import sys


def inspect_machine():

    total, used, free = shutil.disk_usage("/")

    return {
        "python_version": platform.python_version(),
        "python_executable": sys.executable,
        "os": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "disk_total_gb": round(total / 1024**3, 2),
        "disk_used_gb": round(used / 1024**3, 2),
        "disk_free_gb": round(free / 1024**3, 2),
        "cwd": os.getcwd(),
        "virtual_env": sys.prefix != sys.base_prefix,
    }
