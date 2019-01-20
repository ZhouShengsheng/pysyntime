from util.NlpUtil import NlpUtil
from util.RegexUtil import RegexUtil

class SynTime(object):
    """
    SynTime.
    """

    def __init__(self):
        self.nlpUtil = NlpUtil()
        self.regexUtil = RegexUtil()

    def extractTimexFromText(self, text, date):
        """
        Extract timex (time expressions) from text.

        Args:
            text (str): Raw text to extract timex from.
            date (str)
        """
        taggedTokenList = self.nlpUtil.tagging(text)
        self.identifyTimeToken(taggedTokenList)

    def identifyTimeToken(self, taggedTokenList):
        for taggedToken in taggedTokenList:
            token = taggedToken.token
            tag = taggedToken.tag

            tokenTypes = self.regexUtil.getTokenTypes(token, tag)
            taggedToken.tokenTypes = tokenTypes


