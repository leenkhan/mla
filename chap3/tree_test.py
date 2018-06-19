import chap3.trees as tress

dataSet,labels =tress.createDataSet()
print(tress.calcShannonEnt(dataSet))

dataSet[0][-1] = 'maybe'
print(tress.calcShannonEnt(dataSet))