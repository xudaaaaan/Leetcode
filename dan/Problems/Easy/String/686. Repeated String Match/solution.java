class Solution {
   
    
    //Most clear way
    public int repeatedStringMatch(String A, String B){
        String as = A;
        for (int cnt = 1; cnt <= (B.length()/A.length() + 2); cnt++, as += A)
            if (as.indexOf(B) != -1) return cnt;
        return -1;
    }
}
