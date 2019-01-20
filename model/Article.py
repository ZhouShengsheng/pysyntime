from model.TaggedToken import TaggedToken

class Article(object):
    """
    An article consists of text and tagged token list.

    Attributes:
        text (str): Raw text of the article.
        taggedTokenList (list): Tagged token list for the text.
    """

    def __init__(self, text, taggedTokenList):
        self.text = text
        self.taggedTokenList = taggedTokenList
