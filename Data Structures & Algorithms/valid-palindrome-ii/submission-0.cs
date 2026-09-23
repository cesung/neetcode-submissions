public class Solution {
    public bool ValidPalindrome(string s) {

        bool Check(int lo, int hi, int k)
        {
            while (lo < hi)
            {
                if (s[lo] != s[hi] )
                {
                    return k > 0 ? (
                        Check(lo + 1, hi, k - 1) ||
                        Check(lo, hi - 1, k - 1)
                    ): false;
                }
                lo += 1;
                hi -= 1;
            }

            return true;
        }

        var size = s.Length;
        return Check(0, size - 1, 1);
    }
}