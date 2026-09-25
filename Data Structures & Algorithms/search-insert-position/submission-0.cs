public class Solution {
    public int SearchInsert(int[] nums, int target) {
        var size = nums.Length;
        int left = 0, right = size - 1;

        while (left < right)
        {
            var mid = left + (right - left) / 2;
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }

        return nums[left] < target ? left + 1 : left;
    }
}