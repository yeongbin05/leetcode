class Solution {
     private int ans = 0;
    private int maximum = 0;
    private int n;
    private int[] nums;

    public int countMaxOrSubsets(int[] nums) {
        this.nums = nums;
        this.n = nums.length;
        for (int i = 0; i < n;i++){
            maximum |= nums[i];
        }
        
        back(0,0);
        return ans;
        }
        private void back(int temp, int idx) {
        if (idx == n) {
                if (temp == maximum) {
                    ans += 1;
                }
                return;
            }

            // 1) 현재 nums[idx] 포함
            back(temp | nums[idx], idx + 1);
            // 2) 현재 nums[idx] 제외
            back(temp, idx + 1);
        }
            
        
        
}
