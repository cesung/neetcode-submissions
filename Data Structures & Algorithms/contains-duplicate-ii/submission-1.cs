public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        var vis = new HashSet<int>();

        for (int i = 0; i <= k && i < nums.Length; i++)
        {
            if (vis.Contains(nums[i]))
            {
                return true;
            }
            vis.Add(nums[i]);
        }

        for (int i = k + 1; i < nums.Length; i++)
        {
            vis.Remove(nums[i - k - 1]);
            if (vis.Contains(nums[i]))
            {
                return true;
            }

            vis.Add(nums[i]);
        }

        return false;
    }
}