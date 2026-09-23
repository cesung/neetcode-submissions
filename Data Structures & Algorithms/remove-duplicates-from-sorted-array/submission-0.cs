public class Solution {
    public int RemoveDuplicates(int[] nums) {
        var size = nums.Length;
        var nxt = 1;
        for (int i = 1; i < size; i++)
        {
            if (nums[i] != nums[nxt - 1])
            {
                (nums[i], nums[nxt]) = (nums[nxt], nums[i]);
                nxt += 1;
            }
        }
        return nxt;
    }
}