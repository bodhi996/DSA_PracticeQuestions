#include <iostream>
#include <bits/stdc++.h>
using namespace std;
bool valid(vector<int> &v)
{
    int c=v[0]%2;
    bool val=false;
    for(int i=1;i<v.size();i++)
    {
        if(v[i]%2!=c)
        {
            if(val==false)
            {
                c=v[i]%2;
                val=true;
            }
            else
            {
                val=false;
                break;
            }
        }
    }
    return val;
}
int main() 
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,c=0;
        cin>>n;
        vector<int> w(n,0);
        for(int i=0;i<n;i++)
        {
            cin>>w[i];
        }
        cout<<valid(w)<<endl;
    }
	return 0;
}
