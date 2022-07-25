vector<pair<int,int>> temp;
    bool static comp(pair<int, int> a, pair<int,int> b)
    {
        return a.second  < b.second;
    }
    int maxMeetings(int start[], int end[], int n)
    {
        // Your code here
        for(int i=0;i<n;i++)
        {
            temp.push_back({start[i], end[i]});
        }
        sort(temp.begin(), temp.end(), comp);
        int st = temp[0].first;
        int en = temp[0].second;
        int meet = 1;
        
        for(int i=1;i<n;i++)
        {
            if(temp[i].first > en){
                meet++;
                en = temp[i].second;
            }
        }
        return meet;
    }
