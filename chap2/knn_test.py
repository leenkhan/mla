import chap2.knn as knn

dataSet,labels = knn.createData()
print(dataSet)
print(labels)
result = knn.classfiy0([0.1,0.5], dataSet, labels, 2)
print(result)