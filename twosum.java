import java.util.*;

class twosum{
    public int[] twoS(int[] nums, int target) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            m.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int c = target - nums[i];
            if (m.containsKey(c) && m.get(c) != i) {
                return new int[] { i, m.get(c) };
            }
        }
        
        return null;
        
    }
}
//TC reduced from n^2 to n