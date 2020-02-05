#include<stdio.h>

int main()
{
    int n,i,j;
    int f=1;
    scanf("%d",&n);
    for(i=2 ; i < n; i++)
    {
        for(j = 2 ; j < i ; j++)
        {
            if(i%j==0)
            {
                f=0;
                break;
            }
            else if(i%j!=0)
            {
                f=1;
            }
        
        }
        if (f==1)
        {
            printf("%d ",i);
        }
           
    }
    return 0;
}