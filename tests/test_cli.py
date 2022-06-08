import unittest
from unittest.mock import patch
from roboform.cli import run, Cmd, print_menu, create_config


class TestCli(unittest.TestCase):
    FORM_TEST = "form_test"

    @patch("roboform.cli.print_menu")
    def test_run_no_args(self, mock_print_menu):
        run()

        mock_print_menu.assert_called_once()

    @patch("roboform.cli.print_help")
    def test_run_help(self, mock_print_help):
        run(Cmd.HELP)

        mock_print_help.assert_called_once()

    @patch("roboform.cli.create_config")
    def test_run_create(self, mock_create_config):
        run(Cmd.CREATE)

        mock_create_config.assert_called_once()

    @patch("roboform.cli.list_configs")
    def test_run_list(self, mock_list_configs):
        run(Cmd.LIST)

        mock_list_configs.assert_called_once()

    @patch("roboform.cli.remove_config")
    def test_run_remove(self, mock_remove_config):
        run(Cmd.REMOVE)

        mock_remove_config.assert_called_once()

    @patch("roboform.cli.edit_config")
    def test_run_edit(self, mock_edit_config):
        run(Cmd.EDIT)

        mock_edit_config.assert_called_once()

    @patch("builtins.input")
    def test_print_menu_input_help(self, mock_input):
        mock_input.return_value = 1
        value = print_menu()
        self.assertEqual(value, Cmd.HELP)

    @patch("builtins.input")
    def test_print_menu_input_not_valid(self, mock_input: patch):
        with self.assertRaises(SystemExit) as mock_exit:
            mock_input.return_value = len(Cmd) + 1
            print_menu()
        self.assertEqual(mock_exit.exception.code, 1)

    @patch("roboform.form_configs.FormConfigs.write_file_form_configs")
    def test_create_config(self, mock_write_file_form_configs):
        form_configs = create_config(self.FORM_TEST)

        self.assertEqual(form_configs.name, self.FORM_TEST)

    @patch("roboform.form_configs.FormConfigs.write_file_form_configs")
    @patch("builtins.input")
    def test_create_config_no_arg(self, mock_input, mock_write_file_form_configs):
        mock_input.return_value = self.FORM_TEST
        form_configs = create_config()

        self.assertEqual(form_configs.name, self.FORM_TEST)


if __name__ == "__main__":
    unittest.main()
