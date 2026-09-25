/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution : GuessGame {
    public int GuessNumber(int n) {
        int left = 0, right = n;

        while (left < right)
        {
            var mid = left + (right - left) / 2 + 1;
            if (guess(mid) == -1)
            {
                right = mid - 1;
            }
            else
            {
                left = mid;
            }
        }

        return left;
    }
}