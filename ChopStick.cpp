#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,d;
    cin>>n>>d;
    //cout<<d;
    int t=n;
	vector<int> b;
	while(t--)
	{
	    int x;
	    cin>>x;
	    b.push_back(x);
	}
	sort(b.begin(),b.end());
	int c=0;
	for(int i=0;i<b.size()-1;i++)
	{
	   
	    if(b[i+1]-b[i] <= d)
	    {
	        c++;
	        i++;
	    }
	   
	}
	cout<<c;
	return 0;
}
