class Solution {
    public int[] twoSum(int[] numbers, int target) {
       int left =0;
       int last =numbers.length-1;

        while (left < last){
        int total = numbers[left] + numbers[last];

        if (total == target ){
            return new int[]{left+1, last+1};

        } else if (total < target){
            left++;
        } else if (total>target){
            last--;
        }
        }
       return null;
       }
   
}
