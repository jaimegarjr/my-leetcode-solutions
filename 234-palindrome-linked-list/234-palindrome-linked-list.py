# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = head
        res = []
        while tmp:
            res.append(tmp.val)
            tmp = tmp.next
        
        return self.checkPalindrome(res)
        
    
    def checkPalindrome(self, nums):
        l, r = 0, len(nums) - 1
        
        while l < r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        
        return True