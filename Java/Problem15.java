/*
Created on Aug 30, 2014

@author: Prathyush

It uses Pascal's Triangle to solve the lattice paths. Change the grid to suit your needs.
Java has concept of BigInteger to handle numbers in string format.
Formula used is: N!/ (K! * (N-K)!)
*/

import java.math.BigInteger;
public class Problem15 {

	public static void main(String args[])
	{
		double start = System.nanoTime();		
		final int grid=4;
		int n=grid*2;		
		String N=(factorial(n));
		String K=(factorial(n/2));
		String NK=(factorial(n/2));
		BigInteger opr=new BigInteger(N); 
		opr=opr.divide(new BigInteger(K));
		opr=opr.divide(new BigInteger(NK));
		System.out.println("No of lattice paths for "+grid+" x "+ grid + " grid is :" +opr);		   
		double end = System.nanoTime();
		System.out.println("Time Elapsed is: " + String.valueOf((end - start))
				+ "ns");
	}
	
	public static String factorial(int n) {
	       BigInteger fact = new BigInteger("1");
	       for (int i = 1; i <= n; i++) 
	           fact = fact.multiply(new BigInteger(i + ""));	       
	       return fact.toString();
	   }
}

