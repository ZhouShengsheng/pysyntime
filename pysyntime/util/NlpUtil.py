import spacy
from ..model import TaggedToken

class NlpUtil(object):
    """
    NLP util to do POS-tagging for the input text. NLP is powered by spaCy.
    """

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def tagging(self, text):
        if not text:
            return None
        doc = self.nlp(text)
        taggedTokenList = []
        offset = 0
        for token in doc:
            offset = text.find(token.text, offset)
            taggedToken = TaggedToken()
            taggedToken.token = token.text
            taggedToken.lemma = token.lemma_
            taggedToken.tag = token.tag_
            taggedToken.tokenPosition = token.i
            taggedToken.beginCharPosition = offset
            taggedToken.endCharPosition = offset + len(token)
            offset += len(token)
            taggedTokenList.append(taggedToken)

        return taggedTokenList
