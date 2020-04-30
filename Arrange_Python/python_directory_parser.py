'''
Recursive Generator Directory Parser
'''
def directory_parser(target):
    list = os.listdir(target)
    for item in list:
        path = os.path.join(target, item)
        if os.path.isdir(path) == True:
            print("/{} : it's directory".format(item))
            yield directory_parser(path)
        else:
            print("{} : is full_path".format(path))
            yield path

path = directory_parser("precede_path")
for inner_path in path:
    for item in inner_path:
        print(item)
