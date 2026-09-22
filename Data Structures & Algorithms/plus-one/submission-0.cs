public class Solution {
    public int[] PlusOne(int[] digits) {
        var digitsList = digits.ToList();
        var done = false;

        for (int i = digitsList.Count() - 1; i >= 0; i -= 1)
        {
            if (digitsList[i] != 9) {
                digitsList[i] += 1;
                done = true;
                break;
            }
            else {
                digitsList[i] = 0;
            }
        }

        if (!done)
        {
            digitsList.Insert(0, 1);
        }

        return digitsList.ToArray();
    }
}
