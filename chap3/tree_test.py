import chap3.trees as trees

dataSet,labels =trees.createDataSet()
print(trees.calcShannonEnt(dataSet))

dataSet[0][-1] = 'maybe'
print(trees.calcShannonEnt(dataSet))

myDat,labels = trees.createDataSet()
res1 = trees.splitDataSet(myDat,0,1)
print(res1)

res1 = trees.splitDataSet(myDat,0,0)
print(res1)

print(trees.chooseBestFeatureToSplit(myDat))

print("tree: ",trees.createTree(myDat,labels))