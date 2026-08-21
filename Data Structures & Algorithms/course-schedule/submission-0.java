class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Queue<Integer> queue = new LinkedList<>();
        List<List<Integer>> graph = new ArrayList<>();
        int[] inDegree = new int[numCourses];

        for (int i=0; i<numCourses;i++){
            graph.add(new ArrayList<>());
        }

        for (int[] pre : prerequisites){
            int from = pre[1];
            int to = pre[0];
            graph.get(from).add(to);
            inDegree[to]++;

        }

        for (int i=0; i< numCourses; i++){
            if (inDegree[i] == 0){
                queue.offer(i);
            }
        }
        int index=0;
        while (!queue.isEmpty()){
            int course = queue.poll();
            index++;

            for (int neighbour : graph.get(course)){
                inDegree[neighbour]--;
                if (inDegree[neighbour] ==0){
                    queue.offer(neighbour);
                }

            }


        }
        return index == numCourses;
    }
}
