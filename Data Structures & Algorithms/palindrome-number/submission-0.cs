public class Solution {
    public bool IsPalindrome(int x) {
        if (x == 0)
        {
            return true;
        }

        if (x < 0)
        {
            return false;
        }

        var digits = new List<int>();
        while (x > 0)
        {
            var d = x % 10;
            digits.Add(d);
            x /= 10;
        }

        var l = digits.Count;
        var (i, j) = (0, l - 1);
        while (i < j)
        {
            if (digits[i] != digits[j])
            {
                return false;
            }

            i += 1;
            j -= 1;
        }

        return true;
    }
}