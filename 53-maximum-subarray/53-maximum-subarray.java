class Solution {
    public int maxSubArray(int[] nums) {
        int sum=nums[0];
        int max_value=nums[0];
        for(int i=1;i<nums.length;i++){
            if(sum<0){
                sum=0;
            }
            sum+=nums[i];
          max_value=Math.max(max_value,sum);
        }
        return max_value;
    }
}