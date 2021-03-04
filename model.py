import numpy as np

def normalize(arr):
	return arr / sum(arr)

class RPSModel:
	def __init__(self):
		self.unigrams = np.ones((9,3))
		self.bigrams = np.ones((9,9,3))
		self.trigrams = np.ones((9,9,9,3))

		self.history = [None, None, None]
		self.prediction = None

	def predict(self):
		if self.prediction is not None:
			return
		weights = np.array([0,0,0],dtype=float)
		h = self.history

		if h[0] is not None:
			weights += 0.5 * normalize(self.unigrams[h[0]])
		else:
			weights += np.array([1,1,1])

		if h[1] is not None:
			weights += 0.3 * normalize(self.bigrams[h[0]][h[1]])
		else:
			weights += np.array([1,1,1])

		if h[2] is not None:
			weights += 0.2 * normalize(self.trigrams[h[0]][h[1]][h[2]])
		else:
			weights += np.array([1,1,1])
		
		self.prediction = np.random.choice([1,2,0], p=normalize(weights))
		return self.prediction
		
	def update(self,n):
		if self.prediction is None:
			return
		
		h = self.history
		if h[0] is not None:
			self.unigrams[h[0]][n] += 1
		if h[1] is not None:
			self.bigrams[h[0]][h[1]][n] += 1
		if h[2] is not None:
			self.trigrams[h[0]][h[1]][h[2]][n] += 1

		next_gram = 3*n+self.prediction

		self.history[2] = self.history[1]
		self.history[1] = self.history[0]
		self.history[0] = next_gram

		self.prediction = None
