from download_data import DOWNDATA
from read_csv import READCSV
from uncompress import UNCOMP

if __name__ == "__main__":

        download_tag = DOWNDATA.download_tag("datasets/housing/housing.tgz")
        get_data_path = DOWNDATA.get_data(download_tag)
        uncompress_file_path = UNCOMP.uncompress(get_data_path)
        read_csv = READCSV.load_data(uncompress_file_path)
        print(str(read_csv))

