import pytest

from hr import cli

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_fail_witout_arguments(parser):
    """
    without any arguments
    """
    with pytest.raises(SystemExit):
        parser.parse_args()

def test_parser_succeed_with_path(parser):
    """
     with some path
    """
    args = parser.parse_args(['/some/path'])
    assert args.path == '/some/path'

def test_parser_export_flag(parser):
    """
    with export flag
    """
    args = parser.parse_args(['/some/path'])
    assert  args.export == False

    args = parser.parse_args(['--export', '/some/path'])
    assert  args.export == True