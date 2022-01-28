class Solution {
    public int numIdenticalPairs(int[] nums) {
        int total_pair=0;
    for(int i=0;i<nums.length;i++){
        for(int j=i+1;j<nums.length;j++){
            if(nums[i]==nums[j]){
                total_pair+=1;
            }
        }
        
    }
    
    return total_pair;
    }
}