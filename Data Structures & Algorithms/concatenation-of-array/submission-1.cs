public class Solution {
    public int[] GetConcatenation(int[] nums) {
        var size = nums.Length;
        var ret = new int[size * 2];

        for (int i = 0; i < size; i++)
        {
            ret[i] = ret[i + size] = nums[i];
        }

        return ret;
    }
}