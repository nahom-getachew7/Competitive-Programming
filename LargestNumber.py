class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a,b):
            if int(b + a) > int(a + b):
                return 1
            else:
                return 0
        nums.sort(reverse=True)
        nums = list(map(str,nums))
        if nums[0] == '0':
            return '0'
        for i in range (len(nums)-1):
            j=i
            while j>= 0:
                if comp(nums[j], nums[j+1]):
                    nums[j],nums[j+1] = nums[j+1], nums[j]
                    j -= 1
                else:
                    break
        return ''.join(nums)