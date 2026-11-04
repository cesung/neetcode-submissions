public class Solution {
    public int MaxLengthBetweenEqualCharacters(string s) {
        int[] lastPos = new int[26];
        Array.Fill(lastPos, -1);

        int ret = -1;
        for (int i = 0; i < s.Length; i++)
        {
            var c = s[i];
            if (lastPos[c - 'a'] == -1)
            {
                lastPos[c - 'a'] = i;
            }

            ret = Math.Max(
                ret,
                i - lastPos[c - 'a'] - 1
            );
        }

        return ret;
    }
}