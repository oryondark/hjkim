##### 자바 프로그래밍 인터페이스
* 본 예제에서는 하나의 인터페이스를 구현했지만, 추상(abstract)과 다르게 직접 구현하길 원하는 인터페이스를 여러개 implements 할 수 있다.

```Java
interface letter {
	void addr();
	void body();
	void footer();
}

class writeLetter implements letter {



	public void addr() {
		String from;
		from = "Kookmin Univ. Bigdata Lab.";
		System.out.println("from : " + from);
	}


	public void body() {
		String body;
		body = "hello, my Letter";
		System.out.println("\n letter : \n" + body);
	}


	public void footer() {
		String foot;
		foot = "H.J.Kim";
		System.out.println("\n footer \n" + foot);
	}
	
}

public class WriteInterface {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		writeLetter wl = new writeLetter();
		
		wl.addr();
		wl.body();
		wl.footer();
	}
}
```
