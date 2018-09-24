class Solution {
    StringBuilder res = new StringBuilder();
    Set<String> set = new HashSet<>();
    
    public String crackSafe(int n, int k) {
        StringBuilder sb = new StringBuilder();
        for(int i = 1; i < n; i++){
            sb.append("0");
        }
        dfs(sb.toString(), k);
        for(int i = 1; i < n; i++){
            res.append("0");
        }
        return res.toString();
        
    }
    
    public void dfs(String node,int k){
        for(int i = 0; i < k; i++){
            String psw = node.concat(String.valueOf(i));
            if(!set.contains(psw)){
                set.add(psw);
                dfs(psw.substring(1), k);
                res.append(i);
            }
        }
    }
}
