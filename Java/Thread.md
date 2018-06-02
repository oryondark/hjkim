1.[Thread](#thread)<br>
2.[Runnable](#runnable)

### Thread

* Usage for basic.
```java
class PrintText extends Thread{
	
	public void setText(String str) {
		setName(str); // naming for Thread
	}
	
	public void run() { //required.
		for(int i = 0; i < 10; i++) {
			System.out.println(i + " Thread Run : " + getName());
		}
	}
}
```

* main()
```java
public class TrheadExm {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PrintText p = new PrintText();
		PrintText p2 = new PrintText();
		p.setText("Thread_1");
		p2.setText("Thread_2");
		
		p.start();
		p2.start();
	}

}
```

* be followed.
```shell
0 Thread Run : Thread_1
0 Thread Run : Thread_2
1 Thread Run : Thread_2
2 Thread Run : Thread_2
3 Thread Run : Thread_2
4 Thread Run : Thread_2
5 Thread Run : Thread_2
6 Thread Run : Thread_2
```


### Runnable

* you make to implementation Runnable Interface for thread if you aready extend class.
```java
class RunnableTest extends ExtendedClass implements Runnable{

	@Override
	public void run() {
		// TODO Auto-generated method stub
		ExtendedClass t = new ExtendedClass();
		for(int i = 0; i < 10; i++)
			t.printText("runnable_" + i);
	}
}
```

* Let write to main code.
```java

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		RunnableTest runnable = new RunnableTest();
		Thread t = new Thread(runnable);
		Thread t2 = new Thread(runnable);
		
		t.start();
		t2.start();
	}

```
* for success, you can see that look at like the below.
```shell
runnable_0
runnable_0
runnable_1
runnable_1
runnable_2
```

