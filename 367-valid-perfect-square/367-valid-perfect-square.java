class Solution {
    public boolean isPerfectSquare(int num) {
        
        if(num==1)
            return true;
        
        int low = 0;
        int high = num/2;
        int mid = 0;
        while(low<=high)
        {
            mid = low + (high-low)/2;
            if((float)num/mid<(float)mid)
                high = mid - 1;
            else if((float)num/mid>(float)mid)
                low = mid + 1;
            else
                return true;
        }
        return false;
    }
}