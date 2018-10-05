class Solution {
    //Merge two lists and find the medium
    public double findMedianSortedArrays1(int[] nums1, int[] nums2) {
        int[] nums = new int[nums1.length + nums2.length];
        int i = 0; int j = 0;
        while(i < nums1.length || j < nums2.length){
            System.out.println("i = " + i +  ", j = " + j);
            if(i < nums1.length && j < nums2.length){
                if(nums1[i] <= nums2[j])
                    nums[i + j] = nums1[i++];
                else if(nums1[i] > nums2[j])
                    nums[i + j] = nums2[j++];
            }else if(i < nums1.length)
                nums[i + j] = nums1[i++];
            else
                nums[i + j] = nums2[j++];  
        }
        if((i + j) % 2 == 0)
            return (nums[(i + j) / 2] + nums[(i + j) / 2 - 1]) / 2.0;
        else
            return nums[(i + j) / 2];       
    }
    
    //Binary Search
    public double findMedianSortedArrays(int[] nums1, int[] nums2){
        
    }
    
}
