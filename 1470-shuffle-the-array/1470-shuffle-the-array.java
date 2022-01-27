class Solution {
    public int[] shuffle(int[] nums, int n) {
       int[] result=new int[nums.length];
        int k=0;
        for(int i=0;i<(nums.length)/2;i++)
        {
            result[k]=nums[i];
            k++;
            result[k]=nums[i+n];
            k++;
        }
        return result;
    }
}