import sklearn_crfsuite
from create_training_data import getAllSentencesFromAllDocs,getAllLabelsTups,sentences,getTups,getLabelsOnly,getFeaturesFromSentences,getTestFeatures


##########################TRAINING DATA#######
sentencesDocs = getAllSentencesFromAllDocs()

trainSent = getFeaturesFromSentences(sentencesDocs)

trainLabs =  getLabelsOnly(getAllLabelsTups())

##############################################


crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=1000,
    all_possible_transitions=True
)
crf.fit(trainSent, trainLabs)

print ("Trained")

testF = getTestFeatures()

predictLables = crf.predict(testF)

#LABELS PREDICTED
#print predictLables
#REAL LABELS
#print (testTups)