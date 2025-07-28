class Solution {
private:
    int n = 0;
    int maximum;
    int ans;
    vector<int> nums;
public:
    int countMaxOrSubsets(vector<int>& nums) {
        this->nums = nums; 
        n = nums.size();
        maximum = 0;
        ans = 0;
        for (int i = 0;i<n;i++){
            maximum |= nums[i];
        }
        back(0,0);
        return ans;
    }
    void back(int temp, int idx){
        if(idx == n){
            if(temp == maximum){
                ans += 1;
            }
            return;
        }
        back(temp|nums[idx],idx+1);
        back(temp,idx+1);
    }
        
};
