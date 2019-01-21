import unittest
from pysyntime.util import NlpUtil


class NlpUtilTest(unittest.TestCase):

    text = 'The last 6 months surviving member of the team which first ' \
           'conquered Everest in 6 a.m. 17 Jan 1953 has died in a Derbyshire nursing home.'
    nlpUtil = NlpUtil()

    def testNlp(self):
        doc = self.nlpUtil.nlp(self.text)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                  token.shape_, token.is_alpha, token.is_stop)
        token = doc[0]
        self.assertEqual(token.text, 'The')
        self.assertEqual(token.lemma_, 'the')
        self.assertEqual(token.tag_, 'DT')

    def testTagging(self):
        taggedTokenList = self.nlpUtil.tagging(self.text)
        for taggedToken in taggedTokenList:
            print(taggedToken)
        taggedToken = taggedTokenList[0]
        self.assertEqual(taggedToken.token, 'The')
        self.assertEqual(taggedToken.lemma, 'the')
        self.assertEqual(taggedToken.tag, 'DT')
        self.assertEqual(taggedToken.tokenPosition, 0)
        self.assertEqual(taggedToken.beginCharPosition, 0)
        self.assertEqual(taggedToken.endCharPosition, 3)
        taggedToken = taggedTokenList[1]
        self.assertEqual(taggedToken.token, 'last')
        self.assertEqual(taggedToken.lemma, 'last')
        self.assertEqual(taggedToken.tag, 'JJ')
        self.assertEqual(taggedToken.tokenPosition, 1)
        self.assertEqual(taggedToken.beginCharPosition, 4)
        self.assertEqual(taggedToken.endCharPosition, 8)
