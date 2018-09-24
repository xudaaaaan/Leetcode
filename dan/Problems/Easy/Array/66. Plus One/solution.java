class Solution {
    public int[] plusOne(int[] digits) {
        int flag = 0;
        for(int i = digits.length - 1; i >= 0; --i){
            if(digits[i] < 9){
                digits[i]++;
                flag = 1;
                break;
            }else{
                digits[i] = 0;
            }
        }
        int[] list = new int[digits.length + 1];
        list[0] = 1;
        return (flag == 1)?digits:list;
        
    }
}
