import unittest
from util.RegexUtil import RegexUtil

class RegexUtilTest(unittest.TestCase):

    def testRegex(self):
        regexUtil = RegexUtil(synTimeRegexFile='../../resource/syntimeregex/SynTimeRegex.txt')
        self.assertIsNotNone(regexUtil.YEAR_PATTERN_1.search('This is 2019.'))
        self.assertIsNotNone(regexUtil.MONTH_PATTERN.search('Course starts in January.'))
        self.assertIsNotNone(regexUtil.DATE_PATTERN_1.search('27-01-2019.'))
        self.assertIsNotNone(regexUtil.TIME_PATTERN_1.search('Let us meet at 13:30, is it OK?'))
