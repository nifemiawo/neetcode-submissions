class Solution {
    public boolean isPalindrome(String s) {
        String fixedString = "";

        for (char c : s.toCharArray()){
            if(Character.isDigit(c) || Character.isLetter(c)){
                fixedString+=c;
            }
        }
        int right =fixedString.length()-1;
        int left =0;
        fixedString = fixedString.toLowerCase();

        while (left <= right){
            if (fixedString.charAt(left) != fixedString.charAt(right)){
                return false;
            }
            left++;
            right--;

        }
        return true;
    }
}
