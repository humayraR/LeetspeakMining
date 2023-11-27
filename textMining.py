from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
import pandas as pd
import re

MAX_LEET_WORD_SIZE = 15 # word length
# load common words
commonWords_df = pd.read_csv('commonWords.csv')

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
    regex = ".*[a-zA-Z].*" # regex for string containing at least 1 alphabet, to filter just numbers/special character/emojis tokens
    # tokenList = word_tokenize(inputStr)
    tokenList = inputStr.split(" ")
    leetList = []

    for word in tokenList:
        word = word.strip(".,'?")
        if not word.isalpha() and re.search(".*[a-zA-Z].*", word) and len(word) > 1 and len(word) <= MAX_LEET_WORD_SIZE:
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


def getPossibleSubstitutions(leetWord, candidates):
    # candidates = getMatchList(leetWord)
    # print(leetWord)
    # print(candidates)
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
def updateLeetDict(subs):
    # subs = getPossibleSubstitutions(leetWord)
    for key in subs:
        for leetChar in subs[key]:
            if leetChar in leetDict[key]: # if '3' is in list of 'E'
                leetDict[key][leetChar] += subs[key][leetChar]
            else:
                leetDict[key][leetChar] = subs[key][leetChar]

def processTextInput(textInput): # per row processing: get leetWords, for each leetWord get matches, for each match get context and update leetDict
    leetWordList = getLeetWordList(textInput)
    print("LeetWord List:" + str(leetWordList))
    for lword in leetWordList:
        possibleMatches = getMatchList(lword)
        possibleSubs = getPossibleSubstitutions(lword, possibleMatches)
        updateLeetDict(possibleSubs)
        print("LeetWord: " + lword)
        print("Candidate list: " + str(possibleMatches))
        print("Possible Substitutions and counts: " + str(possibleSubs))


testStr = "He11o W0rld !!"     

# processTextInput(testStr)
# print("Final Leet Dictionary: " + str(leetDict))

# inverseDict ={}
# for key in leetDict.keys():
#     for key2 in leetDict[key].keys():
#         print(key, key2)

# print(leetDict["C"]["1"])

#get the best match using the leet FP list to replace the leetword
def getBestMatch(leetWord):
    matchedWord = list(leetWord)
    #trim the leet word first, get rid of all the unnecessary punctuation 
    candList = getMatchList(leetWord)
    
    charPos = 0
    for char in leetWord:
        subAlphas = []
        subAlphaScores = []
        if not char.isalpha():
            for cand in candList:
                if len(cand) == len(leetWord):
                    subAlphas.append(cand[charPos].upper())
                    subAlphaScores.append(leet_dict[cand[charPos].upper()][char])
            maxConf = max(subAlphaScores)
            index = subAlphaScores.index(maxConf)
            matchedWord[charPos] = subAlphas[index]
        charPos += 1
    
    matchedWord = "".join(matchedWord)

    spell = SpellChecker()
    finalMatch = spell.correction(matchedWord)
    
    return finalMatch

print(getBestMatch("$Helly"))





