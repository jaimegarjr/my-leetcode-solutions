class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        binLen = len(nums)
        combs = 2 ** binLen
        for i in range(combs-1, -1, -1):
            binStr = bin(i)[2:]  # removing 0b notation

            # find extra zeros for bit length
            if len(binStr) != binLen:
                neededZeros = binLen - len(binStr)
                for _ in range(neededZeros):
                    binStr = '0' + binStr

            if binStr in nums:
                continue
            else:
                return binStr