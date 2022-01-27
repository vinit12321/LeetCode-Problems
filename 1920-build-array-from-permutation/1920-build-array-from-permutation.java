class Solution {
    public int[] buildArray(int[] nums) {
         int[] new_array=new int[nums.length];
        for(int i=0;i<nums.length;i++)
        {
            new_array[i]=nums[nums[i]];
        }

    return new_array;
    }
}