class Solution {
public:
    vector<vector<string>> res;
    vector<vector<string>> partition(string s) {
        back(0,{},s);
        return res;
    }
    bool isPal(string s){
        int l = 0, r = s.size()-1;
        if(s.size() == 1) return true;
        while(l < r){
            if(s[l] != s[r]) return false;
            l++; r--;
        }
        return true;
    }
    void back(int i,vector <string> curr,string s){
        if(i==s.size()){
            res.push_back(curr);
            return;
        }

        string t;
        for (int j = i; j < s.size(); j++) {
            t = s.substr(i, j - i + 1);
            if (isPal(t)) {
                curr.push_back(t);
            } else {
                continue;
            }
            back(j+1,curr,s);
            curr.pop_back();
    }

    

}
};
