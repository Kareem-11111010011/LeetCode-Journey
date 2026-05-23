class Solution {
    public boolean isPalindrome(int x) {
        int reverse = 0;
        int xCopy = x;

        while (x > 0) {
            reverse = (reverse * 10) + (x % 10); // get the last int and multiply it by 10. Then add the ints to the last int in reverse
            x /= 10; // move backwards from digit to digit omiting the last digit due to decimal truncation
        }
        
        return reverse == xCopy;
    }
}
