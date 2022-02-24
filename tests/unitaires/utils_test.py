import unittest

from utils.misc import parse_command_line

class UtilsTest(unittest.TestCase):

    def test_parse_command_line(self):
        tester = ["--settings=test.ini","--log_level=40","--log_info_file=info.log", "--log_crit_file=crit.log"]
        result = parse_command_line(tester)

        if(result["conf_file_name"] != "test.ini" or result["log_level"] != 40 or result["log_info"] != "info.log" or result["log_critical"] != "crit.log"):
            self.assertFalse(True)

        self.assertTrue(True)
