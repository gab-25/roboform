import unittest
from unittest.mock import patch
from roboform.cli import run, Cmd


class TestCli(unittest.TestCase):

    def test_run_no_args(self):
        with patch("roboform.cli.print_menu") as mock_print_menu:
            run()

        mock_print_menu.assert_called_once()

    def test_run_help(self):
        with patch("roboform.cli.print_help") as mock_print_help:
            run(Cmd.HELP)

        mock_print_help.assert_called_once()

    def test_run_create(self):
        with patch("roboform.cli.create_config") as mock_create_config:
            run(Cmd.CREATE)

        mock_create_config.assert_called_once()

    def test_run_list(self):
        with patch("roboform.cli.list_configs") as mock_list_configs:
            run(Cmd.LIST)

        mock_list_configs.assert_called_once()

    def test_run_remove(self):
        with patch("roboform.cli.remove_config") as mock_remove_config:
            run(Cmd.REMOVE)

        mock_remove_config.assert_called_once()

    def test_run_edit(self):
        with patch("roboform.cli.edit_config") as mock_edit_config:
            run(Cmd.EDIT)

        mock_edit_config.assert_called_once()


if __name__ == "__main__":
    unittest.main()
