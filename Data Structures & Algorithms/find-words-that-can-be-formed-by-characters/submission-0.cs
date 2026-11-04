public class Solution {
    public int CountCharacters(string[] words, string chars) {
        Dictionary<char, int> GetStrCntr(string s)
        {
            return s.GroupBy(c => c).ToDictionary(g => g.Key, g => g.Count());
        }

        var charsCntr = GetStrCntr(chars);

        int ret = 0;
        foreach (var word in words)
        {
            var suc = true;
            var wordCntr = GetStrCntr(word);
            foreach (var (k, v) in wordCntr)
            {
                if (!charsCntr.TryGetValue(k, out var o) || o < v)
                {
                    suc = false;
                }
            }

            if (suc == true)
            {
                ret += word.Length;
            }
        }

        return ret;
    }
}