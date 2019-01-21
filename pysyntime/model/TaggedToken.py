from ..model import BasicTaggedToken


class TaggedToken(BasicTaggedToken):
    """
    Tagged token with token types.

    Attributes:
        tokenTypeSet (set): Token types for this token.
    """

    def __init__(self, tokenTypeSet=None):
        super().__init__()
        self.tokenTypeSet = tokenTypeSet

    def clearTokenType(self):
        if not self.tokenTypeSet:
            self.tokenTypeSet.clear()
