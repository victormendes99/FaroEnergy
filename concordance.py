import nltk
from wordService import word
from fileService import openArchive
import string

nltk.download('punkt')

phrasesDict = {}
text = openArchive()
phrases = nltk.tokenize.sent_tokenize(text)
table = str.maketrans(dict.fromkeys(string.punctuation))

for idxPhrase, phrase in enumerate(phrases):
    words = phrase.split()
    for wordAux in words:
        wordAux = wordAux.translate(table)
        if wordAux in phrasesDict:
            phrasesDict[wordAux].setCount(phrasesDict[wordAux].count)
            phrasesDict[wordAux].setPhraseOccurrence(idxPhrase + 1)
        else: 
            phrasesDict[wordAux] = word(wordAux, idxPhrase + 1)

#Need to implement loading
print('**-- CONCORDANCIA --*')
for i in sorted(phrasesDict.keys()):
    stringAux = ''
    for j in range (0, len(phrasesDict[i].phrase)):
        stringAux += str(phrasesDict[i].phrase[j]) + ','
    stringAux = stringAux.rstrip(',')
    print(f'{i}: {{{phrasesDict[i].count}: {stringAux}}}' )
print('**-- FINAL DA CONCORDANCIA --*')