public class Solution {
    public int[] PlusOne(int[] digits) {
        int size = digits.Length;

        for (int i = size - 1; i >= 0; i--)
        {
            if (digits[i] != 9)
            {
                digits[i] += 1;
                return digits;
            }
            digits[i] = 0;
        }

        digits = new int[size + 1];
        digits[0] = 1;
        return digits;
    }
}
