import unittest
from roboform.global_configs import GlobalConfigs


class TestGlobalConfigs(unittest.TestCase):

    def test_get_instance(self):
        instance_1 = GlobalConfigs.get_instance()
        instance_2 = GlobalConfigs.get_instance()

        self.assertEqual(instance_1, instance_2)


if __name__ == "__main__":
    unittest.main()
