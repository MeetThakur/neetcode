class Solution {
public:
    vector<int> partitionLabels(string s) {
    map<char, int> mp;
    vector <int> ans;
    ans.push_back(-1);
    for(int i = 0;i<s.size();i++){
        mp[s[i]] = i;
    }

    int l = 0;
    int r = mp[s[0]];
    if (r == s.size()-1){
        ans.push_back(r);
        return ans;
    }
    while (l<s.size()){
        if(s[l] == s[r]){
            if (l!=r)
                l++;
            else{
                ans.push_back(r);
                l++;
                r = max(mp[s[l]],r);
            }
        }
        else{
            if(mp[s[l]]<r)
                l++;
            r=max(mp[s[l]],r);
        }
    }
    vector <int> vec;
    for(int i = 1;i<ans.size();i++){
        vec.push_back(ans[i]-ans[i-1]);
    }
    return vec;
    }
};
