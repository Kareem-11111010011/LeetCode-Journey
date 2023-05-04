class Solution {
    HashMap<Integer, Integer> hm = new HashMap<>();

    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (hm.containsKey(target - nums[i])) 
                return new int[]{hm.get(target - nums[i]), i};
            hm.put(nums[i], i);
        }
        return new int[]{0,0};
    }
}
