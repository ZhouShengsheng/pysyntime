from unittest import TestCase
from pysyntime import SynTime

class SynTimeTest(TestCase):

    def testExtractTimexFromText(self):
        synTime = SynTime()

        text = 'The last 6 months surviving member of the team which first conquered Everest in 6 a.m. 17 Jan 1953 has died in a Derbyshire nursing home.'
        date = '2016-10-10'
        timeMLText = synTime.extractTimexFromText(text, date)
        print(timeMLText)
        self.assertEqual(timeMLText, '<TIMEX3 tid="t1" type="DATE" value="2016-10-10">The last 6 months</TIMEX3> surviving member of the team which first conquered Everest in <TIMEX3 tid="t2" type="DATE" value="2016-10-10">6 a.m. 17 Jan 1953</TIMEX3> has died in a Derbyshire nursing home.')

        text = 'Poetsch referred to the tougher-than-expected targets to cut greenhouse emissions from cars by 37.5 percent by 2030, which the European Union agreed in December.'
        timeMLText = synTime.extractTimexFromText(text, date)
        print(timeMLText)
        self.assertEqual(timeMLText, 'Poetsch referred to the tougher-than-expected targets to cut greenhouse emissions from cars by 37.5 percent by <TIMEX3 tid="t1" type="DATE" value="2016-10-10">2030,</TIMEX3> which the European Union agreed in <TIMEX3 tid="t2" type="DATE" value="2016-10-10">December</TIMEX3>.')
