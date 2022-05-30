class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for word in strs:
            for c in word:
                res += c
            res += chr(257)
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        string = ""
        for c in s:
            if c == chr(257):
                res.append(string)
                string = ""
            else:
                string += c
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))