from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
import pandas

# load common words
commonWords_df = pandas.read_csv('commonWords.csv')

# dictionary for possible leet substitutions with frequency/count {'A': {}, 'B': {},...,'Z': {}}
leetDict = {} 

for asc in range(ord('A'), ord('Z')+1):
    leetDict[chr(asc)] = {}

def getWordFrequencyPercentile(percentile):
    return commonWords_df.quantile(percentile, numeric_only=True).values[0]

def getWordFrequency(word):
    wordFrequency = 0
    if word in commonWords_df['word'].values:
        wordRowIndex = commonWords_df.index[commonWords_df['word']==word].tolist()[0]
        wordFrequency = commonWords_df['count'].loc[commonWords_df.index[wordRowIndex]]
    return wordFrequency
    
def getLeetWordList(inputStr):
    tokenList = word_tokenize(inputStr)
    leetList = []

    for word in tokenList:
        if not word.isalpha() and len(word) > 1:
            leetList.append(word)

    return leetList # returns the list of leetwords in a given text body

def getMatchList(leetWord):
    # get candidates of equal length
    spell = SpellChecker()
    candidateList = spell.candidates(leetWord)
    sameSizeCands = []
    if candidateList is not None:
        for word in candidateList:
            if len(word) == len(leetWord) and getWordFrequency(word) >= getWordFrequencyPercentile(0.70):
                sameSizeCands.append(word)

    return sameSizeCands # e.g: ['hello', 'hella', 'hells'] for hell0


def getPossibleSubstitutions(leetWord):
    candidates = getMatchList(leetWord)
    print(leetWord)
    print(candidates)
    substitutions = {}
    
    for word in candidates:
        charPos = 0        
        for char in leetWord:
            if not char.isalpha():
                subAlpha = word[charPos].upper()
                if subAlpha not in substitutions:
                    substitutions[subAlpha] = {char:1}
                else:
                    if char not in substitutions[subAlpha]:
                        substitutions[subAlpha][char] = 1
                    else:
                        substitutions[subAlpha][char] += 1

            charPos += 1

    return substitutions # e.g: {'A': {'3',1}, 'E': {'3',1}} 

# for a given leet word , add the possible leet substituions to the global leet dictionary
def updateLeetDict(leetWord):
    subs = getPossibleSubstitutions(leetWord)
    for key in subs:
        for leetChar in subs[key]:
            if leetChar in leetDict[key]: # if '3' is in list of 'E'
                leetDict[key][leetChar] += subs[key][leetChar]
            else:
                leetDict[key][leetChar] = subs[key][leetChar]

def processTextInput(): # per row processing: get leetWords, for each leetWord get matches, for each match get context and update leetDict
    return 1


testStr = "H31l0 W0rld  !"

updateLeetDict("4R5e")
print(leetDict)



