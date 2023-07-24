class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        arith = []
        i = 0
        j = 0
        y = False
        while i < len(l):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            z = temp[1] - temp[0]
            k = 0
            while k < len(temp)-1:
                if temp[k+1] - temp[k] != z:
                    y = False
                    break
                else: 
                    y = True
                    k += 1
            arith.append(y)
            i += 1
        return arith