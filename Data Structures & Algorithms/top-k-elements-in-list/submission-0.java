class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        PriorityQueue<Map.Entry<Integer,Integer>> maxHeap = new PriorityQueue<>((a,b) -> b.getValue() - a.getValue());

        for (int i =0; i<nums.length; i++){
            freqMap.put(nums[i], freqMap.getOrDefault(nums[i],0)+1);
        }

        for (Map.Entry<Integer,Integer> entry : freqMap.entrySet()){
            maxHeap.offer(entry);
        }
        int[] res = new int[k];
        for (int i =0; i<k; i++){
          res[i] =  maxHeap.poll().getKey();
        }
        return res;


    }
}