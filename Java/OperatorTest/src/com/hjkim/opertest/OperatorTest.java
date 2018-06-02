package com.hjkim.opertest;

public class OperatorTest {

	public static void main(String[] args) {
		int i = 0;
		
		int v = i + 1 + 1 * 3;
		System.out.println(v);
		// 4
		
		int b = (i + 1 + 1) * 3;
		System.out.println(b);
		// 6
		
		int c = i++ - 25;
		System.out.println(c);
		// -25
		System.out.println(i);
		// 1
		
		int z = ++i - i++; // i == 2
		System.out.println(z);
		// 0
		
		System.out.println(i);
		int x = (i--);
		System.out.println(x);
		// 3
		
		System.out.println(i);		
		int f = (i++) + (i--);
		System.out.println(f);
		//5
		
		int g = i;
		System.out.println(g);
		//2
		
	}

}
