class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        
       int[] result=Arrays.copyOf(nums,nums.length);
        Arrays.sort(result);
        for(int i=0;i<nums.length;i++){

            for(int j=0;j<result.length;j++){
                if(nums[i]==result[j]){
                    nums[i]=j;
                    break;
                }
            }

        }
        return nums;
    }
}