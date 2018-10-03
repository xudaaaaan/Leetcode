class Solution {
    //Recursive
    public int searchInsert1(int[] nums, int target) {
        if(nums.length == 0)
            return 0;
        else
            return binarySearch(nums, target, 0, nums.length - 1);
    }
    
    public int binarySearch(int[] nums, int target, int begin, int end){
        if(begin == end){
            return (nums[begin] < target)? begin + 1 : begin;
        }else if(begin > end){
            return begin;
        }else{
            int mid = begin + (end - begin) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < target)
                return binarySearch(nums, target, mid + 1, end);
            else
                return binarySearch(nums, target, begin, mid - 1);
        }       
    }
    //Iterative
    public int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        while (low <= high){
            int mid = low + (high - low) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < target)
                low++;
            else
                high--;
        }
        return low;
    }
        
}
