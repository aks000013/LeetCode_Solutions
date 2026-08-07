class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_st={}

        for i in range(len(nums)):
            num=nums[i]
            diff=target-num

            if diff in num_st:
                return [num_st[diff],i]
            num_st[num]=i