class Logger:

    def __init__(self):
        self.logs = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Runtime: O(1)
        Space: O(n)
        """
        if message not in self.logs:
            self.logs[message] = timestamp
            return True
        else:
            time = self.logs[message] + 10
            if timestamp >= time:
                self.logs[message] = timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)