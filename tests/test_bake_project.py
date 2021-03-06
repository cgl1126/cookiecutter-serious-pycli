import os
import subprocess
from contextlib import contextmanager
from os.path import isdir, isfile


@contextmanager
def inside_dir(path):
    """
    Execute code from inside the given directory
    :param path: String, path of the directory the command is being run.
    """
    if not isinstance(path, str):
        path = str(path)
    old_path = os.getcwd()

    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    result = cookies.bake(
        extra_context={
            'project_name': 'test-project',
            'project_slug': 'test_project',
        }
    )
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'test-project'

    files = [
        '.gitignore',
        '.pylintrc',
        'CHANGELOG.md',
        'LICENSE',
        'README.md',
        'setup.cfg',
        'setup.py',
    ]
    dirs = [
        'src',
        'src/test_project',
        'tests',
    ]
    with inside_dir(result.project):
        for path in files:
            assert isfile(path)
        for path in dirs:
            assert isdir(path)


def test_run_flake8(cookies):
    result = cookies.bake(extra_context={'project_slug': 'flake8_compat'})
    with inside_dir(result.project):
        subprocess.check_call(['flake8'])


def test_run_pytest(cookies):
    result = cookies.bake(extra_context={'project_name': 'run-pytest'})
    with inside_dir(result.project):
        subprocess.check_call(['git', 'init'])
        subprocess.check_call(['python', '-m', 'venv', '.env'])
        subprocess.check_call(
            '. .env/bin/activate && pip install .[dev]',
            shell=True,
        )
        subprocess.check_call('. .env/bin/activate && pytest', shell=True)
