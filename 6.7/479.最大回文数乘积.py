public class Solution {
    public int largestPalindrome(int n) {
        if (n == 1) {
            return 9;
        }

        int high = (int) Math.pow(10, n) - 1, low = high / 10;

        for (int i = high; i > low; i--) {
            long palindrome = createPalindrome(i);

            for (long j = high; j > low; j--) {
                if (palindrome / j > high) {
                    break;
                }
                if (palindrome % j == 0) {
                    return (int) (palindrome % 1337);
                }
            }
        }
        return -1;
    }

    private long createPalindrome(long num) {
        String str = num + new StringBuilder(Long.toString(num)).reverse().toString();
        return Long.parseLong(str);
    }
}