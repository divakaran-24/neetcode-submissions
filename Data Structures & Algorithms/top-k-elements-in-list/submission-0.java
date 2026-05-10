class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        List<Integer>[] bucket = new List[nums.length+1];

        for( int n : nums)
        {
            map.put(n,map.getOrDefault(n,0)+1);
        }

        for(int key : map.keySet())
        {
            int fre = map.get(key);
            if(bucket[fre] == null)
            {
                bucket[fre] = new ArrayList<>();
            }
            bucket[fre].add(key);
        }

        int res[] = new int[k];
        int c=0;
        for(int i=bucket.length-1; i>=0 && c < k; i--)
        {
            if(bucket[i] != null)
            {
                for(Integer n : bucket[i])
                {
                    res[c++] = n;
                }
            }
        }

       
        return res;
    }
}
