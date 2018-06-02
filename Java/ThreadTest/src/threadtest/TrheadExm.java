package threadtest;


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
