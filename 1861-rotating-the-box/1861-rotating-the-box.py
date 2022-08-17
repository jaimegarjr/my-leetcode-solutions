class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(box), len(box[0])
        rotatedBox = []
        
        # falling
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if box[r][c] == ".":
                    travColumn = c - 1
                    while box[r][travColumn] == "." and travColumn >= 0: # shift
                        travColumn -= 1
                    
                    if box[r][travColumn] == "*" or travColumn < 0:
                        continue
                    else:
                        box[r][c] = "#"
                        print(travColumn)
                        box[r][travColumn] = "."
        
        # rotation
        for i in range(COLS):
            newRow = []
            for j in range(ROWS-1, -1, -1):
                newRow.append(box[j][i])
            rotatedBox.append(newRow)
        
        return rotatedBox