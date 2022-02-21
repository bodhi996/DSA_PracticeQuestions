#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	   int n;
	   cin>>n;
	   vector<int> a(n,0);
	   for(int i=0;i<n;i++)
	   {
	       cin>>a[i];
	   }
	   sort(a.begin(),a.end());
	   int prev=-1, count=0,ans=1,c=0;
	   for(int i=n-1;i>=0;i--)
	   {
	       if(a[i]!=prev)
	       {
	           prev=a[i];
	       }
	       else
	       {
	           count+=1;
	       }
	       if(count==1)
	       {
	           ans*=a[i];
	           count=0;
	           c++;
	           prev=-1;
	       }
	       //cout<<ans<<" "<<prev<<" "<<endl;
	       if(c==2)
	       break;
	   }
	   if(c==2)
	   cout<<ans<<endl;
	   else
	   cout<<-1<<endl;
	}
	return 0;
}
