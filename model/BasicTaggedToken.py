class BasicTaggedToken(object):

    def __init__(self):
        self.token = ""
        self.lemma = ""
        self.tag = ""
        self.tokenPosition = 0
        self.beginCharPosition = 0
        self.endCharPosition = 0

    # def __init__(self, token, lemma, tag, tokenPosition, beginCharPosition, endCharPosition):
    #     self.token = token
    #     self.lemma = lemma
    #     self.tag = tag
    #     self.tokenPosition = tokenPosition
    #     self.beginCharPosition = beginCharPosition
    #     self.endCharPosition = endCharPosition

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.token, self.lemma, self.tag, self.tokenPosition,
                                               self.beginCharPosition, self.endCharPosition)
