import unittest
import argparse
from unittest.mock import patch
from roboform.__main__ import main
from roboform.cli import Cmd


class TestMain(unittest.TestCase):
    FORM_TEST = "form_test"

    @patch("argparse.ArgumentParser.parse_args")
    @patch("roboform.__main__.run")
    def test_main_create(self, mock_run, mock_parser):
        mock_parser.return_value = argparse.Namespace(command="create", name=self.FORM_TEST)

        main()

        mock_run.assert_called_once_with(Cmd.CREATE, self.FORM_TEST)

    @patch("argparse.ArgumentParser.parse_args")
    @patch("roboform.__main__.run")
    def test_main_list(self, mock_run, mock_parser):
        mock_parser.return_value = argparse.Namespace(command="list")

        main()

        mock_run.assert_called_once_with(Cmd.LIST, None)

    @patch("argparse.ArgumentParser.parse_args")
    @patch("roboform.__main__.run")
    def test_main_edit(self, mock_run, mock_parser):
        mock_parser.return_value = argparse.Namespace(command="edit", name=self.FORM_TEST)

        main()

        mock_run.assert_called_once_with(Cmd.EDIT, self.FORM_TEST)

    @patch("argparse.ArgumentParser.parse_args")
    @patch("roboform.__main__.run")
    def test_main_no_args(self, mock_run, mock_parser):
        mock_parser.return_value = argparse.Namespace(command=None)
        main()

        mock_run.assert_called_once_with(None, None)


if __name__ == "__main__":
    unittest.main()
