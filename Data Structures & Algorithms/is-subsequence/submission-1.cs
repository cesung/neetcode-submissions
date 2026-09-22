public class Solution {
    public bool IsSubsequence(string s, string t) {
        var sLen = s.Length; var tLen = t.Length;

        var j = 0;
        for (var i = 0; i < tLen; i++)
        {
            if (j < sLen && t[i] == s[j])
            {
                j += 1;
            }
        }

        return j == s.Length;
    }
}