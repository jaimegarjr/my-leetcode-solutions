class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Runtime: O(n)
        Space: O(1)
        Encodes a list of strings to a single string.
        """
        
        return ''.join(str(len(word)) + '-' + word for word in strs)
        
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "-":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))