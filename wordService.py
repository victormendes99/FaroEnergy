class word:
    

    def __init__(self, text, idxPhrase):
        self.phrase = []
        self.text = text
        self.phrase.append(idxPhrase)
        self.count = 1

    def setCount(self, count):
        self.count = count + 1

    def setPhraseOccurrence(self, phraseNumber):
        self.phrase.append(phraseNumber)