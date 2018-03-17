import tarfile, os

class UNCOMP:
	
	def uncompress(path):
		SAVE_PATH = "/home/hadoopadm/MLtest/MLtest/collect_csv/"
		SAVE_NAME = "housing.csv"
		try:
			target = tarfile.open(path)
			stat = target.extractall(SAVE_PATH)
			SAVE_PATH = SAVE_PATH + SAVE_NAME
			print("Success get CSVfile")
			return SAVE_PATH
		except:
			print("Uncompress Error")
			return False
		
