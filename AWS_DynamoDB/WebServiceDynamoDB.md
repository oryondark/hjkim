**Create by hjKim. BigData Labs on Kookmin Univ.**

# Connection to AWS DynamoDB used for JavaScript.

1. ### Get Access Key for sign.
	
	1. Open the IAM and follow the navigation pane of the console that you have to choosing by that Users.
	2. next to click "add user"
	3. you must be typing user name, and choose programmin access on the access type.
	4. Create groub by AmazonDynamoDBFullAccess (= is AWS management), next.
	5. if you look at succed page, and let's copy accessKey&secretKey to page.

2. ### Get Started with DynamoDB from JS.
	
	1. follow ScriptTag in your HTML. 
	   ```<script type="text/javascript" src="https://sdk.amazonaws.com/js/aws-sdk-2.7.16.min.js"></script>```
	   and you can see the [API for AWS JS.][2]

	2. Configure for AWS.
		- Setting AWS region to using the Global Configure.
			AWS.confg.update({region: 'region'})
		- Setting AccessKey & SecretKey, example simple code below.
			```
			<pre>
				<script type="text/javascript">
					AWS.config.update({
						region : "region",
						endpoint : "enpoint", // service region endpoint
						accessKeyId: "",
						secretAccessKey: ""
				})
				</script>

			</pre> 

			```
			Show service region&enpoints List [link][1]






[1]:https://docs.aws.amazon.com/general/latest/gr/rande.html#ddb_region
[2]:https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/ 
