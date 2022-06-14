import unittest
from unittest.mock import patch
from roboform.cli import run, Cmd, print_menu, create_config, list_configs, remove_config, edit_config, edit_settings, show_form_logs


class TestCli(unittest.TestCase):
    FORM_TEST = "form_test"
    LIST_CONFIGS_TEST = ["form_test_1", "form_test_2", "form_test_3"]

    @patch("roboform.cli.print_menu")
    def test_run_no_args(self, mock_print_menu):
        run()

        mock_print_menu.assert_called_once()

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

    @patch("roboform.cli.edit_settings")
    def test_run_settings(self, mock_edit_settings):
        run(Cmd.SETTINGS)

        mock_edit_settings.assert_called_once()

    @patch("builtins.input")
    def test_print_menu_input_create(self, mock_input):
        mock_input.return_value = 1
        value = print_menu()
        self.assertEqual(value, Cmd.CREATE)

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
    @patch("roboform.form_configs.FormConfigs.form_configs_exist")
    @patch("builtins.input")
    def test_create_config_no_arg(self, mock_input, mock_form_configs_exist, mock_write_file_form_configs):
        mock_input.return_value = self.FORM_TEST

        mock_form_configs_exist.return_value = True
        form_configs = create_config()
        self.assertEqual(form_configs, None)

        mock_form_configs_exist.return_value = False
        form_configs = create_config()
        self.assertEqual(form_configs.name, self.FORM_TEST)

    @patch("roboform.form_configs.FormConfigs.get_all_configs")
    def test_list_configs(self, mock_get_all_configs):
        mock_get_all_configs.return_value = self.LIST_CONFIGS_TEST
        configs = list_configs()

        self.assertEqual(configs, self.LIST_CONFIGS_TEST)

    @patch("roboform.form_configs.FormConfigs.remove_config")
    def test_remove_configs(self, mock_remove_config):
        mock_remove_config.return_value = True
        self.assertTrue(remove_config(self.FORM_TEST))

        mock_remove_config.return_value = False
        self.assertFalse(remove_config(self.FORM_TEST))

    @patch("roboform.form_configs.FormConfigs.get_all_configs")
    @patch("roboform.form_configs.FormConfigs.remove_config")
    @patch("builtins.input")
    def test_remove_configs_no_args(self, mock_input, mock_remove_config, mock_get_all_configs):
        test_form_removed = self.LIST_CONFIGS_TEST[0]
        mock_input.return_value = self.LIST_CONFIGS_TEST.index(test_form_removed) + 1
        mock_remove_config.return_value = True
        mock_get_all_configs.return_value = self.LIST_CONFIGS_TEST

        result = remove_config(None)

        mock_remove_config.assert_called_once_with(test_form_removed)
        self.assertTrue(result)

    @patch("roboform.form_configs.FormConfigs.edit_config")
    def test_edit_config(self, mock_edit_config):
        mock_edit_config.return_value = True
        self.assertTrue(edit_config(self.FORM_TEST))

        mock_edit_config.return_value = False
        self.assertFalse(edit_config(self.FORM_TEST))

    @patch("roboform.form_configs.FormConfigs.get_all_configs")
    @patch("roboform.form_configs.FormConfigs.edit_config")
    @patch("builtins.input")
    def test_edit_config_no_args(self, mock_input, mock_edit_config, mock_get_all_configs):
        test_form_edited = self.LIST_CONFIGS_TEST[0]
        mock_input.return_value = self.LIST_CONFIGS_TEST.index(test_form_edited) + 1
        mock_edit_config.return_value = True
        mock_get_all_configs.return_value = self.LIST_CONFIGS_TEST

        result = edit_config(None)

        mock_edit_config.assert_called_once_with(test_form_edited)
        self.assertTrue(result)

    @patch("roboform.form_configs.FormLogs.show_log")
    def test_show_log(self, mock_show_log):
        mock_show_log.return_value = True
        self.assertTrue(show_form_logs(self.FORM_TEST))

        mock_show_log.return_value = False
        self.assertFalse(show_form_logs(self.FORM_TEST))

    @patch("roboform.form_configs.FormConfigs.get_all_configs")
    @patch("roboform.form_configs.FormLogs.show_log")
    @patch("builtins.input")
    def test_show_log_no_args(self, mock_input, mock_show_log, mock_get_all_configs):
        test_form_edited = self.LIST_CONFIGS_TEST[0]
        mock_input.return_value = self.LIST_CONFIGS_TEST.index(test_form_edited) + 1
        mock_show_log.return_value = True
        mock_get_all_configs.return_value = self.LIST_CONFIGS_TEST

        result = show_form_logs(None)

        mock_show_log.assert_called_once_with(test_form_edited)
        self.assertTrue(result)

    @patch("roboform.global_configs.GlobalConfigs.edit_global_configs")
    def test_edit_settings(self, mock_edit_settings):
        mock_edit_settings.return_value = True
        self.assertTrue(edit_settings())

        mock_edit_settings.return_value = False
        self.assertFalse(edit_settings())


if __name__ == "__main__":
    unittest.main()
