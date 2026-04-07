class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int ans = 0;
        int curr = 0;
        if (k == arr.size())
            return arr;
        for(int i = 0;i<k;i++){
            curr+= abs(x-arr[i]);
        }
        int m = curr;
        int l = 0;
        int r = k-1;

        while(r < arr.size()){
            curr -= abs(x-arr[l]);
            l++;
            r++;
            curr += abs(x-arr[r]);

            if(curr < m){
                ans = l;
                m = curr;
            } 
        }
        vector <int> res;
        while(k){
            res.push_back(arr[ans]);
            ans++;
            k--;

        }
        return res;
        
    }
};