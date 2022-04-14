class Solution {
public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> hs=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            int sum=target-nums[i];
            if(hs.containsKey(sum)){
                return new int[]{hs.get(sum),i};
            }
            hs.put(nums[i],i);
        }
        return new int[]{0,0};
    }
}