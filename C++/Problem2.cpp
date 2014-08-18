/*
 * Problem2.cpp
 *
 *  Created on: Aug 18, 2014
 *      Author: Prathyush
 */
#include <iostream>
#include <time.h>
using namespace std;

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


int main() {


		time_t start,end;
		time (&start);

		cout<<"Fibonacci Series\n";
		cout<<fib(0,4000000)<<"\n";

		time (&end);
		double dif = difftime (end,start);
		cout<<"Elasped time is "<<dif<<"sec" ;



   return 0;
}

