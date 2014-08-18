/*
 * Problem2.c
 *
 *  Created on: Aug 17, 2014
 *      Author: Prathyush
 */

#include <stdio.h>
#include <time.h>

int MIN=0,MAX=0;

int main() {
	time_t start, end;
	time(&start);
	printf("Fibonacci Series \n");
	printf("%d \n",fib(0,4000000));
	time(&end);
	double dif = difftime(end, start);
	printf("Elasped time is %.2lf seconds.", dif);
	return 0;
}

int fib(int MIN,int MAX)
{
	int even=0,a=MIN,b=MIN+1,i=0,t=0;
	for(i=0;i<=MAX;i++)
	{
		t=a;
		a=b;
		b=t+b;
		if(b>MAX)
		{
			break;
		}
		if(b%2==0)
		{
			even+=b;
		}
	}
return even;
}
