public class Solution {
    public int LengthOfLastWord(string s) {
        var parts = s.Split(' ').Where(p => p != string.Empty);
        return parts.Last().Length;
    }
}