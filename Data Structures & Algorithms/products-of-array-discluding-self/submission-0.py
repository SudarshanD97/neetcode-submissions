class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        pre=[]
        for i in range(len(nums)):
            pre.append(prefix)
            prefix*=nums[i]

        postfix=1
        post=[]

        for i in range(len(nums)-1, -1 , -1):
            post.append(postfix)
            postfix*=nums[i]
        
        res=[1]*len(nums)

        for i in range(len(nums)):
            res[i]=pre[i]*post[(len(nums)-1)-i]
        return res
        