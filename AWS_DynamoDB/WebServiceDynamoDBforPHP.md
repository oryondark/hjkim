### Configure to DynamoDB Client for PHP
```
        $client = dynamoClient::factory(array(
                'profile' => 'default',
                'region' => 'ap-northeast-2',
                'version' => 'latest'
        ));
```
if you returned version error from configure_php, Should defining for match version. (= recommanded for 'latest' )


### Get Item from DynamoDB
give your one Item

at first, parameter below.
* AttributesToGet : for get Column name.
* ConsistentRead : if true, received to exist data but not false
