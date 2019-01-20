class TimeSegment(object):
    """
    Time segment.

    Attributes:
        timeTokenPosition (int): Time token position in the text.
        beginTokenPosition (int): Begin position in the text.
        endTokenPosition (int): End position in the text.
    """

    def __init__(self, timeTokenPosition, beginTokenPosition, endTokenPosition):
        self.timeTokenPosition = timeTokenPosition
        self.beginTokenPosition = beginTokenPosition
        self.endTokenPosition = endTokenPosition
