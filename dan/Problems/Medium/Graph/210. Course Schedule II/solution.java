class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Queue<Integer> queue = new LinkedList<>();
        int[][] graph = new int[numCourses][numCourses];
        int[] indegree = new int[numCourses];
        int[] res = new int[numCourses];
        int cnt = 0;
        for(int i = 0; i < prerequisites.length; i++){
            int pre = prerequisites[i][1];
            int lat = prerequisites[i][0];
            graph[pre][lat] = 1;
            indegree[lat]++;
        }
        for(int i = 0; i < numCourses; i++){
            if(indegree[i] == 0){
                queue.offer(i);
            }
        }
        while(!queue.isEmpty()){
            int course = queue.poll();
            res[cnt++] = course;
            for(int j = 0; j < numCourses; j++){
                if(graph[course][j] == 1){
                    indegree[j]--;
                    if(indegree[j] == 0){
                        queue.offer(j);
                    }
                }
            }
        }
        return (cnt == numCourses)?res:new int[0]; 
    }
}
