#include <stdio.h>

void main()
{
    int i, j, k=0;
  printf("Enter the number of rows");
  scanf(%s",&a);
    for(i=1; i<=a; i++)
    {
	for(j=1; j<=(a-i); j++)
	{
	   printf(" ");
	}
	while(k!=(2*i-1))
	{
	   printf("*");
	   k++;
	}
	k=0;
	printf("\n");
    }
}
