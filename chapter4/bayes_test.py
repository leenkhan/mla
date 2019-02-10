import chapter4.bayes  as bayes

list0Posting,listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(list0Posting)
print(myVocabList)

wordVec = bayes.setOfWords2Vec(myVocabList, list0Posting[0])
print(wordVec)
wordVec = bayes.setOfWords2Vec(myVocabList, list0Posting[3])
print(wordVec)

trainMat=[]
for postinDoc in list0Posting:
    trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))

p0V,p1V,pAb=bayes.trainNB0(trainMat, listClasses)
print(pAb)
print(p0V)
print(p1V)