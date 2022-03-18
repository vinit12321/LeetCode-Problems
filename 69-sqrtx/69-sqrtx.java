class Solution {
    public int mySqrt(int x) {
        if (x <= 1) return x;
        long s = 1, e = x;
        long mid = 1;
        
        while (s <= e) {
            mid = (s + e) / 2;
            long tx = ((long) mid) * mid;
            if (tx == x) return (int) mid;
            if (x < tx) {
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }
        
        return (int) e;
    }
}