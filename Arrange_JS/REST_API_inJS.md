## REST API ?
REST API란 로이 필딩이 제안한 프로그래밍 디자인 방법론 중 하나<br>
HTTP Resource를 활용한 요청 처리 방식으로 가장 많이 알려져 있음<br>

## How do it work on?
1. 요청을 수용하는 Receiver Role Application이 구성되어 있어야하며,
2. Receiver Role Application은 서로 다른 요청을 처리하기 위한 다양한 시스템 어플리케이션에 데이터를 전달할 수 있어야 함.
3. 각 시스템 어플리케이션은 서로 독립이 되도록 구성되며, 따라서 모든 요청이 HOST by HOST 관계로 구성됨.
4. 작업을 요청한 Client Side Environment는 요청된 작업의 신뢰성을 위한 정보체, 예를 들어 세션 데이터와 같은 정보를 저장하고 있어야하며,
5. Reciever Role부터 시스템 어플리케이션까지 작업 처리의 주체가 되는 Service Side(or Server Side)에서는 작업에 필요한 일부 데이터를 제외한 불필요한 정보체는 저장하지 않음. (**Stateless**)

## Jquery based HTTP-Request
#### GET
GET 방식은 특정 자원의 데이터를 요청하기 위한 방법으로, 가장 간결하게 구성되어야하며, 요청에 필요한 일부 검색용 파라메터를 제외한 불필요한 데이터를 전달하면 안됨.<br>
따라서 최대한 URIs 내에 모든 쿼리 파라메터로 정보를 구성하여 전달해야하며, Client 또한 불필요한 행위가 발생하지 않도록 해야함.<br>
```javascript
/*
GET /{resource_location}/{data_identity}&{optional_query_parameter1&[optional_query_parameter2]}
*/
$.get('resource_location', {}, function(data) {

}
```
