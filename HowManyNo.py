class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mar = []
        z = 0
        for x in nums:
            for y in nums:
                if x > y:
                    z+=1
            mar.append(z)
            z =0
        return mar