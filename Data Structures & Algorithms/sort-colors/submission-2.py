class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=0
        left=0
        right=len(nums)-1

        while i<=right:
            if nums[i]==0:
                nums[i],nums[left]=nums[left],nums[i]
                left+=1
            if nums[i]==2:
                nums[right],nums[i]=nums[i],nums[right]
                i-=1
                right-=1
            i+=1

        


