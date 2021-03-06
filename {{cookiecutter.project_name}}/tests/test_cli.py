import re
import subprocess

from _pytest.capture import CaptureFixture
from pytest import mark, raises

from {{ cookiecutter.project_slug }} import main


@mark.integration
@mark.parametrize('argv', [
    ['{{ cookiecutter.project_slug }}'],
    ['python', '-m', '{{ cookiecutter.project_slug }}'],
])  # yapf: disable
def test_from_cli(argv):
    out = subprocess.check_output(argv)
    assert not out


@mark.integration
@mark.parametrize('argv', [
    ['-h'],
    ['--help'],
])
def test_help(argv, capsys: CaptureFixture):
    with raises(SystemExit) as exc_info:
        main(argv)
    assert exc_info.value.code == 0

    out, err = capsys.readouterr()
    assert 'show this help message and exit' in out
    assert not err


@mark.integration
@mark.parametrize('argv', [
    ['-V'],
    ['--version'],
])
def test_version(argv, capsys: CaptureFixture):
    with raises(SystemExit) as exc_info:
        main(argv)
    assert exc_info.value.code == 0

    out, err = capsys.readouterr()
    assert re.match(r'\d+\.\d+\..*', out)
    assert not err


@mark.integration
def test_default(capsys: CaptureFixture):
    main([])
    out, err = capsys.readouterr()
    assert not out
    assert not err


@mark.integration
@mark.parametrize('argv', [
    ['-p'],
    ['--print'],
])
def test_print(argv, capsys: CaptureFixture):
    main(argv)
    out, err = capsys.readouterr()
    assert 'Hello world!' in out
    assert not err
