class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int ts = accumulate(nums.begin(), nums.end(), 0);

        if (ts % k != 0) {
            return false;
        }

        int target = ts / k;
        int n = nums.size();

        vector<int> sub(k, 0);

        function<bool(int)> backtrack = [&](int index) -> bool {
            if (index == n) {
                return true;
            }

            for (int i = 0; i < k; ++i) {
                if (i > 0 && sub[i] == sub[i - 1]) {
                    continue;
                }

                sub[i] += nums[index];

                if (sub[i] <= target && backtrack(index + 1)) {
                    return true;
                }

                sub[i] -= nums[index];
            }

            return false;
        };

        sort(nums.begin(), nums.end(), greater<int>());

        return backtrack(0);
    }
};
