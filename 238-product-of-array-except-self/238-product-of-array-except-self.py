class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        res = [0] * len(nums)
        pre, post = 1, 1

        for i in range(len(nums)):
            pre *= nums[i]
            prefix[i] = pre

        for i in range(len(nums)-1, -1, -1):
            post *= nums[i]
            postfix[i] = post

        for i in range(len(nums)):
            if i == 0:
                res[i] = 1 * postfix[i + 1]
            elif i == len(nums)-1:
                res[i] = prefix[i - 1] * 1
            else:
                res[i] = prefix[i - 1] * postfix[i + 1]

        return res