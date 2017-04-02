from sklearn.feature_selection import mutual_info_classif
from sklearn import preprocessing
import csv
import numpy as np
import random
from sklearn.svm import SVC, LinearSVC

class imdataset(object):
	def __init__(self):
		self.PreProcessing_ratio = 0.7
		ds = open('feature_vector.csv')
		rdr = csv.reader(ds)
		self.data = list(rdr)
		self.data = random.sample(self.data, len(self.data))
		self.data = np.array(self.data)
		ds.close()

	def PreProcessing(self):
		cols = np.shape(self.data)[1]
		self.y = self.data[:,cols-1]
		self.y = np.array(self.y)
		self.y = self.y.astype(np.int)
		y = np.ravel(self.y,order='C')
		self.X = self.data[:,:cols-1]
		self.X = self.X.astype(np.float)
		self.X = preprocessing.scale(self.X)
		

	def SelectionTopFeatures(self):
		features = [i.strip() for i in open("feature_vector.csv").readlines()]
		features = np.array(features)
		mi = mutual_info_classif(self.X,self.y)
		print mi
		self.featureind = sorted(range(len(mi)), key=lambda i: mi[i], reverse=True)[:50]
		top25 = features[self.featureind]

	def TrainTest(self):
		PreProcessingRows = int(self.PreProcessing_ratio*len(self.data))
		trainData = self.X[:PreProcessingRows,self.featureind]
		trainLabel = self.y[:PreProcessingRows]
		testData = self.X[PreProcessingRows:,self.featureind]
		testLabel = self.y[PreProcessingRows:]
		return trainData, trainLabel, testData, testLabel		

	def SVM(self):
		svmstruct = SVC()
		trainData, trainLabel, testData, testLabel = self.TrainTest()
		svmstruct.fit(trainData,trainLabel)
		svmaccr = (svmstruct.score(testData,testLabel))*100
		print svmaccr


adr = imdataset()
adr.PreProcessing()
adr.SelectionTopFeatures()
adr.SVM()
