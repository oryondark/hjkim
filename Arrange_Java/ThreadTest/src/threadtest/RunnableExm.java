package threadtest;

class ExtendedClass {
	
	public void printText(String str) {
		

		System.out.println(str);
	}
}

class RunnableTest extends ExtendedClass implements Runnable{

	@Override
	public void run() {
		// TODO Auto-generated method stub
		ExtendedClass t = new ExtendedClass();
		for(int i = 0; i < 10; i++)
			t.printText("runnable_" + i);
	}
}

public class RunnableExm extends RunnableTest{

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		RunnableTest runnable = new RunnableTest();
		Thread t = new Thread(runnable);
		Thread t2 = new Thread(runnable);
		
		t.start();
		t2.start();
	}

}
