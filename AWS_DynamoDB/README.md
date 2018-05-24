**Create by hjKim. BigData Labs on Kookmin Univ.**

# Usage DynamoDB.



_Can following the link to click_

* ###### [1. Table, Article and Attribute](#table-and-article-and-attribute)
* ###### [2. Key](#key)
* ###### [3. Secondary Indexes](#secondary-indexes)
* ###### [4. DynamoDB Streams](#dynamodb-streams)
* ###### [5. Usage API](#dynamodb-api)

### DynamoDB core constituent.

  * ###### Table and Article and Attribute
    * Table : RDB의 Table의 기능과 유사
    * Article : Table 내에서 하나의 객체를 식별할 수 잇는 유일한 정보. is Key.
    * Attribute : 객체를 구성하는 다양한 항목들이 가지고 있는 
      정보들로 RDB에서는 각 항목당 하나의 원소(데이터 정보)가 저장되는 것과 비교하여, NoSQL에서는 하나의 항목이 1개 이상의 정보를 포함할 수 있다.
  
  * ###### Key
  	* Primary Key (기본키)
  	    - Partition Key : DynamoDB에서 말하는 기본키가 이것에 해당.
  	    - Partition & Sort Key : 파티션과 정렬 두가지 기능을 가지는 키로 첫 번째 속싱이 파티션키를 내부 해시 함수 입력으로 사용(물리적 스토리지 결정)하며, 파티션 키가 동일한 항목이 있을 때, 해당 파티션키가 정렬키를 추가로 가지고 있다면 정렬키를 기준하여 Sort되어 저장.

  * ###### Secondary Indexes
  	: 보조 인덱스라고 말하며 기본적으로 Index기능이 요구되지 않으므로 필수적인 부분은 아니다. 
  	* 보조 인덱스는 하나의 테이블 내에서 1개 이상을 정의할 수 있으며, Table에서 Data의 대한 Query를 수행할 때 대체키로 사용된다.
  	* Indexing을 위한 2가지 방법
  	    - Global secondary index – An index with a partition key and sort key that can be different from those on the table.
  	    - Local secondary index – An index that has the same partition key as the table, but a different sort key.
  	    - 각 Table마다 5개의 Local과 5개의 Global을 지정할 수 있다.


  * ###### DynamoDB Streams
  	: DynamoDB Table 내에서 발생하는 데이터 수정 Event를 캡처하기 위한 선택적 기능
  	* A new item is added to the table: The stream captures an image of the entire item, including all of its attributes.
  	* An item is updated: The stream captures the "before" and "after" image of any attributes that were modified in the item.
  	* An item is deleted from the table: The stream captures an image of the entire item before it was deleted.


  	각 스트림 정보는 아래와 같은 정보를 포함하고 있다.
  	name of tables, time stamp, specific meta-data 
  	
  	각 스트림정보는 24시간을 기준으로 삭제된다.


### DynamoDB API

   * ###### Control 
   		- CreateTable : 새로운 테이블 생성
		- DescribeTable : 기본키와 각 항목에 지정된 제약, index formation 등의 Table 정보를 반환
		- ListTables : 모든 Table name을 List로 반환
		- UpdateTable : Table과 관련된 모든 행위의 대해 수정사항을 반영
		- DeleteTable : 지정한 Table 및 그 Table의 종속되는 수 많은 Tab을 모두 제거.


   * ###### Data Plan
   		- Creating
   			1. PutItem : table내 Item을 생성하며, primary Key 지정 필수
   			2. BatchWriteItem : 최고 25개의 대한 Item 정보를 작성가능하며, PutItem을 통한 Network의 연속적 부하가 적다.

   		- Reading 
   			1. [GetItem] : 오직 1개의 Item 만을 가져온다. 이것은 전체 항목이나 일부 지정된 항목을 통해 검색이 가능하며, Primary Key 지정 필수
   			2. BatchGetItem : 최대 100개까지의 Item 정보를 가져올 수 있다. 단, 1개 이상의 Table의 대해 모든 호출될 수 있는 Item의 갯수는 총 100개를 뜻 한다.
   			3. Query : 조건으로 Index, Table, Partition Key(필수 지정) & Sort Key를 이용하여 일부 범위부터 전체 항목의 대해 조건에 부합하는 모든 Item의 정보를 질의 할 수 있다.
   			4. Scan : Table과 Index 정보를 통해 원하는 Item을 받아 올 수 있으며, Filter기능을 사용할 시 관심있는 데이터만을 질의할 수 있다.

   		- Updating 
   			1. UpdateItem : 하나 이상의 수정된 정보를 Partition Key를 이용하여, 해당하는 Article로 Update.
   						이때 속성의 대한 정보를 추가하거나 삭제도 가능하며, Update 상태를 열람할 수 있는 선택적 기능도 포함된다.

   		- Deleting
   			1. DeleteItem : 한개의 Item을 삭제.
   			2. BatchWriteItem : 최대 25개까지 삭제 가능.

   * ###### DynamoDB Streams
   		- ListStreams : Returns a list of all your streams, or just the stream for a specific table.
   		- DescribeStream : Returns information about a stream, such as its Amazon Resource Name (ARN) and where your application can begin reading the first few stream records.
   		- GetShardIterator : Returns a shard iterator, which is a data structure that your application uses to retrieve the records from the stream.
   		- GetRecords : Retrieves one or more stream records, using a given shard iterator.


[GetItem]:https://github.com/oryondark/-/blob/master/AWS_DynamoDB/getItem.md "link for Example GetItem"
