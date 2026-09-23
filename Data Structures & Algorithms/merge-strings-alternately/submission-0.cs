public class Solution {
    public string MergeAlternately(string word1, string word2) {
        var (size1, size2) = (word1.Length, word2.Length);
        var (ptr1, ptr2) = (0, 0);
        var res = new StringBuilder(size1 + size2);

        while (ptr1 < size1 && ptr2 < size2)
        {
            res.Append(word1[ptr1]);
            res.Append(word2[ptr2]);
            ptr1 += 1;
            ptr2 += 1;
        }

        if (ptr1 < size1)
        {
            res.Append(word1[ptr1..size1]);
        }
        if (ptr2 < size2)
        {
            res.Append(word2[ptr2..size2]);
        }

        return String.Join("", res);
    }
}