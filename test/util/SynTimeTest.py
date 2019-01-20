from unittest import TestCase
from main.SynTime import SynTime

class SynTimeTest(TestCase):

    def testExtractTimexFromText(self):
        text = 'The last 6 months surviving member of the team which first ' \
               'conquered Everest in 6 a.m. 17 Jan 1953 has died in a Derbyshire nursing home.'
        date = '2016-10-10'
        synTime = SynTime()
        synTime.extractTimexFromText(text, date)
