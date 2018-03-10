import os
from six.moves import urllib

class DOWNDATA:

        def download_tag(path):
                #input path = "second/third" or "second/third/.../last"
                DOWNLOAD_SOURCE_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master"

                JOINING_PATH = DOWNLOAD_SOURCE_ROOT + "/" +path
                print("DEBUG Message : " + str(JOINING_PATH))
                return JOINING_PATH


        def get_data(source_path):
                if not os.path.isdir("/home/hadoopadm/MLtest/MLtest/collect_csv"):
                        os.makedirs("/home/hadoopadm/MLtest/MLtest/collect_csv")

                SAVE_PATH = "/home/hadoopadm/MLtest/MLtest/collect_csv/something.tgz"
                try:
                        urllib.request.urlretrieve(source_path, SAVE_PATH)
                        file_check = os.path.exists(SAVE_PATH)
                        if file_check == True:
                                print("DEBUG Message : " + str(SAVE_PATH))
                                return SAVE_PATH

                        return 0
                except:
                        return 0


