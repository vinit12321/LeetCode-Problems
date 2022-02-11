class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        int arr[]=new int[nums.length];
        for(int i=0;i<nums.length;i++) {
            insert(arr,nums[i],index[i]);
        }
        return arr;
    }
    public void insert(int[] arr, int num, int index) {
        int i;
        for(i=arr.length-1;i>index;i--){

            arr[i]=arr[i-1];
        }
        arr[i]=num;

    }
}