class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        Sorts a list of given logs.
        logs: list
        """
        digitLogs, letterLogs = [], []

        for l in logs:
            log = l.split()
            if log[1].isdigit():
                digitLogs.append(l)
            else:
                letterLogs.append(l)

        letterLogs.sort(key=lambda x: x.split()[0])

        letterLogs.sort(key=lambda x: x.split()[1:])
        return letterLogs + digitLogs