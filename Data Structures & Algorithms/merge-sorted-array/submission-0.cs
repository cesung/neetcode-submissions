public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        for (var i = m + n - 1; i >= n; i--)
        {
            (nums1[i], nums1[i - n]) = (nums1[i - n], nums1[i]);
        }

        var (ptr1, ptr2) = (n, 0);

        var j = 0;
        while (ptr1 < m+n && ptr2 < n)
        {
            if (nums1[ptr1] < nums2[ptr2])
            {
                nums1[j] = nums1[ptr1];
                ptr1 += 1;
            }
            else
            {
                nums1[j] = nums2[ptr2];
                ptr2 += 1;
            }

            j += 1;
        }

        while (ptr1 < m+n)
        {
            nums1[j] = nums1[ptr1];
            ptr1 += 1;
            j += 1;
        }

        while (ptr2 < n)
        {
            nums1[j] = nums2[ptr2];
            ptr2 += 1;
            j += 1;
        }
    }
}