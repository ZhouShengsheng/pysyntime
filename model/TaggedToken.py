from model.BasicTaggedToken import BasicTaggedToken


class TaggedToken(BasicTaggedToken):
    """
    Tagged token with token types.

    Attributes:
        tokenTypes (set): Token types for this token.
    """

    tokenTypes = None
