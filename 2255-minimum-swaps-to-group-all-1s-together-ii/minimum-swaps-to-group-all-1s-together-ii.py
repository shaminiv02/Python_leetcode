class Solution(object):
    def minSwaps(self, nums):
        ones = sum(nums)

        if ones <= 1:
            return 0

        nums = nums + nums

        curr = sum(nums[:ones])
        ans = ones - curr

        left = 0

        for right in range(ones, len(nums)):
            if nums[left] == 1:
                curr -= 1

            if nums[right] == 1:
                curr += 1

            ans = min(ans, ones - curr)

            left += 1

        return ans