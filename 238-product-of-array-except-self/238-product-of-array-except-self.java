class Solution {
    public int[] productExceptSelf(int[] nums) {
        int flag=0;
        int prod=1;
        for(int i=0;i<nums.length;i++){
            
            if(nums[i]==0){
                flag++;
            }
            else{
                prod*=nums[i];
            }
        }
        
        int arr[]=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            
            if(flag>1){
                arr[i]=0;
            }
            else if(flag==0){
                
                arr[i] = (prod / nums[i]);
            }
            else if (flag == 1 && nums[i] != 0) {
                arr[i] = 0;
            }
 
           
            else
                arr[i] = prod;
            
        }
        
        return arr;
    }
}