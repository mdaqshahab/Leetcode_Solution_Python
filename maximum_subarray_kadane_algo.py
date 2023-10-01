# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maxSubArray(self, nums: List[int]) -> int:
    s = 0
    maxi = nums[0]
    for i in nums:
        s+=i
        maxi = max(maxi,s)
        if s<0:
            s=0
    return maxi
