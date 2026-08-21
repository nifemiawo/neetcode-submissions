class Solution {
     int[] parent;
    public int countComponents(int n, int[][] edges) {
        int count = n;

         parent = new int[n];

         for (int i =0; i<n; i++){
            parent[i] = i;
         }
        for (int[] edge : edges){
            int x = edge[0];
            int y = edge[1];

            if (find(x) != find(y)){
                union(x,y);
                count--;
            }
        }
        return count;


    }

    private int find(int x){
        if (parent[x] !=x){
            parent[x] = find(parent[x]);
        }

        return parent[x];
    }

    private void union(int x, int y){
        int rootX = find(x);
        int rootY = find(y);

        parent[rootX] = rootY;
    }
}
