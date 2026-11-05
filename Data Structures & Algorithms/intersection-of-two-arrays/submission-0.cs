public class Solution {
    public int[] Intersection(int[] nums1, int[] nums2) {
        var nums1Set = new HashSet<int>();
        var nums2Set = new HashSet<int>();

        foreach (var num in nums1)
        {
            nums1Set.Add(num);
        }
        foreach (var num in nums2)
        {
            nums2Set.Add(num);
        }

        var res = new HashSet<int>();
        foreach (var num in nums1Set)
        {
            if (nums2Set.Contains(num))
            {
                res.Add(num);
            }
        }
        foreach (var num in nums2Set)
        {
            if (nums1Set.Contains(num))
            {
                res.Add(num);
            }
        }

        return res.ToArray();
    }
}