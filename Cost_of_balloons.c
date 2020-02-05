#include<stdio.h>

int max(int a,int b)
{
    if (a>b)
        return a;
    else 
        return b;
}

int min(int a, int b)
{
    if (a>b)
        return b;
    else 
        return a;
}

void main()
{   
    int t;
    scanf("%d",&t);
    for( int k=1; k<=t; k++)
    {
        int g,p;
        scanf("%d %d",&g,&p);
        int n;
        scanf("%d",&n);
        int x=0,y=0;
        for(int l=1;l<=n;l++)
        {
            int x1,y1;
            scanf("%d %d",&x1,&y1);
            x=x1+x;y=y+y1;
            
        }
        //calculating total.
        printf("%d\n",max(p,g)*min(x,y)+min(g,p)*max(x,y));
        
    }
}