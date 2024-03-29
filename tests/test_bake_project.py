import os
import shlex
import subprocess
import sys
from contextlib import contextmanager


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    result = cookies.bake(extra_context={"project_slug": "test_project"})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "test_project"


def test_run_tests(cookies):
    py_version = sys.version_info
    tox_command = f"py{py_version.major}{py_version.minor}"

    result = cookies.bake(extra_context={"project_slug": "test_project_tests"})
    with inside_dir(str(result.project_path)):
        subprocess.check_output(shlex.split(f"python -m tox -e {tox_command}"))
