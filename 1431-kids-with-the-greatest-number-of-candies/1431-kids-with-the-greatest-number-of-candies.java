class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> lis=new ArrayList<>();
        int max=0;
        for(int i=0;i<candies.length;i++){
            if(max<candies[i]){
                max=candies[i];
            }
        }
        for(int arr:candies){
            if((arr+extraCandies)<max){
                lis.add(false);
            }
            else
            {
                lis.add(true);
            }
        }
    return lis;
    }
}