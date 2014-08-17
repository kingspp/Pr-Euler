/*
 * Problem1.cpp
 *
 *  Created on: Aug 17, 2014
 *      Author: Prathyush
 */

#include <iostream>
#include <time.h>
using namespace std;

int main() {

	int i=0,num=0;
		time_t start,end;
		time (&start);
		cout<<"Sum of Multiples of 3 and 5\n";
		for (i = 3; i < 1000; i++) {
					if (i % 3 == 0) {
						num += i;
					}
					if (i % 5 == 0) {
						num += i;
					}
				}

		cout<<num<<"\n";
		time (&end);
		double dif = difftime (end,start);
		cout<<"Elasped time is %.2lf seconds."<<dif ;

		return 0;

   return 0;
}
