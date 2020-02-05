#include<stdio.h>

int main()

{
    int x=0, y=0;
    char z[20];
    scanf("%s",z);
    int l=strlen(z);
    for(int i=0;i<l;i++)
    {
        if(z[i]=='z')
            x++;
        else if (z[i]=='o')
            y++;
        
    }
    if(2*x==y)
        printf("Yes");
    else
        printf("No");
    

    return 0;
}




