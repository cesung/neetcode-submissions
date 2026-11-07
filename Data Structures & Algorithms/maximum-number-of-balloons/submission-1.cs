public class Solution {
    public int MaxNumberOfBalloons(string text) {
        var chCntr = new Dictionary<char, int>();

        foreach (var ch in text)
        {
            chCntr[ch] = (chCntr.TryGetValue(ch, out var count) ? count : 0) + 1;
        }

        var ballonCntr = new Dictionary<char, int>()
        {
            ['a'] = 1,
            ['b'] = 1,
            ['l'] = 2,
            ['o'] = 2,
            ['n'] = 1
        };

        var res = text.Length;
        foreach (var ch in new char[] {'b', 'a', 'l', 'o', 'n'})
        {
            res = Math.Min(
                res,
                chCntr.ContainsKey(ch) ? chCntr[ch] / ballonCntr[ch] : 0
            );
        }

        return res;
    }
}