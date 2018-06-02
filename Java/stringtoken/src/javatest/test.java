package javatest;

import java.util.StringTokenizer;
import java.lang.NumberFormatException;

public class test {
	public static void main(String[] args)  {
		// TODO Auto-generated method stub
		String data = "1980	26	27	28	28	28	30	31	31	31	30	30	30	29	"
					+ "1980	26	27	28	28	28	30	31	31	31	30	30	30	45	";
		StringTokenizer s = new StringTokenizer(data, "\t");
		String firstToken = null;
		String lastToken = null;
		
		//System.out.println(s);
		
		String row = s.nextToken();
		firstToken = row;
		System.out.println("first token : " + firstToken);
		/*
		while(s.hasMoreTokens()) {
			try {
			lasttoken = s.nextToken();
			System.out.println(lasttoken);
			int avgprice = Integer.parseInt(lasttoken);
			System.out.println(avgprice);
			} catch(NumberFormatException e) {
				continue;
			}
		*/
		while(s.hasMoreTokens()) {
			lastToken = s.nextToken();
		}
		System.out.println("last token : " + lastToken);
	}

}
