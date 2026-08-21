class Solution {
    public int search(int[] nums, int target) {
        int low =0;
        int high = nums.length -1;


        while (low <= high){
            int middle = (low + high)/2;
            int middleNum = nums[middle];

            if (target > middleNum){
                low = middle +1;

            } else if (target == middleNum){
                return middle;
            } else {
                high = middle - 1;
            }
        }
        return -1;
        }

      
    }

