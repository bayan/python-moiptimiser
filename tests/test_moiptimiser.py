
from click.testing import CliRunner

from moiptimiser.cli import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ['tests/examples/2AP05.lp'])

    assert '9 non dominated vectors found' in result.output

    assert '(50, 24)' in result.output
    assert '(39, 28)' in result.output
    assert '(34, 29)' in result.output
    assert '(31, 30)' in result.output
    assert '(30, 31)' in result.output
    assert '(27, 36)' in result.output
    assert '(24, 45)' in result.output
    assert '(23, 46)' in result.output
    assert '(21, 55)' in result.output

    assert result.exit_code == 0
