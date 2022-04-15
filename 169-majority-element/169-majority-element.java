class Solution {
   public int majorityElement(int[] nums) {
        int cand=findCandidate(nums,nums.length);
        /* Print the candidate if it is Majority*/
        if (isMajority(nums, nums.length, cand)){
            return cand;
        }
        else
            return 0;


    }
    public  boolean isMajority(int a[],int size,int cand){
        int count=0;
        for(int i=0;i<size;i++){
            if(cand==a[i]){
                count++;
            }
        }
        if(count>size/2)
            return true;
        else
            return  false;

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