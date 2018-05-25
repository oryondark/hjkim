### Basic Lambda Execution Example.
1. access IAM role of your console.
2. create Role<br>
![alt_text](https://github.com/oryondark/-/blob/master/AWS_Lambda/%EC%97%AD%ED%95%A0%EC%83%9D%EC%84%B1.png)<br>

3. To run Lambda, assigned permission to access application.
![alt_text](https://github.com/oryondark/-/blob/master/AWS_Lambda/assignedPermission.png)<br>

    * **For test, a basic permission assign to IAM for Lambda you can try test.**
    * **Would you like to you want so much access application? follow to above assign.**

3. Below is example for access policy.<br>
[get for permission Resource]<br>


```Json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "sns:Publish"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow", // get assign tirgger for DynamoDB
            "Action": [
                "dynamodb:UpdateItem"
            ],
            "Resource": "arn:arn.address"
        }
    ]
}
```

[get for permission Resource]:https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/Streams.Lambda.Tutorial.html#Streams.Lambda.Tutorial.SNSTopic "follow link"
