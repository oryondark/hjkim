import zipfile
import os,sys

#def analyser(path):

def getApkList(dirpath):
	apkList = [] 
	for getapk in os.listdir(dirpath):
		#print (str(getapk))
		apkList.append(str(getapk))
	
	return apkList

def getZipArch(apkfile):
    archive = zipfile.ZipFile(apkfile)
    return archive

def getInnerFiles(archive):
    innerFileList = []
    for getOnceName in archive.namelist():
        #print(str(getOnceName))
        innerFileList.append(getOnceName)
        
    return innerFileList

def DEXMLfilter(data):
    """
    for data in dataList:
        if data.lower() == "androidmanifest.xml":
            #print(str(file))
            
        
        if data.lower() == "classes.dex":
            #print(str(file))
    """
    conditions = ['androidmanifest.xml', 'classes.dex']
    
    if(data.lower() in conditions):
        return data

if __name__ == "__main__":
	dirpath = "./apkfolder"
	apklist = getApkList(dirpath)
        
        global fileList
	for getname in apklist:
            global archive_data 
            archive_data = getZipArch(dirpath+"/"+getname)
            fileList = getInnerFiles(archive_data)

            print ("dex size = "\
                    + str(archive_data.getinfo('classes.dex').file_size))

        listForAnalysis = list(filter(DEXMLfilter, fileList))
        print (str(listForAnalysis))
        archive_data.close()


