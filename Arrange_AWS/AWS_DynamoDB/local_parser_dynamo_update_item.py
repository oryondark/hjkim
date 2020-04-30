import os
import boto3

image_file_list = []
signature_list = [
    'ffd8ffe0' #image file header check
]


def dir_parser(path):
    items = os.listdir(path)

    for item in items:
        join_path = os.path.join(path,item)
        if os.path.isdir(join_path) == True:
            dir_parser(join_path)
        else:
            #print(join_path)
            image_check_andAppend(join_path)


def image_check_andAppend(path):
    with open(path, 'rb') as fp:
        byte = fp.read(4)
        if signature_check(byte):
            file_name = path.split('/')[-1].split(' ')
            if(len(file_name) > 1):
                file_name = [file_name[0] + "_" + file_name[1]]

             
            image_file_list.append(''.join(file_name))

def signature_check(byte):
    res = False
    for sig in signature_list:
        if byte.hex() == sig:
            res = True
            break
        
    return res

def foreach_image_item(table):
    for img in image_file_list:
        dynamoDB_update_item(img, table)

def dynamoDB_update_item(img, table):
    print("updating---------")
    res = table.update_item(
            Key = {
                'WorkerId': '2'
            },
            UpdateExpression = "SET #img = :img",
            ExpressionAttributeNames = {
                '#img': img.split(".")[0]
            },
            ExpressionAttributeValues = {
                ':img': {
                    "done": False,
                    "path": "path/to/file" + img
                }
            },
            ReturnValues = "UPDATED_OLD"
        )
    print(res)
    
if __name__ == "__main__":
    dir_parser('.')
    #print(image_file_list)
    client = boto3.client('dynamodb')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("kookminUniv_bucket")
    foreach_image_item(table)

