public class Solution {
    public int CountSeniors(string[] details) {
        var res = 0;
        foreach (var d in details)
        {
            if (int.TryParse(d[^4..^2], out var age))
            {
                if (age > 60)
                {
                    res += 1;
                }
            }
        }

        return res;
    }
}