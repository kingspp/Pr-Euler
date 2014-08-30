/*
Created on Aug 19, 2014

@author: Prathyush
*/
public class Problem5 {

	public static void main(String v[]) {
		double start = System.nanoTime();
		int i=30;
		System.out.println("Least number divisible by first 20 natural numbers");

		while (i %  2 != 0 || i %  3 != 0 || i %  4 != 0 || i %  5 != 0 || 
		         i %  6 != 0 || i %  7 != 0 || i %  8 != 0 || i %  9 != 0 ||
		         i % 10 != 0 || i % 11 != 0 || i % 12 != 0 || i % 13 != 0 ||
		         i % 14 != 0 || i % 15 != 0 || i % 16 != 0 || i % 17 != 0 ||
		         i % 18 != 0 || i % 19 != 0 || i % 20 != 0)
		{
			i+=30;
		}
		
		System.out.println(i);
		
		
		double end = System.nanoTime();
		System.out.println("Time Elapsed is: " + String.valueOf((end - start))
				+ "ns");
	}

	
}
