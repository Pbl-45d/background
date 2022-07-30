# include<stdio.h>

int producto(int a, int b);
void ingreso(int *a,int *b);

main()
{
	int a,b,c;
	ingreso(&a,&b);
	printf("\nEl producto es :");
	c=producto(a,b);
	printf("%d",c);
		
}


int producto(int a, int b)
{
	//printf("\nLa mltiplicacion es: %d", *a**b);
	
	if (b==0)
	return 0;
	else
	return a+producto(a,b-1);

}

void ingreso(int *a,int *b)
{
	printf("\nIngrese primer numero:");
	scanf("%d",a);
	printf("\nIngrese segundo numero:");
	scanf("%d",b);
}




