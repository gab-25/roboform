import unittest
from unittest.mock import patch
from roboform.cli import run, Cmd, print_menu


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

    def test_print_menu_input_help(self):
        with patch("builtins.print"):
            with patch("builtins.input") as mock_input:
                mock_input.return_value = 1
                value = print_menu()
                self.assertEqual(value, Cmd.HELP)

    def test_print_menu_input_not_valid(self):
        with patch("builtins.print"):
            with patch("builtins.input") as mock_input:
                with self.assertRaises(SystemExit) as mock_exit:
                    mock_input.return_value = len(Cmd) + 1
                    print_menu()
                self.assertEqual(mock_exit.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
