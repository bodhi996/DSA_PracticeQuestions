#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int n;
    cin>>n;
    while(n--)
    {
        string s,wd="";
        cin>>s;
        for(int i=0;i<s.size();i++)
        {
            if(i!=s.size()-1 && (s[i]=='s' && s[i+1]=='m') || (s[i]=='m' && s[i+1]=='s'))
            {
                wd+='m';
                i++;
            }
            else
               wd+=s[i];
        }
        //cout<<wd;
        unordered_map<char,int> umap;
        umap['s']=0;
        umap['m']=0;
        for(int i=0;i<wd.size();i++)
        {
            umap[wd[i]]++;
        }
        
        if(umap['s']>umap['m'])
        cout<<"snakes";
        if(umap['s']<umap['m'])
        cout<<"mongooses";
        if(umap['s']==umap['m'])
        cout<<"tie";
        cout<<endl;//<<wd<<endl;
    }
	return 0;
}
