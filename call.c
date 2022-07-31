#include <stdio.h>

void impresion(int *var,void numero());
void numero();

main()
{
	int ds;
	
printf("Inicio de funcion");
impresion(&ds,numero);

}

void numero(){
	int x;
	x=10;
		
}

void impresion(int *var,void numero()){
	printf("\nImpresion del nuemro:");
	numero();
	printf("\nel valor de x=%d",var);	
}


