class Solution {
    public int singleNumber(int[] nums) {
        int ele = 0;
        
        for(int val : nums) {
            ele ^= val;
        }
        
        return ele;
    }
}