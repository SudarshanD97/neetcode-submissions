class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
        
        nums.clear()
        for i in range(0,3):
            nums.extend(([i]*count[i]))