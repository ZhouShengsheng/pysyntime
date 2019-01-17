import spacy
from model.TaggedToken import TaggedToken

class NlpUtil(object):

    def __init__(self):
        self.nlp = spacy.load('en')

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
