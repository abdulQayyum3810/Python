class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum==target:
                    sol=[i,j]
                    return sol
                
out=Solution()
print(out.twoSum([2,7,11,15],9))
