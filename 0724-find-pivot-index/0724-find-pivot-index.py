class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left_sum=0
        for i in range(len(nums)):
            num=nums[i]

            if left_sum ==(total_sum-left_sum-num):
                return i

            left_sum += num
        return -1
