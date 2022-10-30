class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] soln = {0,0};
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target && (i != j)) {
                    soln[0] = i; 
                    soln[1] = j;
                    break;
                }
            }
        }
        return soln;
    }
}
