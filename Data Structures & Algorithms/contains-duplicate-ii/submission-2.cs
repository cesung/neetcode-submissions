public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        var size = nums.Length;
        if (size == 1 || k == 0)
        {
            return false;
        }

        var vis = new HashSet<int>();

        var l = 0;
        for (int r = 0; r < size; r++)
        {
            if (vis.Contains(nums[r]))
            {
                return true;
            }
            vis.Add(nums[r]);

            if (r - l == k)
            {
                vis.Remove(nums[l++]);
            }
        }

        return false;

    }
}