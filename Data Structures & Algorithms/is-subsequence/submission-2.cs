public class Solution {
    public bool IsSubsequence(string s, string t) {
        Dictionary<char, List<int>> rcd = new();
        foreach (var (ch, idx) in t.Select((ch, idx) => (ch, idx)))
        {
            if (!rcd.TryGetValue(ch, out var _))
            {
                rcd[ch] = new List<int>();
            }
            rcd[ch].Add(idx);
        }

        int check(char c, int idx)
        {
            if (rcd.TryGetValue(c, out var idxs) == false)
            {
                return -1;
            }
            
            var left = 0; var right = idxs.Count - 1;
            while (left < right)
            {
                var mid = (left + right) / 2;
                if (idxs[mid] < idx)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid;
                }
            }

            if (idxs[left] < idx)
            {
                return -1;
            }

            return idxs[left];
        }

        var cur = 0;
        for (int i = 0; i < s.Length; i++)
        {
            var nxt = check(s[i], cur);
            if (nxt == -1)
            {
                return false;
            }

            cur = nxt + 1;
        }

        return true;
    }
}