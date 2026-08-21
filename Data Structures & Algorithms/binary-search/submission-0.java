class Solution {
    public int search(int[] nums, int target) {
        int low =0;
        int high = nums.length -1;

        while (low <=high){
            int middlepos = (low+high)/2;
            int middleNumber = nums[middlepos];

            if (target == middleNumber){
                return middlepos;
            }

            if (target < middleNumber){
                high = middlepos-1;
            }else {
                low = middlepos+1;
            }

        }

        return -1;
    }
}
