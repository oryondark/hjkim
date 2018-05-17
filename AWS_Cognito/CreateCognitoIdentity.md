# Linkage DynamoDB

### 1. create new credential.
Open https://aws.amazon.com/, and then choose Create an AWS Account.<br><br>
[development guide]

**You can make credentials to use CLI**

```

aws cognito-identity create-identity-pool  \
--identity-pool-name DynamoPool  \
--allow-unauthenticated-identities  \
--output json

```
next to check your Aws Cognito CredentialPool Console.
You should look like at the below.

```

{
    "IdentityPoolId": "ap-northeast-2:2c838b20-2942-4a44-b7a2-c3d50438db93",
    "AllowUnauthenticatedIdentities": true,
    "IdentityPoolName": "DynamoPool"
}

```

* IdentityPoolId is insert to your browser(HTML or JavaScript etc..)
* IdentityPoolName is Object Name.

![alt text](https://github.com/oryondark/-/blob/master/AWS_Cognito/%EC%BD%94%EA%B7%B8%EB%8B%88%ED%86%A0_%EC%9E%90%EA%B2%A9%EC%A6%9D%EB%AA%85%ED%92%80%EC%83%9D%EC%84%B1.png)

### 2. Create your IAM role.
  [1] first, let you make to IAM role how create to trust object. < Web ID : amazon cognito > <br>
  [2] input your cognito identityPool ID (ex: ap-northeast-2:xxxx-xx-xx-xx-xxx). Just you can see cogito edit page. <br>
  ![alt text](https://github.com/oryondark/-/blob/master/AWS_Cognito/IAM%EC%A0%95%EC%B1%85%EC%83%9D%EC%84%B1.png)
  
  [3] and next, must be select policy. are you done it? Good!<br>
  [4] finally, look at below.<br><br>
  ![alt text](https://github.com/oryondark/-/blob/master/AWS_Cognito/%EC%8B%A0%EB%A2%B0%EA%B4%80%EA%B3%84%ED%8E%B8%EC%A7%91.png)<br>
  
  [5] copy code.
  ```
  {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "cognito-identity.amazonaws.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "cognito-identity.amazonaws.com:aud": "identityPoolId"
        },
        "ForAnyValue:StringLike": {
          "cognito-identity.amazonaws.com:amr": "unauthenticated"
        }
      }
    }
  ]
}
  ```

### 5. Configuration
\<**java Script**\>
<pre>
var mycred = new AWS.CognitoIdentityCredentials({
	region: 'region',
	IdentityPoolId:'IdentityPoolId',
	RoleArn: 'IAM Role Arn',
	Logins:{

	}
});    

AWS.config.credentials = mycred;
AWS.config.region = "ap-northeast-2";
AWS.config.version = "latest";
var dynamodb = new AWS.DynamoDB();
    
</pre>
  
### 4. Connect to Application <br>

  **1\. [DynamoDB]**
  


[development guide]:https://aws.amazon.com/ko/cognito/getting-started/ "cognito page"
[DynamoDB]:https:// ""
