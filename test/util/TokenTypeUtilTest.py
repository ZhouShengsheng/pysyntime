import unittest
from syntime.util.NlpUtil import NlpUtil
from syntime.util.RegexUtil import RegexUtil
from syntime.util.TokenTypeUtil import TokenTypeUtil
from syntime.model.TokenType import TokenType

class TokenTypeUtilTest(unittest.TestCase):

    def testGetTokenTypeSet(self):
        nlpUtil = NlpUtil()
        regexUtil = RegexUtil()
        tokenTypeUtil = TokenTypeUtil(regexUtil)

        text = 'The last 6 months surviving member of the team which first ' \
               'conquered Everest in 6 a.m. 17 Jan 1953 has died in a Derbyshire nursing home.'
        taggedTokenList = nlpUtil.tagging(text)

        # 6
        tokenTypeSet = tokenTypeUtil.getTokenTypeSet(taggedTokenList[2].token, 'CD')
        self.assertTrue(tokenTypeSet and len(tokenTypeSet) == 1)
        tokenType = list(tokenTypeSet)[0]
        self.assertEqual(tokenType, TokenType.NUMERAL)

        # months
        tokenTypeSet = tokenTypeUtil.getTokenTypeSet(taggedTokenList[3].token, 'NNP')
        self.assertTrue(tokenTypeSet and len(tokenTypeSet) == 1)
        tokenType = list(tokenTypeSet)[0]
        self.assertEqual(tokenType, TokenType.TIME_UNIT)
