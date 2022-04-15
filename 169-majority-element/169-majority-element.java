class Solution {
   public int majorityElement(int[] nums) {
        int cand=findCandidate(nums,nums.length);
        /* Print the candidate if it is Majority*/
       return cand;


    }
    public  int findCandidate(int[] nums, int length) {
        int majIndex=0,count=1;
        for(int i=0;i<nums.length;i++){
            if(nums[majIndex]==nums[i]) {
                count++;
            }else{
                count--;
            }
            if(count==0){
                majIndex=i;
                count=1;
            }
        }
        return nums[majIndex];
    }

}