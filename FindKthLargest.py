class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range (len(nums)):
            nums[i] = int(nums[i])
        nums.sort(key= lambda x:x, reverse= True)
        mar = str(nums[k-1])
        return mar