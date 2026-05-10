class Solution {
    public int longestConsecutive(int[] nums) {
        //first set create pananum
        Set<Integer> set = new HashSet<>();

        //add the all elements into set

        for(int n:nums)
        set.add(n);

        int max = 0;
        for(int i=0; i<nums.length; i++)
        {
            int num = nums[i];
            if(set.contains(num - 1)) continue;

            int current_len = 0;
            while(set.contains(num))
            {
                current_len+=1;
                num+=1;
            }

            max = Math.max(max,current_len);
        }

        return max;
    }
}
