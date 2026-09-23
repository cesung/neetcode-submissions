public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        var size = strs.Length;
        var minLength = strs.Min(s => s.Length);

        bool Check(int j)
        {
            var ch = strs[0][j];
            for (int i = 1; i < size; i++)
            {
                if (strs[i][j] != ch)
                {
                    return false;
                }
            }

            return true;
        }

        for (int j = 0; j < minLength; j++)
        {
            if (!Check(j))
            {
                return strs[0][0..j];
            }
        }

        return strs[0][0..minLength];
    }
}