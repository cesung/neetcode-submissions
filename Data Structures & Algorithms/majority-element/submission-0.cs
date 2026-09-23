public class Solution {
    public int MajorityElement(int[] nums) {
        nums = nums.Order().ToArray();
        return nums[nums.Length/2];
    }
}