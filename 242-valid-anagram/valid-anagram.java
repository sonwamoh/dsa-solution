class Solution {
    public boolean isAnagram(String s, String t) {
        int[] sCount = new int[26];
        int[] tCount = new int[26];
        char[] s_arr = s.toCharArray();
        char[] t_arr = t.toCharArray();
        if(s.length() != t.length()){
            return false;
        }
        for(int i = 0; i < s.length(); i ++){
            sCount[s_arr[i] - 'a']++;
            tCount[t_arr[i] - 'a']++;
        }
        for(int i = 0; i < sCount.length; i ++){
            if(sCount[i] != tCount[i]){
                return false;
            }
        }
        return true;
    }
}