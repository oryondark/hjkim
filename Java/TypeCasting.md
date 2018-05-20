### 강제 형 변환
##### 객체 지향에서 클래스의 강제 형 변환은 상속 관계가 성립되는 **객체** 간 변환이 가능

```Java
class A {
	String str_a = "Class is A\n";
}
class B extends A {
	String str_b = "Class is B\n";
}
class C extends B {
	String str_c = "Class is C\n";
}

public class TypeChanger {

	public static void main(String[] mainArg) {
		A a;
		a = new C();
		
		System.out.println(a.str_a);
		System.out.println(a.str_c); // -> error
	}
}
```

##### What happened?
A라는 클래스는 단순히 타입을 지정해주는 것.<br>
우리는 A라는 클래스 타입을 a로 assigned, 그러나 C 클래스를 객체화 하는 순간 타입이 A로 Casting 되며, C는 A,B 클래스 전부를 상속받고 있지만 결국 A만 사용가능한 상태로 
