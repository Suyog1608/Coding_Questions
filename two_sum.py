class Solution(object):
    def two_sum(self, nums, target):
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i


input_list = [2, 8, 12, 15]
ob1 = Solution()
print(ob1.two_sum(input_list, 20))
