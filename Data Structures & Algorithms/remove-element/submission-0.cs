public class Solution {
    public int RemoveElement(int[] nums, int val) {
        var size = nums.Length;
        var left = 0;

        for (int right = 0; right < size; right++)
        {
            if (nums[right] != val)
            {
                (nums[left], nums[right]) = (nums[right], nums[left]);
                left += 1;
            }
        }

        return left;
    }
}