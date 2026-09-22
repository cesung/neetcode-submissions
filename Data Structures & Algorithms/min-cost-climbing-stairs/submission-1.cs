public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        var size = cost.Length;
        var min_cost = new int[size + 1];

        for (int i = 2; i < size + 1; i++)
        {
            min_cost[i] = Math.Min(
                min_cost[i - 1] + cost[i - 1],
                min_cost[i - 2] + cost[i - 2]
            );
        }

        return min_cost[^1];
    }
}
