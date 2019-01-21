import unittest
from syntime.util.RegexUtil import RegexUtil

class RegexUtilTest(unittest.TestCase):

    def testRegex(self):
        regexUtil = RegexUtil()
        self.assertIsNotNone(regexUtil.YEAR_PATTERN_1.fullmatch('2019'))
        self.assertIsNotNone(regexUtil.MONTH_PATTERN.fullmatch('January'))
        self.assertIsNotNone(regexUtil.DATE_PATTERN_1.fullmatch('27-01-2019'))
        self.assertIsNotNone(regexUtil.TIME_PATTERN_1.fullmatch('13:30'))
