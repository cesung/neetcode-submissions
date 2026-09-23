public class Solution {
    public void ReverseString(char[] s) {
        var size = s.Length;
        var (left, right) = (0, size - 1);

        while (left < right)
        {
            (s[left], s[right]) = (s[right], s[left]);
            left += 1;
            right -= 1;
        }
    }
}