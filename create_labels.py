import re
def setLabels(eachDocument,labels):
    listOfWordsLabeled = []



    for eachSentence in eachDocument:
        #wordList = eachSentence.split(' ')
        wordList = re.split(' ',eachSentence)
        eachWordsOfDocument = []
        for word in wordList:
            eachWordsOfDocument.append(word.encode('utf-8'))


        listOfWordsForSentence = []
        for eachWord in eachWordsOfDocument:
            if len(eachWord) != 0:
                #if eachWord in labels:
                if labels.find(eachWord) != -1:
                    partyTup = (eachWord,'PARTY')

                    listOfWordsForSentence.append(partyTup)
                else:
                    nonPartyTup=(eachWord,'O')
                    listOfWordsForSentence.append(nonPartyTup)

        listOfWordsLabeled.append(listOfWordsForSentence)

    return listOfWordsLabeled