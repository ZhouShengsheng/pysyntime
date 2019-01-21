from ..model import TokenType
from ..model import TaggedToken


class TokenTypeUtil(object):

    def __init__(self, regexUtil):
        self.regexUtil = regexUtil

    def getTokenTypeSet(self, token, posTag):
        """
        Get token type set for specific token with specific pos-tag.

        Args:
            token (str)
            posTag (str)
        """
        tokenTypeSet = set()
        isPosTagNN = posTag.startswith('NN')
        isPosTagJJ = posTag == 'JJ'
        isPosTagCD = posTag == 'CD'
        isPosTagRB = posTag == 'RB'

        if self.regexUtil.YEAR_PATTERN_1.fullmatch(token) or self.regexUtil.YEAR_PATTERN_2.fullmatch(token) \
                or self.regexUtil.YEAR_MID_PATTERN.fullmatch(token) or self.regexUtil.ERA_YEAR_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.YEAR)

        mYearYear = self.regexUtil.YEAR_YEAR_PATTERN.fullmatch(token)
        if mYearYear:
            tokenTypeSet.add(TokenType.YEAR_YEAR)

        if isPosTagNN and self.regexUtil.SEASON_PATTERN.fullmatch(token) \
                or self.regexUtil.SEASON_MID_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.SEASON)

        if isPosTagNN and self.regexUtil.MONTH_PATTERN.fullmatch(token) \
                or self.regexUtil.MONTH_MID_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.MONTH)
        if isPosTagNN and self.regexUtil.MONTH_ABBR_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.MONTH_ABBR)
        if self.regexUtil.MONTH_MONTH_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.MONTH_MONTH)

        if self.regexUtil.YEAR_MONTH_PATTERN_1.fullmatch(token) or self.regexUtil.YEAR_MONTH_PATTERN_2.fullmatch(token):
            tokenTypeSet.add(TokenType.YEAR_MONTH)

        if isPosTagNN and self.regexUtil.WEEK_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.WEEK)

        if isPosTagNN and self.regexUtil.WEEK_ABBR_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.WEEK_ABBR)

        if self.regexUtil.WEEK_WEEK_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.WEEK_WEEK)

        if self.regexUtil.DATE_PATTERN_1.fullmatch(token) or self.regexUtil.DATE_PATTERN_2.fullmatch(token) \
                or self.regexUtil.DATE_PATTERN_3.fullmatch(token):
            tokenTypeSet.add(TokenType.DATE)

        if self.regexUtil.TIME_PATTERN_1.fullmatch(token) or self.regexUtil.TIME_PATTERN_2.fullmatch(token):
            tokenTypeSet.add(TokenType.TIME)
        if self.regexUtil.TIME_TIME_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.TIME_TIME)

        if self.regexUtil.HALFDAY_PATTERN_1.fullmatch(token) or self.regexUtil.HALFDAY_PATTERN_2.fullmatch(token):
            tokenTypeSet.add(TokenType.HALFDAY)
        if self.regexUtil.HALFDAY_HALFDAY_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.HALFDAY_HALFDAY)

        if self.regexUtil.TIME_ZONE_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.TIME_ZONE)

        if isPosTagNN and self.regexUtil.ERA_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.ERA)

        if isPosTagNN and self.regexUtil.TIME_UNIT_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.TIME_UNIT)

        mDuration = self.regexUtil.DURATION_PATTERN.fullmatch(token)
        if (isPosTagNN or isPosTagJJ or isPosTagCD) and mDuration:
            tokenTypeSet.add(TokenType.DURATION)

        if not mDuration and (
                self.regexUtil.DURATION_DURATION_PATTERN_1.fullmatch(token)
                or self.regexUtil.DURATION_DURATION_PATTERN_2.fullmatch(token)):
            tokenTypeSet.add(TokenType.DURATION_DURATION)

        if (isPosTagNN or isPosTagRB or isPosTagJJ or self.regexUtil.DAY_TIME_MID_PATTERN.fullmatch(token)) and \
                self.regexUtil.DAY_TIME_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.DAY_TIME)

        if (isPosTagNN or isPosTagRB) and self.regexUtil.TIMELINE_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.TIMELINE)

        if self.regexUtil.HOLIDAY_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.HOLIDAY)

        if (isPosTagNN or isPosTagRB or isPosTagJJ) and self.regexUtil.PERIOD_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.PERIOD)

        if isPosTagNN and self.regexUtil.DECADE_PATTERN.fullmatch(token) or self.regexUtil.DECADE_MID_PATTERN.fullmatch(
                token):
            tokenTypeSet.add(TokenType.DECADE)

        mBasicNum2 = self.regexUtil.BASIC_NUMBER_PATTERN_2.fullmatch(token)
        if ((isPosTagJJ or isPosTagCD or isPosTagRB) and (self.regexUtil.ORDINAL_PATTERN_1.fullmatch(token)
                                                          or self.regexUtil.ORDINAL_PATTERN_2.fullmatch(token))) \
                or self.regexUtil.DIGIT_PATTERN_1.fullmatch(token) \
                or self.regexUtil.DIGIT_PATTERN_2.fullmatch(token) \
                or self.regexUtil.BASIC_NUMBER_PATTERN_1.fullmatch(token) \
                or mBasicNum2:
            tokenTypeSet.add(TokenType.NUMERAL)

        if not mYearYear and not mBasicNum2 and (
                self.regexUtil.DIGIT_DIGIT_PATTERN.fullmatch(
                    token) or self.regexUtil.BASIC_NUMBER_NUMBER_PATTERN.fullmatch(token)
                or self.regexUtil.ORDINAL_ORDINAL_PATTERN.fullmatch(token)):
            tokenTypeSet.add(TokenType.NUMERAL_NUMERAL)

        if self.regexUtil.INARTICLE_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.INARTICLE)

        if len(tokenTypeSet) == 0 and (not isPosTagNN and self.regexUtil.PREFIX_PATTERN_1.fullmatch(token) or
                                     isPosTagNN and self.regexUtil.PREFIX_PATTERN_2.fullmatch(token)):
            tokenTypeSet.add(TokenType.PREFIX)

        if self.regexUtil.SUFFIX_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.SUFFIX)

        if self.regexUtil.LINKAGE_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.LINKAGE)

        if self.regexUtil.COMMA_PATTERN.fullmatch(token):
            tokenTypeSet.add(TokenType.COMMA)

        return tokenTypeSet

    @classmethod
    def hasType(cls, tokenTypeSet, targetTypeFunc):
        """
        Check if tokenTypeSet contains a target type.
        Args:
            tokenTypeSet (set): Token type set.
            targetTypeFunc (function): Function to determine if the tokenTypeSet contain a target type.
        """
        for tokenType in tokenTypeSet:
            if targetTypeFunc(tokenType):
                return True
        return False

    @classmethod
    def isYear(cls, tokenType):
        """
        Check if the token type is year.
        Args:
            tokenType (TaggedToken): Token type.
        """
        return tokenType == TokenType.YEAR or tokenType == TokenType.YEAR_YEAR

    @classmethod
    def hasYear(cls, tokenTypeSet):
        """
        Check if one of the token types is year.
        Args:
            tokenTypeSet (set): Token type set.
        """
        return cls.hasType(tokenTypeSet, cls.isYear)

    @classmethod
    def isYearToken(cls, taggedToken):
        """
        Check if taggedToken has year token type in its tokenTypeSet.
        Args:
            taggedToken (TaggedToken): Tagged token.
        """
        return cls.hasYear(taggedToken.tokenTypeSet)

    @classmethod
    def isYearYear(cls, tokenType):
        return tokenType == TokenType.YEAR_YEAR

    @classmethod
    def hasYearYear(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isYearYear)

    @classmethod
    def isYearYearToken(cls, taggedToken):
        return cls.hasYearYear(taggedToken.tokenTypeSet)

    @classmethod
    def isSeason(cls, tokenType):
        return tokenType == TokenType.SEASON

    @classmethod
    def hasSeason(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isSeason)

    @classmethod
    def isSeasonToken(cls, taggedToken):
        return cls.hasSeason(taggedToken.tokenTypeSet)

    @classmethod
    def isMonth(cls, tokenType):
        return tokenType == TokenType.MONTH or tokenType == TokenType.MONTH_ABBR \
               or tokenType == TokenType.MONTH_MONTH or tokenType == TokenType.YEAR_MONTH

    @classmethod
    def hasMonth(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isMonth)

    @classmethod
    def isMonthToken(cls, taggedToken):
        return cls.hasMonth(taggedToken.tokenTypeSet)

    @classmethod
    def isMonthMonth(cls, tokenType):
        return tokenType == TokenType.MONTH_MONTH

    @classmethod
    def hasMonthMonth(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isMonthMonth)

    @classmethod
    def isMonthMonthToken(cls, taggedToken):
        return cls.hasMonthMonth(taggedToken.tokenTypeSet)

    @classmethod
    def isYearMonth(cls, tokenType):
        return tokenType == TokenType.YEAR_MONTH

    @classmethod
    def hasYearMonth(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isYearMonth)

    @classmethod
    def isYearMonthToken(cls, taggedToken):
        return cls.hasYearMonth(taggedToken.tokenTypeSet)

    @classmethod
    def isWeek(cls, tokenType):
        return tokenType == TokenType.WEEK or tokenType == TokenType.WEEK_ABBR or tokenType == TokenType.WEEK_WEEK

    @classmethod
    def hasWeek(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isWeek)

    @classmethod
    def isWeekToken(cls, taggedToken):
        return cls.hasWeek(taggedToken.tokenTypeSet)

    @classmethod
    def isWeekWeek(cls, tokenType):
        return tokenType == TokenType.WEEK_WEEK

    @classmethod
    def hasWeekWeek(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isWeekWeek)

    @classmethod
    def isWeekWeekToken(cls, taggedToken):
        return cls.hasWeekWeek(taggedToken.tokenTypeSet)

    @classmethod
    def isDate(cls, tokenType):
        return tokenType == TokenType.DATE

    @classmethod
    def hasDate(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isDate)

    @classmethod
    def isDateToken(cls, taggedToken):
        return cls.hasDate(taggedToken.tokenTypeSet)

    @classmethod
    def isTime(cls, tokenType):
        return tokenType == TokenType.TIME or tokenType == TokenType.TIME_TIME

    @classmethod
    def hasTime(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isTime)

    @classmethod
    def isTimeToken(cls, taggedToken):
        return cls.hasTime(taggedToken.tokenTypeSet)

    @classmethod
    def isTimeTime(cls, tokenType):
        return tokenType == TokenType.TIME_TIME

    @classmethod
    def hasTimeTime(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isTimeTime)

    @classmethod
    def isTimeTimeToken(cls, taggedToken):
        return cls.hasTimeTime(taggedToken.tokenTypeSet)

    @classmethod
    def isHalfDay(cls, tokenType):
        return tokenType == TokenType.HALFDAY or tokenType == TokenType.HALFDAY_HALFDAY

    @classmethod
    def hasHalfDay(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isHalfDay)

    @classmethod
    def isHalfDayToken(cls, taggedToken):
        return cls.hasHalfDay(taggedToken.tokenTypeSet)

    @classmethod
    def isHalfDayHalfDay(cls, tokenType):
        return tokenType == TokenType.HALFDAY_HALFDAY

    @classmethod
    def hasHalfDayHalfDay(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isHalfDayHalfDay)

    @classmethod
    def isHalfDayHalfDayToken(cls, taggedToken):
        return cls.hasHalfDayHalfDay(taggedToken.tokenTypeSet)

    @classmethod
    def isTimeZone(cls, tokenType):
        return tokenType == TokenType.TIME_ZONE

    @classmethod
    def hasTimeZone(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isTimeZone)

    @classmethod
    def isTimeZoneToken(cls, taggedToken):
        return cls.hasTimeZone(taggedToken.tokenTypeSet)

    @classmethod
    def isEra(cls, tokenType):
        return tokenType == TokenType.ERA

    @classmethod
    def hasEra(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isEra)

    @classmethod
    def isEraToken(cls, taggedToken):
        return cls.hasEra(taggedToken.tokenTypeSet)

    @classmethod
    def isTimeUnit(cls, tokenType):
        return tokenType == TokenType.TIME_UNIT

    @classmethod
    def hasTimeUnit(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isTimeUnit)

    @classmethod
    def isTimeUnitToken(cls, taggedToken):
        return cls.hasTimeUnit(taggedToken.tokenTypeSet)

    @classmethod
    def isDuration(cls, tokenType):
        return tokenType == TokenType.DURATION

    @classmethod
    def hasDuration(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isDuration)

    @classmethod
    def isDurationToken(cls, taggedToken):
        return cls.hasDuration(taggedToken.tokenTypeSet)

    @classmethod
    def isDurationDuration(cls, tokenType):
        return tokenType == TokenType.DURATION_DURATION

    @classmethod
    def hasDurationDuration(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isDurationDuration)

    @classmethod
    def isDurationDurationToken(cls, taggedToken):
        return cls.hasDurationDuration(taggedToken.tokenTypeSet)

    @classmethod
    def isDayTime(cls, tokenType):
        return tokenType == TokenType.DAY_TIME

    @classmethod
    def hasDayTime(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isDayTime)

    @classmethod
    def isDayTimeToken(cls, taggedToken):
        return cls.hasDayTime(taggedToken.tokenTypeSet)

    @classmethod
    def isTimeLine(cls, tokenType):
        return tokenType == TokenType.TIMELINE

    @classmethod
    def hasTimeLine(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isTimeLine)

    @classmethod
    def isTimeLineToken(cls, taggedToken):
        return cls.hasTimeLine(taggedToken.tokenTypeSet)

    @classmethod
    def isHoliday(cls, tokenType):
        return tokenType == TokenType.HOLIDAY

    @classmethod
    def hasHoliday(cls, tokenType):
        return cls.hasType(tokenType, cls.isHoliday)

    @classmethod
    def isHolidayToken(cls, taggedToken):
        return cls.hasHoliday(taggedToken.tokenTypeSet)

    @classmethod
    def isPeriod(cls, tokenType):
        return tokenType == TokenType.PERIOD

    @classmethod
    def hasPeriod(cls, tokenType):
        return cls.hasType(tokenType, cls.isPeriod)

    @classmethod
    def isPeriodToken(cls, taggedToken):
        return cls.hasPeriod(taggedToken.tokenTypeSet)

    @classmethod
    def isDecade(cls, tokenType):
        return tokenType == TokenType.DECADE

    @classmethod
    def hasDecade(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isDecade)

    @classmethod
    def isDecadeToken(cls, taggedToken):
        return cls.hasDecade(taggedToken.tokenTypeSet)

    @classmethod
    def isNumeral(cls, tokenType):
        return tokenType == TokenType.NUMERAL or tokenType == TokenType.NUMERAL_NUMERAL

    @classmethod
    def hasNumeral(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isNumeral)

    @classmethod
    def isNumeralToken(cls, taggedToken):
        return cls.hasNumeral(taggedToken.tokenTypeSet)

    @classmethod
    def isNumeralNumeral(cls, tokenType):
        return tokenType == TokenType.NUMERAL_NUMERAL

    @classmethod
    def hasNumeralNumeral(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isNumeralNumeral)

    @classmethod
    def isNumeralNumeralToken(cls, taggedToken):
        return cls.hasNumeralNumeral(taggedToken.tokenTypeSet)

    @classmethod
    def isInArticle(cls, tokenType):
        return tokenType == TokenType.INARTICLE

    @classmethod
    def hasInArticle(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isInArticle)

    @classmethod
    def isInArticleToken(cls, taggedToken):
        return cls.hasInArticle(taggedToken.tokenTypeSet)

    @classmethod
    def isPrefix(cls, tokenType):
        return tokenType == TokenType.PREFIX

    @classmethod
    def hasPrefix(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isPrefix)

    @classmethod
    def isPrefixToken(cls, taggedToken):
        return cls.hasPrefix(taggedToken.tokenTypeSet)

    @classmethod
    def isSuffix(cls, tokenType):
        return tokenType == TokenType.SUFFIX

    @classmethod
    def hasSuffix(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isSuffix)

    @classmethod
    def isSuffixToken(cls, taggedToken):
        return cls.hasSuffix(taggedToken.tokenTypeSet)

    @classmethod
    def isLinkage(cls, tokenType):
        return tokenType == TokenType.LINKAGE

    @classmethod
    def hasLinkage(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isLinkage)

    @classmethod
    def isLinkageToken(cls, taggedToken):
        return cls.hasLinkage(taggedToken.tokenTypeSet)

    @classmethod
    def isComma(cls, tokenType):
        return tokenType == TokenType.COMMA

    @classmethod
    def hasComma(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isComma)

    @classmethod
    def isCommaToken(cls, taggedToken):
        return cls.hasComma(taggedToken.tokenTypeSet)

    @classmethod
    def isGeneralTime(cls, tokenType):
        return cls.isYear(tokenType) or cls.isSeason(tokenType) or cls.isMonth(tokenType) or cls.isWeek(
            tokenType) or cls.isDate(
            tokenType) or cls.isTime(tokenType) or cls.isHalfDay(tokenType) \
               or cls.isTimeZone(tokenType) or cls.isEra(tokenType) or cls.isTimeUnit(tokenType) or cls.isDuration(
            tokenType) or cls.isDayTime(tokenType) or cls.isTimeLine(tokenType) \
               or cls.isHoliday(tokenType) or cls.isPeriod(tokenType) or cls.isDecade(tokenType)

    @classmethod
    def hasGeneralTime(cls, tokenTypeSet):
        return cls.hasType(tokenTypeSet, cls.isGeneralTime)

    @classmethod
    def isGeneralTimeToken(cls, taggedToken):
        return cls.hasGeneralTime(taggedToken.tokenTypeSet)

    @classmethod
    def isSameTokenType(cls, taggedToken1, taggedToken2):
        tokenTypeSet1 = taggedToken1.tokenTypeSet
        tokenTypeSet2 = taggedToken2.tokenTypeSet
        if not tokenTypeSet1 or not tokenTypeSet2 or len(tokenTypeSet1) != len(tokenTypeSet2):
            return False
        for tokenType1 in tokenTypeSet1:
            for tokenType2 in tokenTypeSet2:
                if tokenType1 == tokenType2:
                    return True
        return False
