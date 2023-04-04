class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mar = [0] * len(nums)
        z =0
        for i in range (len(nums)):
            nums[i] = [i,nums[i]]
        nums.sort(key =lambda x:x[1])
        prievious = nums[0][1]
        for i in range (1,len(nums)):
            if prievious == nums[i][1]:
                mar[nums[i][0]] = z
            else:
                z = i
                mar[nums[i][0]] = z
            prievious = nums[i][1]

        return (mar)
