# recursive function
def directory_parser(target):
    list = os.listdir(target)
    for item in list:
        path = os.path.join(target, item)
        if os.path.isdir(path) == True:
            print("/{} : it's directory".format(item))
            directory_parser(path)
        else:
            print("{} : is full_path".format(path))
