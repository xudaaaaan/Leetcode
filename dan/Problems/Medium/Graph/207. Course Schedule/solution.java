class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Stack<Integer> stack = new Stack<Integer>();
        int[][] graph = new int[numCourses][numCourses];
        int[] indegree = new int[numCourses];
        int cnt = 0;
        for(int i = 0; i < prerequisites.length; i++){
            int pre = prerequisites[i][1];
            int lat = prerequisites[i][0];
            graph[pre][lat] = 1;
            indegree[lat]++;
        }
        for(int i = 0; i < numCourses; i++){
            if(indegree[i] == 0){
                stack.push(i);
            }
        }
        while(!stack.isEmpty()){
            int course = stack.pop();
            cnt++;
            for(int i = 0; i < numCourses; i++){
                if(graph[course][i] == 1){
                    indegree[i]--;
                    if(indegree[i] == 0){
                        stack.push(i);
                    }
                }
            }
        }
        return cnt == numCourses;
    }
}
