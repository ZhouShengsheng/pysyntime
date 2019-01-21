from syntime.model.TimeSegment import TimeSegment
from syntime.util.NlpUtil import NlpUtil
from syntime.util.RegexUtil import RegexUtil
from syntime.util.TokenTypeUtil import TokenTypeUtil


class SynTime(object):
    """
    SynTime APIs.
    """

    def __init__(self):
        self.nlpUtil = NlpUtil()
        self.regexUtil = RegexUtil()
        self.tokenTypeUtil = TokenTypeUtil(self.regexUtil)

    def extractTimexFromText(self, text, date):
        """
        Extract timex (time expressions) from text.

        Args:
            text (str): Raw text to extract timex from.
            date (str)
        """
        if not text:
            return None
        taggedTokenList = self.nlpUtil.tagging(text)
        timeTokenList = self.identifyTimeToken(taggedTokenList)
        if not timeTokenList or len(timeTokenList) == 0:
            return None
        timeSegmentList = self.identifyTimeSegment(taggedTokenList, timeTokenList)
        if not timeSegmentList or len(timeSegmentList) == 0:
            return None

    def identifyTimeToken(self, taggedTokenList):
        """
        Get time token list from taggedTokenList.

        Args:
            taggedTokenList (list): Tagged token list.

        Returns:
            timeTokenList (list): Time token index list.
        """
        timeTokenList = []
        for i in range(len(taggedTokenList)):
            taggedToken = taggedTokenList[i]
            token = taggedToken.token
            tag = taggedToken.tag

            tokenTypeSet = self.tokenTypeUtil.getTokenTypeSet(token, tag)
            taggedToken.tokenTypeSet = tokenTypeSet

            if TokenTypeUtil.isHalfDayToken(taggedToken):
                if token.lower() == 'am' or token.lower() == 'pm':
                    if i == 0 or (not TokenTypeUtil.isNumeralToken(taggedTokenList[i - 1])
                                  and not TokenTypeUtil.isTimeToken(taggedTokenList[i - 1])):
                        taggedToken.clearTokenType()
            elif TokenTypeUtil.isTimeZoneToken(taggedToken):
                if i == 0 or not TokenTypeUtil.isTimeToken(taggedTokenList[i - 1]) \
                        and not TokenTypeUtil.isHalfDayToken(taggedTokenList[i - 1]) \
                        and not TokenTypeUtil.isNumeralToken(taggedTokenList[i - 1]):
                    taggedToken.clearTokenType()
            elif TokenTypeUtil.isEraToken(taggedToken):
                if i == 0 or not TokenTypeUtil.isNumeralToken(taggedTokenList[i - 1]):
                    taggedToken.clearTokenType()
            elif TokenTypeUtil.isYearToken(taggedToken):
                if i > 0 and (TokenTypeUtil.isInArticleToken(taggedTokenList[i - 1])
                              or taggedTokenList[i - 1].token.lower() == 'the'):
                    taggedTokenList[i - 1].clearTokenType()

            if TokenTypeUtil.isGeneralTimeToken(taggedToken):
                timeTokenList.append(i)

        return timeTokenList

    def identifyTimeSegment(self, taggedTokenList, timeTokenList):
        """
        Get time segment list from taggedTokenList and timeTokenList.

        Args:
            taggedTokenList (list): Tagged token list.
            timeTokenList (list): Time token position list.

        Returns:
            timeSegmentList (list): Time segment list.
        """
        timeSegmentList = []
        firstToken = 0
        lastToken = len(taggedTokenList) - 1
        timeTokenLen = len(timeTokenList)
        for i in range(timeTokenLen):
            timeTokenPosition = timeTokenList[i]

            beginToken = timeTokenPosition
            endToken = timeTokenPosition

            taggedTimeToken = taggedTokenList[timeTokenPosition]
            if TokenTypeUtil.isPeriodToken(taggedTimeToken) or TokenTypeUtil.isDurationToken(taggedTimeToken):
                timeSegmentList.append(TimeSegment(timeTokenPosition, beginToken, endToken))
                continue

            leftBound = firstToken
            rightBound = lastToken
            if i > 0:
                leftBound = timeTokenList[i - 1] + 1
            if i < timeTokenLen - 1:
                rightBound = timeTokenList[i + 1] - 1

            # Search its left side
            findLeftDependentSegment = False
            leftTimeTokenPosition = -1
            leftBeginToken = leftTimeTokenPosition
            leftEndToken = leftTimeTokenPosition
            j = timeTokenPosition - 1
            while j >= leftBound:
                taggedPreMod = taggedTokenList[j]
                if TokenTypeUtil.isPrefixToken(taggedPreMod) or TokenTypeUtil.isNumeralToken(taggedPreMod) \
                        or TokenTypeUtil.isInArticleToken(taggedPreMod):
                    beginToken = j
                elif TokenTypeUtil.isCommaToken(taggedPreMod):
                    beginToken = j
                    break
                elif TokenTypeUtil.isLinkageToken(taggedPreMod):
                    if j-1 >= leftBound and TokenTypeUtil.isGeneralTimeToken(taggedTimeToken) \
                            and TokenTypeUtil.isNumeralToken(taggedTokenList[j-1]):
                        findLeftDependentSegment = True
                        leftTimeTokenPosition = j - 1
                        leftBeginToken = leftTimeTokenPosition
                        leftEndToken = leftTimeTokenPosition
                        k = leftTimeTokenPosition - 1
                        while k >= leftBound:
                            if TokenTypeUtil.isPrefixToken(taggedPreMod) or TokenTypeUtil.isNumeralToken(taggedPreMod) \
                                    or TokenTypeUtil.isInArticleToken(taggedPreMod):
                                leftBeginToken = k
                                k -= 1
                            else:
                                break
                        beginToken = j + 1
                    else:
                        beginToken = j
                    break
                else:
                    break
                j -= 1

            # Search its right side
            findRightDependentSegment = False
            rightTimeTokenPosition = 0
            rightBeginToken = rightTimeTokenPosition
            rightEndToken = rightTimeTokenPosition
            j = timeTokenPosition + 1
            while j <= rightBound:
                taggedSufMod = taggedTokenList[j]
                if TokenTypeUtil.isSuffixToken(taggedSufMod) or TokenTypeUtil.isNumeralToken(taggedSufMod):
                    endToken = j
                elif TokenTypeUtil.isCommaToken(taggedSufMod):
                    endToken = j
                    break
                elif TokenTypeUtil.isLinkageToken(taggedSufMod):
                    if j + 1 <= rightBound and TokenTypeUtil.isGeneralTimeToken(taggedTimeToken) \
                            and TokenTypeUtil.isNumeralToken(taggedTokenList[j+1]):
                        findRightDependentSegment = True
                        rightTimeTokenPosition = j + 1
                        rightBeginToken = rightTimeTokenPosition
                        rightEndToken = rightTimeTokenPosition
                        k = rightTimeTokenPosition + 1
                        while k <= rightBound:
                            if TokenTypeUtil.isSuffixToken(taggedSufMod) or TokenTypeUtil.isNumeralToken(taggedSufMod):
                                rightEndToken = k
                                k += 1
                            else:
                                break
                        endToken = j - 1
                    else:
                        endToken = j
                    break
                else:
                    break
                j += 1

            if findLeftDependentSegment:
                timeSegmentList.append(TimeSegment(leftTimeTokenPosition, leftBeginToken, leftEndToken))
            timeSegmentList.append(TimeSegment(timeTokenPosition, beginToken, endToken))
            if findRightDependentSegment:
                timeSegmentList.append(TimeSegment(rightTimeTokenPosition, rightBeginToken, rightEndToken))

        return timeSegmentList

    def generateTimeMLText(self, text, taggedTokenList, timeSegmentList, date):
        """
        Generate TimeML text for input text.

        Args:
            taggedTokenList (list): Tagged token list.
            timeSegmentList (list): Time segment list.

        Returns:
            timeMLText (str): Text in TimeML format.
        """
