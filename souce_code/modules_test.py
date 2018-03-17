from download_data import DOWNDATA
from read_csv import READCSV
from uncompress import UNCOMP
import modeling
#logic betch and pattern view
import matplotlib.pyplot as plot
import numpy as np
from sklearn.model_selection import train_test_split

def scenario_betch(read_csv):
	read_csv.hist(bins=50, figsize=(20,15))
	plot.title("hausing test")
	plot.savefig("./housing_test.png")
	#plot.show()
	return

if __name__ == "__main__":
	
	download_tag = DOWNDATA.download_tag("datasets/housing/housing.tgz")
	get_data_path = DOWNDATA.get_data(download_tag)
	uncompress_file_path = UNCOMP.uncompress(get_data_path) 
	read_csv = READCSV.load_data(uncompress_file_path)
	#print(str(read_csv.head()))
	#print(str(read_csv.info()))
	#print(str(read_csv.describe()))
	#print(str(read_csv["ocean_proximity"].value_counts()))
	
	scenario_betch(read_csv)
	
	modeling = modeling.Modeling()
	################### Lesson 2 ########################
	"""
	#train_set, test_set = Modeling.split_train_test(read_csv,0.2)
	csv_id = read_csv.reset_index()	
	train_set, test_set = modeling.split_train_test_by_id(csv_id, 0.2, "index")
	
	print(train_set, test_set)	
	print("train len : " + str(len(train_set))\
		 + " test len : " + str(len(test_set)))
	
	#csv_id['id'] = read_csv["longitude"] * 1000 + read_csv["latitude"]
	#train_set, test_set = Modeling.split_train_test_by_id(csv_id, 0.2, "id")
	"""
	################# Lesson 3 ############################
		
	train_set, test_set = train_test_split(read_csv, test_size=0.2, random_state=42)
	print(train_set, test_set)	
	print("train len : " + str(len(train_set))\
		 + " test len : " + str(len(test_set)))
	



