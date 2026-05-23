class Solution {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                System.out.println(i);
                nums[count++] = nums[i];
                System.out.println(Arrays.toString(nums));
            }
        }
        return count;
    }
}
