class Solution {
    public boolean isAnagram(String s, String t) {
        int len = s.length();
        int len_2 = t.length();
        if(len != len_2)
        {
            return false;
        }
        int countarr[] = new int[26];

        for(int i=0; i<len; i++)
        {
            countarr[s.charAt(i) - 'a']++;
            countarr[t.charAt(i) - 'a']--;
        }

        for(int count: countarr)
        {
            if(count != 0)
            {
                return false;
            }
        }

        return true;

    }
}
