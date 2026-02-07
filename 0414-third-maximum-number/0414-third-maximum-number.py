class Solution(object):
    def thirdMax(self, nums):
        nums = list(nums)   # avoid modifying input list

        first = max(nums)
        nums = [x for x in nums if x != first]

        if not nums:
            return first

        second = max(nums)
        nums = [x for x in nums if x != second]

        if not nums:
            return first

        third = max(nums)
        return third
