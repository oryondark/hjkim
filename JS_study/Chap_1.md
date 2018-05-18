#### 1. Bagic Usage <br>

 * 자바스크립트는 ES5와 ES6 두개의 작성 방법이 존재.
 * 두 방법은 장단점을 비교할 수 있을 부분은 존재하지 않지만, 각자의 코딩스타일에 맞춰 ES5나 ES6로 선택할 수 있음.
 * 두 기법은 서로 혼용이 가능하기 때문에 자바스크립트가 매우 자유로운 코딩스타일을 제공하는 강력한 스크립트 언어라고 할 수 있음.
 * 아직까지는 Type 지정이 편리한 ES5를 많이 사용하고 있지만, 간혹 Type이 분명하고 제한되어야 할 상황에선 ES6 방식을 혼용하는 중.
 
 
#### 2. What is Type JavaScript Language

 * 자바스크립트는 멀티패러다임(Multiple Paradigm) 언어로 프로그래밍 기법을 한정할 수 없음.
 * 일반적으로 Javascript는 Prototype Language such as Oriented-Object 라고 불림
 * 프로토타입이란 사실 인터프리터 방식 언어에서는 불가능한 개념에 가깝지만, 자바스크립트는 프로토타입 언어라고 확정되어 있으며, 이 부분이 다른 스크립트 언어들과 비교했을 때 매우 강력한 기술이 됨.

#### 3. What is Prototype?
  
 * 프로토타입의 어원은 '초기모델', '견본' 등으로 내세우려는 어떠한 Something의 기초가되는 형태.
 * 자바스크립트가 객체지향과 유사하다는 이유는 바로 이 프로토타입을 사용하기 때문이며, 이는 자신의 원형이되는 패키지(*.js)를 하나의 Class화하여 배포하는 방식
 * 기본적은 자바스크립트 작성방법을 설명하면서, 프로토타입과 비교. Look at the below.
 
 ```javascript
 // @ [1] Basic
 // script type ES5.
 function basicFunction(variable){
    // variable is non-required.
 }
 
 // @ [2] Prototype
 basicFunction.prototype.createMethod = "Test"
 
 ```

 * 프로토타입은 위 코드와 같이 작성가능.
 * 기존 코드의 차이는 createMethod가 없었지만, 프로시저(함수)를 프로토타입으로 Clonning 하면서 메서드를 추가한 새로운 객체를 만듬.
 * 따라서 일반적인 인터프리터 언어가 프로시저형태가 아닌 객체 형태로 사용이 가능하게 되는 점이 있음. 이에 자바스크립트는 기존의 언어와 다르게 객체같은 언어로 불림.
 
 
#### 4. identifier

  * Javascript는 ES5, ES6 
 
