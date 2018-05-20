* **상속** 이란 부모 클래스가 가지는 메서드들의 집합을 하위 클래스가 사용할 수 있도록 하는 것.
* **생성자** 란 클래스의 이름과 동일한 메서드를 구현하여, 클래스가 호출될 시 곧바로 적용되는 메서드
* 생성자는 모두 상속 시 자동으로 호출되는 것을 원칙으로 함. 그렇기에 하위 클래스가 상위 클래스의 메서드를 물려받는 것처럼 보임.

##### Default constructor

* 기본 생성자는 매개변수 없이, 하위 클래스에서 상위 클래스를 상속 받자마자 자동으로 호출됨.

##### 일반적인 생성자

* 매개변수를 가지는 생성자로 Super를 통해 호출이 가능함.

##### super()

* super는 상속받은 상위 클래스의 생성자를 호출하기 위한 것으로, 대게 매개변수가 존재하는 생성자가 있을 경우 사용됨.

```Java
class AbTest1 {
	
	int t1;
	public AbTest1(int s) {
		t1 = s;
		System.out.println(t1);
	}
}

class AbTest2 extends AbTest1{

	AbTest2(int d){
		super(d);
		System.out.println("test2\n");
	}
}

public class SuperTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		AbTest2 test = new AbTest2(1);
		int test2 = test.t1;
		System.out.println(test2);
	}
}
```
