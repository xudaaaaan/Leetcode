class Solution {
    public int search(int[] nums, int target) {
        int begin = 0;
        int end = nums.length - 1;
        while(begin <= end){
            int mid = begin + (end - begin) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[begin] <= nums[mid]){
                if(nums[begin] <= target && target < nums[mid])
                    end = mid - 1;
                else
                    begin = mid + 1;
            }else{
                if(nums[mid] < target && target <= nums[end])
                    begin = mid + 1;
                else
                    end = mid - 1;
            }
        }
        return -1;
    }
}
