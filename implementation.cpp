#include<bits/stdc++.h>

using namespace std;

int main()
{
  unsigned int a[10];
  memset(a,0,sizeof(a));
  int n;
  cin>>n;
  while(n!=0)
  {
    int w=n%10;
    switch (w) {
      case 0:
      {
        a[0]++;break;
      }
      case 1:
      {
        a[1]++;break;
      }
      case 2:
      {
        a[2]++;break;
      }
      case 3:
      {
        a[3]++;break;
      }
      case 4:
      {
        a[4]++;break;
      }
      case 5:
      {
        a[5]++;break;
      }
      case 6:
      {
        a[6]++;break;
      }
      case 7:
      {
        a[7]++;break;
      }
      case 8:
      {
        a[8]++;break;
      }
      case 9:
      {
        a[9]++;break;
      }
    }
    n=n/10;
  }
  for(int i=0;i<=9;i++){
    cout<<i<<(" ")<<a[i]<<endl;
  }
  return 0;
}
