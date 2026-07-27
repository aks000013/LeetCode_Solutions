class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left_sum=0
        for i in range(len(nums)):
            num=nums[i]

            right_sum = total_sum - left_sum - num
            
            if left_sum == right_sum:
                return i
            left_sum +=num
        return -1