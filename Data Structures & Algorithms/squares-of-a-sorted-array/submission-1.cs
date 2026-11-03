public class Solution {
    public int[] SortedSquares(int[] nums) {
        var minAbsIdx = nums.Select((val, idx) => idx).MinBy(idx => Math.Abs(nums[idx]));
        var size = nums.Length;
        var (left, right) = (minAbsIdx, minAbsIdx + 1);
        var result = new List<int>();

        while (left >= 0 && right < size)
        {
            var leftPow = nums[left] * nums[left];
            var rightPow = nums[right] * nums[right];
            if (leftPow > rightPow)
            {
                result.Add(rightPow);
                right += 1;
            }
            else
            {
                result.Add(leftPow);
                left -= 1;
            }
        }

        while (left >= 0)
        {
            var leftPow = nums[left] * nums[left];
            result.Add(leftPow);
            left -= 1;
        }

        while (right < size)
        {
            var rightPow = nums[right] * nums[right];
            result.Add(rightPow);
            right += 1;
        }

        return result.ToArray();
    }
}