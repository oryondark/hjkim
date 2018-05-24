### UpdateItem Example for Javascript

!! 필독 !!
DynamoDB Json에서 Key 부분은 변수가 할당되지 않는다. 
따라서 ExpressionAttrbuteValues 와 ExpressionAttributeNames를 활용하여 Key를 Matching 해야한다.
그 예제는 아래와 같다.

```Javascript
  var value;
	var dynamodb = new AWS.DynamoDB();
	var parm = {
		Key: {
			"WorkerId":{
				S:"1"
			}
		},
		ExpressionAttributeNames:{
			"#keyMap": value, // -> Key is match to variable.
		},
		ExpressionAttributeValues: {
			":keyMap": {
				M: {
					"Attr": {
						S: ""
					},
					"Attr": {
						S: ""
					}
				}
			}
		},
		UpdateExpression:"SET #img = :img",
		TableName : "simpleImgInfoTable_kookmin",
		ReturnValues:"UPDATED_OLD"
	};
  
  dynamodb.updateItem(parm, function(err, data){
    if(err) console.log(err);
    else console.log(data);
  });
```
