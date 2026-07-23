class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search=defaultdict(int)
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in search:
                return [search[diff],i]
            search[nums[i]]=i
        


        