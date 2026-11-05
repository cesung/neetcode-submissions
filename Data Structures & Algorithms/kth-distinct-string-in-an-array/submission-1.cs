public class Solution {
    public string KthDistinct(string[] arr, int k) {
        var cntr = new Dictionary<string, int>();

        foreach (var s in arr)
        {
            cntr[s] = cntr.TryGetValue(s, out var cnt) ? cnt + 1 : 1;
        }

        int c = 0;
        foreach (var s in arr)
        {
            if (cntr[s] == 1)
            {
                c += 1;
            }

            if (c == k)
            {
                return s;
            }
        }

        return string.Empty;
    }
}