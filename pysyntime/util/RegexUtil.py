import os.path
import re


class RegexUtil(object):
    """
    Util to load and compile regex patterns for SynTime.
    """

    SYN_TIME_REGEX_FILE = os.path.join(os.path.dirname(__file__), '../resource/SynTimeRegex.txt')

    # From StanfordCoreNLP edu.stanford.nlp.ie.regexp.NumberSequenceClassifier.java
    MID_REGEX = None

    # POS: CD; Type: DATE
    YEAR_REGEX_1 = None
    YEAR_PATTERN_1 = None
    YEAR_REGEX_2 = None
    YEAR_PATTERN_2 = None
    YEAR_MID_REGEX = None
    YEAR_MID_PATTERN = None

    YEAR_YEAR_REGEX = None
    YEAR_YEAR_PATTERN = None

    # POS: NNP; Type: DATE
    MONTH_REGEX = None
    MONTH_PATTERN = None
    MONTH_ABBR_REGEX = None
    MONTH_ABBR_PATTERN = None
    MONTH_MID_REGEX = None
    MONTH_MID_PATTERN = None

    MONTH_MONTH_REGEX = None
    MONTH_MONTH_PATTERN = None

    YEAR_MONTH_REGEX_1 = None
    YEAR_MONTH_PATTERN_1 = None
    YEAR_MONTH_REGEX_2 = None
    YEAR_MONTH_PATTERN_2 = None

    # POS: NNP; Type: DATE
    WEEK_REGEX = None
    WEEK_PATTERN = None
    WEEK_ABBR_REGEX = None
    WEEK_ABBR_PATTERN = None

    WEEK_WEEK_REGEX = None
    WEEK_WEEK_PATTERN = None

    # POS: CD
    BASIC_NUMBER_REGEX_1 = None
    BASIC_NUMBER_PATTERN_1 = None
    BASIC_NUMBER_REGEX_2 = None
    BASIC_NUMBER_PATTERN_2 = None

    BASIC_NUMBER_NUMBER_REGEX = None
    BASIC_NUMBER_NUMBER_PATTERN = None

    # POS: CD
    DIGIT_REGEX_1 = None
    DIGIT_PATTERN_1 = None
    DIGIT_REGEX_2 = None
    DIGIT_PATTERN_2 = None

    DIGIT_DIGIT_REGEX = None
    DIGIT_DIGIT_PATTERN = None

    # POS: JJ, CD
    ORDINAL_REGEX_1 = None
    ORDINAL_PATTERN_1 = None
    ORDINAL_REGEX_2 = None
    ORDINAL_PATTERN_2 = None

    ORDINAL_ORDINAL_REGEX = None
    ORDINAL_ORDINAL_PATTERN = None

    INARTICLE_REGEX = None
    INARTICLE_PATTERN = None

    #  Type: DATE
    DATE_REGEX_1 = None
    DATE_PATTERN_1 = None
    DATE_REGEX_2 = None
    DATE_PATTERN_2 = None
    DATE_REGEX_3 = None
    DATE_PATTERN_3 = None

    #  Type: TIME
    TIME_REGEX_1 = None
    TIME_PATTERN_1 = None
    TIME_REGEX_2 = None
    TIME_PATTERN_2 = None
    TIME_TIME_REGEX = None
    TIME_TIME_PATTERN = None

    TIME_ZONE_REGEX = None
    TIME_ZONE_PATTERN = None

    ERA_REGEX = None
    ERA_PATTERN = None
    ERA_YEAR_REGEX = None
    ERA_YEAR_PATTERN = None

    # POS: NN, VBD; Type: TIME
    HALFDAY_REGEX_1 = None
    HALFDAY_PATTERN_1 = None

    HALFDAY_REGEX_2 = None
    HALFDAY_PATTERN_2 = None

    HALFDAY_HALFDAY_REGEX = None
    HALFDAY_HALFDAY_PATTERN = None

    # From english.sutime.txt
    # https://github.com/stanfordnlp/CoreNLP/tree/master/src/edu/stanford/nlp/time/rules
    #
    # POS: NNS; Type: DATE
    DECADE_REGEX = None
    DECADE_PATTERN = None
    DECADE_MID_REGEX = None
    DECADE_MID_PATTERN = None

    # POS: NN, NNS, NNP; Type: DURATION
    TIME_UNIT_REGEX = None
    TIME_UNIT_PATTERN = None

    # POS: NN, JJ; Type: DURATION
    DURATION_REGEX = None
    DURATION_PATTERN = None

    DURATION_DURATION_REGEX_1 = None
    DURATION_DURATION_PATTERN_1 = None
    DURATION_DURATION_REGEX_2 = None
    DURATION_DURATION_PATTERN_2 = None

    # POS: RB, JJ; Type: SET
    PERIOD_REGEX = None
    PERIOD_PATTERN = None

    # POS: NN, NNP, NNS, RB, JJ; Type: TIME
    DAY_TIME_REGEX = None
    DAY_TIME_PATTERN = None
    DAY_TIME_MID_REGEX = None
    DAY_TIME_MID_PATTERN = None

    # POS: NN, NNS; Type: DATE
    SEASON_REGEX = None
    SEASON_PATTERN = None
    SEASON_MID_REGEX = None
    SEASON_MID_PATTERN = None

    # POS: RB, NN; Type: DATE
    TIMELINE_REGEX = None
    TIMELINE_PATTERN = None

    """
    Five kinds of semantic modifiers: relative modifiers, frequency modifiers, early late modifiers, approximate modifiers, and operators.
    Relative modifier: the, next, following, last, previous, this, coming, past
    Frequency modifier: each, every, other, alternate, alternating
    Early late modifier: late, early, mid-?, beginning, start, dawn, middle, end, of, in, on
    Approximate modifier: about, around, some, exactly, precisely
    Operator: this, next, following, previous, last, this, the, coming, following, next, past, previous
    """
    # POS: non-NN*
    PREFIX_REGEX_1 = None
    PREFIX_PATTERN_1 = None
    # POS: NN*
    PREFIX_REGEX_2 = None
    PREFIX_PATTERN_2 = None

    SUFFIX_REGEX = None
    SUFFIX_PATTERN = None

    LINKAGE_REGEX = None
    LINKAGE_PATTERN = None

    COMMA_REGEX = None
    COMMA_PATTERN = None

    # From english.holidays.sutime.txt
    HOLIDAY_REGEX = None
    HOLIDAY_PATTERN = None

    def __init__(self, synTimeRegexFile=SYN_TIME_REGEX_FILE):
        self.__loadSynTimeRegex(synTimeRegexFile)
        self.__inducePattern()

    def __loadSynTimeRegex(self, synTimeRegexFile):
        with open(synTimeRegexFile) as f:
            lines = f.readlines()
        assert lines is not None, 'Failed to load SynTime regex'
        for line in lines:
            line = line.strip()
            if not line:
                continue
            regexName, regex = line.split('\t')
            regexName = regexName[1:-1]
            if regexName == 'MID_REGEX':
                self.MID_REGEX = regex
            elif regexName == 'YEAR_REGEX_1':
                self.YEAR_REGEX_1 = regex
            elif regexName == 'YEAR_REGEX_2':
                self.YEAR_REGEX_2 = regex
            elif regexName == 'MONTH_REGEX':
                self.MONTH_REGEX = regex
            elif regexName == 'MONTH_ABBR_REGEX':
                self.MONTH_ABBR_REGEX = regex
            elif regexName == 'WEEK_REGEX':
                self.WEEK_REGEX = regex
            elif regexName == 'WEEK_ABBR_REGEX':
                self.WEEK_ABBR_REGEX = regex
            elif regexName == 'BASIC_NUMBER_REGEX_1':
                self.BASIC_NUMBER_REGEX_1 = regex
            elif regexName == 'BASIC_NUMBER_REGEX_2':
                self.BASIC_NUMBER_REGEX_2 = regex
            elif regexName == 'DIGIT_REGEX_1':
                self.DIGIT_REGEX_1 = regex
            elif regexName == 'ORDINAL_REGEX_1':
                self.ORDINAL_REGEX_1 = regex
            elif regexName == 'ORDINAL_REGEX_2':
                self.ORDINAL_REGEX_2 = regex
            elif regexName == 'INARTICLE_REGEX':
                self.INARTICLE_REGEX = regex
            elif regexName == 'DATE_REGEX_1':
                self.DATE_REGEX_1 = regex
            elif regexName == 'DATE_REGEX_2':
                self.DATE_REGEX_2 = regex
            elif regexName == 'DATE_REGEX_3':
                self.DATE_REGEX_3 = regex
            elif regexName == 'TIME_REGEX_1':
                self.TIME_REGEX_1 = regex
            elif regexName == 'TIME_REGEX_2':
                self.TIME_REGEX_2 = regex
            elif regexName == 'TIME_ZONE_REGEX':
                self.TIME_ZONE_REGEX = regex
            elif regexName == 'HALFDAY_REGEX_1':
                self.HALFDAY_REGEX_1 = regex
            elif regexName == 'ERA_REGEX':
                self.ERA_REGEX = regex
            elif regexName == 'DECADE_REGEX':
                self.DECADE_REGEX = regex
            elif regexName == 'TIME_UNIT_REGEX':
                self.TIME_UNIT_REGEX = regex
            elif regexName == 'PERIOD_REGEX':
                self.PERIOD_REGEX = regex
            elif regexName == 'DAY_TIME_REGEX':
                self.DAY_TIME_REGEX = regex
            elif regexName == 'SEASON_REGEX':
                self.SEASON_REGEX = regex
            elif regexName == 'TIMELINE_REGEX':
                self.TIMELINE_REGEX = regex
            elif regexName == 'PREFIX_REGEX_1':
                self.PREFIX_REGEX_1 = regex
            elif regexName == 'PREFIX_REGEX_2':
                self.PREFIX_REGEX_2 = regex
            elif regexName == 'SUFFIX_REGEX':
                self.SUFFIX_REGEX = regex
            elif regexName == 'LINKAGE_REGEX':
                self.LINKAGE_REGEX = regex
            elif regexName == 'COMMA_REGEX':
                self.COMMA_REGEX = regex
            elif regexName == 'HOLIDAY_REGEX':
                self.HOLIDAY_REGEX = regex

    def __inducePattern(self):
        # POS: CD; Type: DATE
        self.YEAR_PATTERN_1 = re.compile(self.YEAR_REGEX_1, re.IGNORECASE)
        self.YEAR_PATTERN_2 = re.compile(self.YEAR_REGEX_2, re.IGNORECASE)
        self.YEAR_MID_REGEX = "(" + self.MID_REGEX + ")(" + self.YEAR_REGEX_1 + "|" + self.YEAR_REGEX_2 + ")"
        self.YEAR_MID_PATTERN = re.compile(self.YEAR_MID_REGEX, re.IGNORECASE)

        self.YEAR_YEAR_REGEX = self.YEAR_REGEX_1 + "-(" + self.YEAR_REGEX_1 + "|[0-9]{2})"
        self.YEAR_YEAR_PATTERN = re.compile(self.YEAR_YEAR_REGEX, re.IGNORECASE)

        # POS: NNP; Type: DATE
        self.MONTH_PATTERN = re.compile(self.MONTH_REGEX, re.IGNORECASE)
        self.MONTH_ABBR_PATTERN = re.compile(self.MONTH_ABBR_REGEX, re.IGNORECASE)
        self.MONTH_MID_REGEX = "(" + self.MID_REGEX + ")(" + self.MONTH_REGEX + "|" + self.MONTH_ABBR_REGEX + ")"
        self.MONTH_MID_PATTERN = re.compile(self.MONTH_MID_REGEX, re.IGNORECASE)

        self.MONTH_MONTH_REGEX = "(" + self.MONTH_REGEX + "|" + self.MONTH_ABBR_REGEX + ")-(" + self.MONTH_REGEX + "|" + self.MONTH_ABBR_REGEX + ")"
        self.MONTH_MONTH_PATTERN = re.compile(self.MONTH_MONTH_REGEX, re.IGNORECASE)

        self.YEAR_MONTH_REGEX_1 = self.YEAR_REGEX_1 + "-(" + self.MONTH_REGEX + "|" + self.MONTH_ABBR_REGEX + ")"
        self.YEAR_MONTH_PATTERN_1 = re.compile(self.YEAR_MONTH_REGEX_1, re.IGNORECASE)
        self.YEAR_MONTH_REGEX_2 = "(" + self.MONTH_REGEX + "|" + self.MONTH_ABBR_REGEX + ")-" + self.YEAR_REGEX_1
        self.YEAR_MONTH_PATTERN_2 = re.compile(self.YEAR_MONTH_REGEX_2, re.IGNORECASE)

        # POS: NNP; Type: DATE
        self.WEEK_PATTERN = re.compile(self.WEEK_REGEX, re.IGNORECASE)
        self.WEEK_ABBR_PATTERN = re.compile(self.WEEK_ABBR_REGEX, re.IGNORECASE)

        self.WEEK_WEEK_REGEX = "(" + self.WEEK_REGEX + "|" + self.WEEK_ABBR_REGEX + ")-(" + self.WEEK_REGEX + "|" + self.WEEK_ABBR_REGEX + ")"
        self.WEEK_WEEK_PATTERN = re.compile(self.WEEK_WEEK_REGEX, re.IGNORECASE)

        # POS: CD
        self.BASIC_NUMBER_PATTERN_1 = re.compile(self.BASIC_NUMBER_REGEX_1, re.IGNORECASE)
        self.BASIC_NUMBER_PATTERN_2 = re.compile(self.BASIC_NUMBER_REGEX_2, re.IGNORECASE)

        self.BASIC_NUMBER_NUMBER_REGEX = "(" + self.BASIC_NUMBER_REGEX_1 + ")-(" + self.BASIC_NUMBER_REGEX_1 + ")"
        self.BASIC_NUMBER_NUMBER_PATTERN = re.compile(self.BASIC_NUMBER_NUMBER_REGEX, re.IGNORECASE)

        # POS: CD
        self.DIGIT_PATTERN_1 = re.compile(self.DIGIT_REGEX_1, re.IGNORECASE)
        self.DIGIT_REGEX_2 = self.DIGIT_REGEX_1 + "[/\\.]" + self.DIGIT_REGEX_1
        self.DIGIT_PATTERN_2 = re.compile(self.DIGIT_REGEX_2, re.IGNORECASE)

        self.DIGIT_DIGIT_REGEX = self.DIGIT_REGEX_1 + "-" + self.DIGIT_REGEX_1
        self.DIGIT_DIGIT_PATTERN = re.compile(self.DIGIT_DIGIT_REGEX)

        # POS: JJ, CD
        self.ORDINAL_PATTERN_1 = re.compile(self.ORDINAL_REGEX_1, re.IGNORECASE)
        self.ORDINAL_PATTERN_2 = re.compile(self.ORDINAL_REGEX_2, re.IGNORECASE)

        self.ORDINAL_ORDINAL_REGEX = "(" + self.ORDINAL_REGEX_1 + ")-(" + self.ORDINAL_REGEX_1 + ")"
        self.ORDINAL_ORDINAL_PATTERN = re.compile(self.ORDINAL_ORDINAL_REGEX, re.IGNORECASE)

        self.INARTICLE_PATTERN = re.compile(self.INARTICLE_REGEX, re.IGNORECASE)

        #  Type: DATE
        self.DATE_PATTERN_1 = re.compile(self.DATE_REGEX_1)
        self.DATE_PATTERN_2 = re.compile(self.DATE_REGEX_2)
        self.DATE_PATTERN_3 = re.compile(self.DATE_REGEX_3, re.IGNORECASE)

        #  Type: TIME
        self.TIME_PATTERN_1 = re.compile(self.TIME_REGEX_1)
        self.TIME_PATTERN_2 = re.compile(self.TIME_REGEX_2)
        self.TIME_TIME_REGEX = "(" + self.TIME_REGEX_1 + "|" + self.TIME_REGEX_2 + ")-(" + self.TIME_REGEX_1 + "|" + self.TIME_REGEX_2 + ")"
        self.TIME_TIME_PATTERN = re.compile(self.TIME_TIME_REGEX)

        self.TIME_ZONE_PATTERN = re.compile(self.TIME_ZONE_REGEX, re.IGNORECASE)

        self.ERA_PATTERN = re.compile(self.ERA_REGEX, re.IGNORECASE)
        self.ERA_YEAR_REGEX = self.DIGIT_REGEX_1 + "(" + self.ERA_REGEX + ")"
        self.ERA_YEAR_PATTERN = re.compile(self.ERA_YEAR_REGEX, re.IGNORECASE)

        # POS: NN, VBD; Type: TIME
        self.HALFDAY_PATTERN_1 = re.compile(self.HALFDAY_REGEX_1, re.IGNORECASE)

        self.HALFDAY_REGEX_2 = "(" + self.DIGIT_REGEX_1 + "|" + self.DIGIT_REGEX_2 + "|" + self.TIME_REGEX_1 + "|" + self.TIME_REGEX_2 + ")(" + self.HALFDAY_REGEX_1 + ")"
        self.HALFDAY_PATTERN_2 = re.compile(self.HALFDAY_REGEX_2, re.IGNORECASE)

        self.HALFDAY_HALFDAY_REGEX = self.HALFDAY_REGEX_2 + "-" + self.HALFDAY_REGEX_2
        self.HALFDAY_HALFDAY_PATTERN = re.compile(self.HALFDAY_HALFDAY_REGEX, re.IGNORECASE)

        # From english.sutime.txt
        # POS: NNS; Type: DATE
        self.DECADE_PATTERN = re.compile(self.DECADE_REGEX, re.IGNORECASE)
        self.DECADE_MID_REGEX = "(" + self.MID_REGEX + ")(" + self.DECADE_REGEX + ")"
        self.DECADE_MID_PATTERN = re.compile(self.DECADE_MID_REGEX, re.IGNORECASE)

        # POS: NN, NNS, NNP; Type: DURATION
        self.TIME_UNIT_PATTERN = re.compile(self.TIME_UNIT_REGEX, re.IGNORECASE)

        # POS: NN, JJ; Type: DURATION
        self.DURATION_REGEX = "(" + self.DIGIT_REGEX_1 + "|" + self.DIGIT_REGEX_2 + "|" + self.BASIC_NUMBER_REGEX_1 + "|" + self.BASIC_NUMBER_REGEX_2 + "|" + self.ORDINAL_REGEX_1 + "|" + self.ORDINAL_REGEX_2 + "|" + self.INARTICLE_REGEX + ")-?(" + self.TIME_UNIT_REGEX + ")"
        self.DURATION_PATTERN = re.compile(self.DURATION_REGEX, re.IGNORECASE)

        self.DURATION_DURATION_REGEX_1 = "(" + self.DIGIT_DIGIT_REGEX + "|" + self.BASIC_NUMBER_NUMBER_REGEX + "|" + self.ORDINAL_ORDINAL_REGEX + ")-?(" + self.TIME_UNIT_REGEX + ")"
        self.DURATION_DURATION_PATTERN_1 = re.compile(self.DURATION_DURATION_REGEX_1, re.IGNORECASE)
        self.DURATION_DURATION_REGEX_2 = self.DURATION_REGEX + "-" + self.DURATION_REGEX
        self.DURATION_DURATION_PATTERN_2 = re.compile(self.DURATION_DURATION_REGEX_2, re.IGNORECASE)

        # POS: RB, JJ; Type: SET
        self.PERIOD_PATTERN = re.compile(self.PERIOD_REGEX, re.IGNORECASE)

        # POS: NN, NNP, NNS, RB, JJ; Type: TIME
        self.DAY_TIME_PATTERN = re.compile(self.DAY_TIME_REGEX, re.IGNORECASE)
        self.DAY_TIME_MID_REGEX = "(" + self.MID_REGEX + ")(" + self.DAY_TIME_REGEX + ")"
        self.DAY_TIME_MID_PATTERN = re.compile(self.DAY_TIME_MID_REGEX, re.IGNORECASE)

        # POS: NN, NNS; Type: DATE
        self.SEASON_PATTERN = re.compile(self.SEASON_REGEX, re.IGNORECASE)
        self.SEASON_MID_REGEX = "(" + self.MID_REGEX + ")(" + self.SEASON_REGEX + ")"
        self.SEASON_MID_PATTERN = re.compile(self.SEASON_MID_REGEX, re.IGNORECASE)

        # POS: RB, NN; Type: DATE
        self.TIMELINE_PATTERN = re.compile(self.TIMELINE_REGEX, re.IGNORECASE)

        # Modifiers
        # POS: non-NN*
        self.PREFIX_PATTERN_1 = re.compile(self.PREFIX_REGEX_1, re.IGNORECASE)
        # POS: NN*
        self.PREFIX_PATTERN_2 = re.compile(self.PREFIX_REGEX_2, re.IGNORECASE)

        self.SUFFIX_PATTERN = re.compile(self.SUFFIX_REGEX, re.IGNORECASE)

        self.LINKAGE_PATTERN = re.compile(self.LINKAGE_REGEX, re.IGNORECASE)

        self.COMMA_PATTERN = re.compile(self.COMMA_REGEX)

        # From english.holidays.sutime.txt
        self.HOLIDAY_PATTERN = re.compile(self.HOLIDAY_REGEX, re.IGNORECASE)
