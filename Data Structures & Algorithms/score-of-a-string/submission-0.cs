public class Solution {
    public int ScoreOfString(string s) {
        var size = s.Length;

        var score = 0;
        for (int i = 1; i < size; i++)
        {
            score += Math.Abs((int)s[i] - (int)s[i - 1]);
        }

        return score;
    }
}