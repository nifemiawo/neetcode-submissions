class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left =0;
        int right =0;
        int maxLength =0;
        Set<Character> unique = new HashSet<>();

        while (right < s.length()){
            if(!unique.contains(s.charAt(right))){
                unique.add(s.charAt(right));
                maxLength = Math.max(maxLength,right-left+1);
                right++;
            }else{
                unique.remove(s.charAt(left));
                left++;
            }

        }
        return maxLength;

    }
}
