class Solution {
    public String decodeString(String s) {
        Stack<Integer> repStack = new Stack<>();
        Stack<String> resStack = new Stack<>();
        resStack.push("");
        String res = "";
        int idx = 0;
        while(idx < s.length()){
            if(Character.isDigit(s.charAt(idx))){
                int num = 0;
                while(Character.isDigit(s.charAt(idx))){
                    num = num * 10 + (s.charAt(idx) - '0');
                    idx++;
                }
                repStack.push(num);
            }else if(s.charAt(idx) == '['){
                resStack.push(res);
                res = "";
                idx++;
            }else if(s.charAt(idx) == ']'){
                StringBuilder sb = new StringBuilder();
                sb.append(resStack.pop());
                int times = repStack.pop();
                for(int k = 0; k < times; k++){
                    sb.append(res);
                }
                res = sb.toString();
                idx++;
            }else{
                res += s.charAt(idx);
                idx++;
            }      
        }
        return res;     
    }
}
