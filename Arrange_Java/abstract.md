##### 추상 메서드와 추상 클래스

```Java
abstract class absCls{
// is Blueprint
	abstract void absTest_1();
	abstract void absTest_2(int a, int b);
}

class testing extends absCls{
//is builder
	void absTest_1() {
		System.out.println("abstract Test");
	}
	
	void absTest_2(int a, int b) {
		int summary = a+b;
		System.out.println(summary);
	}
}

public class Abstract {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		testing test = new testing();
		test.absTest_1();
		test.absTest_2(25, 10);
	}
}
```
