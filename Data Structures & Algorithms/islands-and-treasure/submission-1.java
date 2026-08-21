class Solution {
    public void islandsAndTreasure(int[][] grid) {
        Queue<int[]> queue = new LinkedList<>();
        final int INF = 2147483647 ;

        for (int i =0; i< grid.length; i++){
            for (int j=0; j < grid[0].length; j++){
                if (grid[i][j] == 0){
                    queue.add(new int[]{i,j});
                }
            }
        }

        int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        while (!queue.isEmpty()){
            int[] cell = queue.poll();
            int r = cell[0];
            int c = cell[1];

            for (int[] dir : dirs){
                int nr = r + dir[0];
            int nc = c + dir[1];

            if (nr >=0 && nr < grid.length && nc>=0 && nc < grid[0].length && grid[nr][nc] == INF){
                grid[nr][nc] = grid[r][c] +1;
                queue.add(new int[] {nr,nc});
            }
            }
            
        }
    }
}
