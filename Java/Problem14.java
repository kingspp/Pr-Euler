
public class Problem14 {

	public static void main(String args[])
	{
		double start = System.nanoTime();
		
		final int num=1000000;		
		int[] cache = new int[num + 1];
		int count=0,grt=1,gnum=1;
		long temp; // Very Important for temp to be long!!
		
		for (int i = 0; i < cache.length; i++) 
		    cache[i] = -1;		
		
		
		for (int i=2;i<=num;i++)
		{			
			temp=i;
			count = 0;
			while(temp!=1 &&temp>=i)
			{
				count++;
				if(temp%2==0)				
					temp=temp/2;					
				else				
					temp=3*temp+1;						
			}
			cache[i] = count + cache[(int) temp];			
			if(cache[i]>grt){
				grt=cache[i];
				gnum=i;
			}
		}
		System.out.println("The number "+gnum+" produces sequence of length "+grt);	
		
		double end = System.nanoTime();
		System.out.println("Time Elapsed is: " + String.valueOf((end - start))
				+ "ns");
	}
}
