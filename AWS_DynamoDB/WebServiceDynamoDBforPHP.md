### Configure to DynamoDB Client for PHP
```
$client = new Aws\DynamoDb\DynamoDbClient([
        'region' => 'ap-northeast-2',
        'version' => 'latest',
        'credentials' => [
                'key' => '',
                'secret' => ''
        ]
]);
```
if you returned version error from configure_php, Should defining for match version. (= recommanded for 'latest' )


### Get Item from DynamoDB
```
        #print_r($client);
/* Describe table
$result = $client->describeTable([
         'TableName' => 'simpleImgInfoTable_kookmin',
]);
*/

$result = $client->getItem([
        'AttributesToGet' => ['attribute'],
        'Key' => [
                'KeyIsNumber' => [
                        'N' => '1']
                ],
        'TableName' => 'tableName',
        ]);
$test = $result;
echo $test; // for ajax.
```

so simple.
