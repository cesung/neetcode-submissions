public class Solution {
    public int MajorityElement(int[] nums) {
        var cntr = new Dictionary<int, int>();
        var maxCnt = 0;
        var majEle = -1;

        foreach (var num in nums)
        {
            if (!cntr.TryGetValue(num, out var _))
            {
                cntr[num] = 0;
            }
            cntr[num] += 1;

            if (cntr[num] > maxCnt)
            {
                maxCnt = cntr[num];
                majEle = num;
            }
        }

        return majEle;
    }
}