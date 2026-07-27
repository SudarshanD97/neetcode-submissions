class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                ele=nums[i]
                cnt=1
            elif ele == nums[i]:
                cnt+=1
            else:
                cnt-=1

        return ele

        