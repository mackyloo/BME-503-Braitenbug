import numpy as np

class HopfieldNetwork():

	def __init__(self,width,height):

		self.width = width

		self.height = height

		self.W = None # init with an empty W

		self.A = None # output

	def trainNetwork(self,X):
		# is is all the patterns wow
		# Train the network

		self.W = np.zeros((self.width * self.height, self.width * self.height))

		# sum outer product then subtract the identity matrix*number of weights? 
		outerprod = 0;
		for m in range(len(X)):
		    outerprod += (np.outer(X[m],(X[m])))
		#Add code here to update the weights   
		self.W = outerprod - len(X)*np.identity(self.height**2)

	def testNetwork(self,A):

		self.A = A

	def updateNetwork(self):

	    self.A=np.sign(np.dot(self.W,self.A))