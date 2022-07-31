# include <stdlib.h>

void entero(num)
{
	printf("\nInicio de funcion callback:");
	ingreso();
	
}


void ingreso()
{
	int a;
printf("ingresse un numero:");
scanf("%d", &a);

}

void ingreso();
void entero(nump);
main()
{
	
	printf("\nFuncion callnabck");
	entero(ingreso);
	printf("el numero ingreasodad des : %d",a);
	
	
}

