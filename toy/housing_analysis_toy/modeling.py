import numpy as np
import hashlib

class Modeling:
	
	def test_set_check(self, identifier, test_ratio, hashed):
		return hashed(np.int64(identifier)).digest()[-1] < 256 * test_ratio
	
	def split_train_test_by_id(self, data, test_ratio, id_column):
		md5 = hashlib.md5
		ids = data[id_column]
		in_test_set = ids.apply(lambda id_: self.test_set_check(id_, test_ratio, md5))
		print(str(in_test_set))

		return data.loc[~in_test_set], data.loc[in_test_set]

	def split_train_test(self, data, test_ratio):
		shuffled_indices = np.random.permutation(len(data))
		test_set_size = int(len(data) * test_ratio)
		test_indices = shuffled_indices[:test_set_size]
		train_indices = shuffled_indices[test_set_size:]
		
		print(str(shuffled_indices))
		return data.iloc[train_indices], data.iloc[test_indices]

"""	
	def __init__(self, data,test_ratio, id_column):
		train_set, test_set = self.split_train_test_by_id(data, test_ratio, id_column)
		return train_set, test_set
"""
