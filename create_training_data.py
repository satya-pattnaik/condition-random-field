from pdf_opener import getSentences
from fetch_labels import fetchLabels
from create_labels import setLabels
from feature_extractor import createFeaturesForSentence
import os

pdfPath='./pdfs'
testPdfPath = './testPdfs'
sentences = []

#sentences1 = getSentences('15.pdf')
#sentences2 = getSentences('17.pdf')

labels = fetchLabels()

#getTups = setLabels(sentences1,labels[0]) + setLabels(sentences2,labels[1])
getTups = []
#getTups.append(setLabels())

def getAllSentencesFromAllDocs():
    sentences = []
    for eachFile in os.listdir(pdfPath):
        sentences =sentences+getSentences(pdfPath,eachFile)

    return sentences

def getAllLabelsTups():
    getTups=[]
    for (eachFile,i) in zip(os.listdir(pdfPath),xrange(len(labels))):
        getTups = getTups + setLabels(getSentences(pdfPath,eachFile),labels[i])
    return getTups

def getFeaturesFromSentences(sentence):
    listOfFeatures=[]
    for eachSentence in sentence:
        sentenceToFeatures = createFeaturesForSentence(eachSentence)
        listOfFeatures.append(sentenceToFeatures)

    return listOfFeatures

print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def getLabelsOnly(getTups):
    onlyLabels =[]
    for eachTup in getTups:
        tags = []
        for eachw,eacht in eachTup:
            tags.append(eacht)
        onlyLabels.append(tags)
    return onlyLabels




def getAllTestSentencesFromAllDocs():
    sentences = []
    for eachFile in os.listdir(testPdfPath):
        sentences =sentences+getSentences(testPdfPath,eachFile)

    return sentences

def getTestFeatures():
    testingSentence = getAllTestSentencesFromAllDocs()
    listOfTestFeatures = []
    for eachTestSent in testingSentence:
        testFeatures = createFeaturesForSentence(eachTestSent)
        listOfTestFeatures.append(testFeatures)

    return listOfTestFeatures