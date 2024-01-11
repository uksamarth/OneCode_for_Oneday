#include <bits/stdc++.h>
using namespace std;

int main() 
{
	// your code goes here
	int n;
	cin>> n;
	int a[n],i;
	for (i=0;i<n;++i)
	cin>>a[i];
	
	int min = INT_MAX ,max = INT_MIN;
	for (i=0;i<n;i++)
	{
	    if(a[i]<min)
	    min=a[i];
	}
	for (i=0;i<n;i++)
	{
	    if(a[i]>max)
	    max=a[i];
	}
	cout<<min<<endl;
	cout<<max<<endl;
}
