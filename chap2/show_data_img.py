
import matplotlib
import matplotlib.pyplot as plt
import chap2.knn as knn
from  numpy import array

#显示数据散点图
datingDataMat,datingLabels = knn.file2matrix('datingTestSet2.txt')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()