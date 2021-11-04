#include <stdio.h>

int main()
{
    int even = 0;
    int odd = 0;
    int positive = 0;
    int negative =0;
    int i,j,n;
    for(i=0; i < 5; i++)
    {
        scanf("%d",&n);

        if(n % 2 == 0)
            even = even+1;
        else
            odd = odd+1;

        if(n<0)
            negative = negative+1;
        else if(n>0)
            positive = positive +1;



    }
    printf("%d valor(es) par(es)\n",even);
        printf("%d valor(es) impar(es)\n",odd);
        printf("%d valor(es) positivo(s)\n",positive);
        printf("%d valor(es) negativo(s)\n",negative);



    return 0;
}