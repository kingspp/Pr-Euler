/*
 * Problem1.c
 *
 *  Created on: Aug 17, 2014
 *      Author: Prathyush
 */


#include <stdio.h>
#include <time.h>

int main()
{
	int i=0,num=0;
	time_t start,end;
	time (&start);
	printf("Sum of Multiples of 3 and 5\n");
	for (i = 3; i < 1000; i++) {
				if (i % 3 == 0) {
					num += i;
				}
				if (i % 5 == 0) {
					num += i;
				}
			}

	printf ("%d \n",num);
	time (&end);
	double dif = difftime (end,start);
	printf ("Elasped time is %.2lf seconds.", dif );

	return 0;
}
