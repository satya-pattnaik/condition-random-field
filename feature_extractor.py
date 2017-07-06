import re

stopWordString = 'is' + 'on' + 'their' + 'not' + 'or' + ',' + 'in' + 'as' + 'terms'

def ifSentenceHasNiceWords(sentence):
    for word in sentence:
        if word.lower() == 'agreement':
            return 1

    return 0

def ifStartsWithCapital(word):
    if word[0].isupper():
        return 1
    else:
        return 0

def ifWordIsCapital(word):
    for letter in word:
        if letter.islower():
            return 0
    return 1

def ifBetweenIsPlacedProperly(sentence):
    if sentence.find('between')!=-1:
        indexBetween = sentence.find('between')

        wordList = re.split(' ', sentence)
        eachWordsOfSent = []
        for word in wordList:
            eachWordsOfSent.append(word.encode('utf-8'))
        if indexBetween < (len(eachWordsOfSent) - 2 ):
            if (stopWordString.find(eachWordsOfSent[indexBetween + 1]) != 1):
                return False
        if indexBetween < (len(eachWordsOfSent) - 3):
            if stopWordString.find(eachWordsOfSent[indexBetween + 2]) != 1:
                return False
        #SLIGHT CHANGE IS REQUIRED HERE
        return True

    return False



def createFeaturesForSentence(sentence):
    sentenceWithNiceWords = ifSentenceHasNiceWords(sentence)
    betweenProperlyPlaced = ifBetweenIsPlacedProperly(sentence)
    eachWordsOfSentence = []
    setenceToFeatures = []


    wordList =sentence.split(' ')
    #wordList = re.split(' ', sentence)
    for word in wordList:
        if len(word) != 0:
            #eachWordsOfSentence.append(word.encode('utf-8').replace('\n', '').replace(',', ''))
            eachWordsOfSentence.append(word.encode('utf-8'))

    for word in eachWordsOfSentence:
        if len(word) == 0:
            eachWordsOfSentence.remove(word)

    numOfWords = len(eachWordsOfSentence)


    for i in xrange(numOfWords):
        wordIsCapital = ifWordIsCapital(eachWordsOfSentence[i])
        wordStartsWithCapital = ifStartsWithCapital(eachWordsOfSentence[i])

        features = {
            'bias': 1.0,
            'sentenceWithNiceWords':sentenceWithNiceWords,
            'wordIsCapital':wordIsCapital,
            'wordStartsWithCapital':wordStartsWithCapital,
        }

        if i<2:
            features.update(
                {
                    'betweenFoundInProximity':0,
                }
            )
        if i>=2:
            if ((eachWordsOfSentence[i-1].lower()=='between') or (eachWordsOfSentence[i-2].lower()=='between')) and betweenProperlyPlaced:
                features.update(
                    {
                        'betweenFoundInProximity': 1,
                    }
                )
            else:
                features.update(
                    {
                        'betweenFoundInProximity': 0,
                    }
                )


        if i>(numOfWords-2):
            features.update(
                {
                    'a_an_andFoundInProximity': 0,
                }
            )

        if i<=(numOfWords-2):
            if (eachWordsOfSentence[i+1] == 'and') or (eachWordsOfSentence[i+1] == 'a') or (eachWordsOfSentence[i+1]=='an')or (eachWordsOfSentence[i+1]=='for'):
                features.update(
                    {
                        'a_an_andFoundInProximity': 1,
                    }
                )
            else:
                features.update(
                    {
                        'a_an_andFoundInProximity': 0,
                    }
                )

        if i==0:
            features.update(
                {
                    'previousWordIsCapital': 0,
                }
            )
        if i>0:
            prevWordCap = ifStartsWithCapital(eachWordsOfSentence[i-1])
            features.update(
                {
                    'previousWordIsCapital': prevWordCap,
                }
            )

        if i==numOfWords-1:
            features.update(
                {
                    'nextWordIsCapital': 0,
                }
            )

        if i < numOfWords-1:
            nextWordCap = ifStartsWithCapital(eachWordsOfSentence[i+1])
            features.update(
                {
                    'nextWordIsCapital': nextWordCap,
                }
            )


        if i == 0:
            features.update(
                {
                    'previousWordIsThe': 0,
                }
            )
        if i > 0:
            if (eachWordsOfSentence[i - 1]) == 'the':
                features.update(
                    {
                        'previousWordIsThe': 1,
                    }
                )
            else:
                features.update(
                    {
                        'previousWordIsThe': 0,
                    }
                )


        setenceToFeatures.append(features)



    return setenceToFeatures