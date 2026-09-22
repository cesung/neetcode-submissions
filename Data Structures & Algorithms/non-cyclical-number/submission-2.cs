public class Solution {
    public bool Check(int v, HashSet<int> vis)
    {
        if (v == 1)
        {
            return true;
        }

        if (vis.Contains(v))
        {
            return false;
        }
        vis.Add(v);

        int t = 0;
        while (v > 0)
        {
            t += (int)Math.Pow((v % 10), 2);
            v /= 10;
        }

        return Check(t, vis);
    }

    public bool IsHappy(int n) {
        var vis = new HashSet<int>();
        return Check(n, vis);
    }
}
