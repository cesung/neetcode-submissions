public class Solution {
    public int MySqrt(int x) {
        if (x < 2)
        {
            return x;
        }

        int left = 0, right = x/2;
        
        while (left < right)
        {
            var mid = left + (right - left) / 2 + 1;
            if (mid > x / mid)
            {
                right = mid - 1;
            }
            else
            {
                left = mid;
            }
        }

        return left;
    }
}