public class Solution {
    public int[] ReplaceElements(int[] arr) {
        var size = arr.Length;
        var maxFromRight = -1;

        for (var i = size - 1; i >= 0; i--)
        {
            var tmp = Math.Max(
                maxFromRight,
                arr[i]
            );
            arr[i] = maxFromRight;
            maxFromRight = tmp;
        }

        return arr;
    }
}