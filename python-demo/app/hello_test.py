import subprocess
import sys
import os

def test_hello_runs():
    # Bazel sets PWD to the runfiles dir; using bazel path is safer:
    # But for simplicity, just run the binary through python entry
    # In real projects, prefer integration via rules or runfiles helper.
    completed = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), "hello.py")],
        capture_output=True, text=True
    )
    assert completed.returncode == 0
    assert "Hello, Bazel!" in completed.stdout
