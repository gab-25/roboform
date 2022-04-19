import unittest
from unittest.mock import patch
from roboform.__main__ import main
from roboform.cli import Cmd


class TestMain(unittest.TestCase):

    def test_main_help(self):
        test_args = ["--help"]

        with patch("roboform.__main__.run") as mock_run:
            main(test_args)

        mock_run.assert_called_once_with(Cmd.HELP)

    def test_main_create(self):
        test_args = ["--create"]

        with patch("roboform.__main__.run") as mock_run:
            main(test_args)

        mock_run.assert_called_once_with(Cmd.CREATE)

    def test_main_list(self):
        test_args = ["--list"]

        with patch("roboform.__main__.run") as mock_run:
            main(test_args)

        mock_run.assert_called_once_with(Cmd.LIST)

    def test_main_edit(self):
        test_args = ["--edit"]

        with patch("roboform.__main__.run") as mock_run:
            main(test_args)

        mock_run.assert_called_once_with(Cmd.EDIT)

    def test_main_not_valid(self):
        test_args = ["--test"]

        with patch("roboform.__main__.run") as mock_run:
            with patch("builtins.print"):
                main(test_args)

        mock_run.assert_called_once_with(Cmd.HELP)

    def test_main_no_args(self):
        test_args = []

        with patch("roboform.__main__.run") as mock_run:
            main(test_args)

        mock_run.assert_called_once_with(None)


if __name__ == "__main__":
    unittest.main()
