#include<stdio.h>

int main()
{
	int l,n,w,h;

	scanf("%d %d",&l,&n);
	for(int i=1;i<=n;i++)
	{
		scanf("%d %d",&w,&h);
		if (w==h & w>=l)
		{
			printf("ACCEPTED\n");
		}
		else
		{
			if(w<l || h<l)
			{
				printf("UPLOAD ANOTHER\n");
			}
			else if (w>l || h>l)
			{
				printf("CROP IT\n");
			}
		}
	}
	return 0;
}