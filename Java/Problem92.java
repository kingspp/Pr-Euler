
public class Problem92 {
	
	public static void main(String v[])
	{
		double start = System.nanoTime();		
		int one=0,en=0;
		int num=85,t=0,sum=0;
		
		
		for(int i=10;i<100;i++){
			while(true){
			while(num>0)
			{
				t=num%10;
				sum+=Math.pow(t, 2);
				num=num/10;
			}	
			
				if(sum==89){
					en++;
					System.out.println("89");
					break;
				}
				else if(sum==1){
					one++;
					System.out.println("1");
					break;
				}
				System.out.print(sum+"--> ");
				num=sum;
				sum=0;
			
			}
			System.out.println(i);
		}
			
					
		
		
		//System.out.println(en);
		//System.out.println(one);
		
		
		double end = System.nanoTime();
		System.out.println("Time Elapsed is: " + String.valueOf((end - start))
				+ "ns");
	}
	

}

