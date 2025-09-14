import subprocess
import sys

from test import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "test", "--version"]
    print("Running command:", " ".join(cmd))
    assert subprocess.check_output(cmd).decode().strip() == __version__
