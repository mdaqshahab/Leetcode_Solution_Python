# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(self, nums: List[int]) -> List[int]:
    l = len(nums)
    prefixProductFromStart = [1]*l
    prefixProductFromEnd = [1]*l
    result = [1]*l

    prefixProductFromStart[0] = nums[0]
    for i in range(1,l):
        prefixProductFromStart[i] = prefixProductFromStart[i-1] * nums[i]
    
    prefixProductFromEnd[-1] = nums[-1]
    for i in range(l-2,0,-1):
        prefixProductFromEnd[i] = prefixProductFromEnd[i+1] * nums[i]

    result[0] = prefixProductFromEnd[1]
    result[-1] = prefixProductFromStart[-2]
    for i in range(1,l-1):
        result[i] = prefixProductFromStart[i-1] * prefixProductFromEnd[i+1]
    
    return result
