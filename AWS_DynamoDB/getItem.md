### You can gave Item List from DynamoDB, and then do extract to each in List.

##### 1. GetItemList
```Javascript
  var dynamodb = new AWS.DynamoDB();
  var parm = {
		Key:{
			'YourPrimaryKey':{ /* Required */
				S:'String' // or M : {} or L : [] ... 
			}
		},
		TableName: 'simpleImgInfoTable_kookmin',
		//AttributesToGet:['Attr'] // only get that.
	};
  
  dynamodb.getItem(parm, function(err, data){
    if(err) console.log("getItem Error",err);
      else {
        // Let implements to callback use parametar data.
        console.log(data);
      }});
```

##### 2. Example for extraction each item.
```Javascript
$.each(data, function(key, value){
  //if(key != "")
  //if(key == "")
  // Json parser for Jquery.
}

```
