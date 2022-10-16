class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.COLS = width
        self.ROWS = height
        self.food = food[1:]
        self.curSnakePos = [0, 0]
        self.curFoodPos = food[0]
        self.snakeLen = 1
        self.score = 0
        self.snakeBodyPoints = collections.deque([[0, 0]])
        self.directions = {
            'R': [0, 1],
            'L': [0, -1],
            'U': [-1, 0],
            'D': [1, 0]
        }

    def move(self, direction: str) -> int:
        dr, dc = self.snakeBodyPoints[0]
        nr, nc = self.directions[direction]
        newHead = [dr + nr, dc + nc]
        
        if newHead in self.snakeBodyPoints:
            if self.snakeBodyPoints[-1] != newHead:
                return -1
        
        if (dr + nr < self.ROWS and
            dr + nr >= 0 and
            dc + nc < self.COLS and 
            dc + nc >= 0):
            self.curSnakePos = [dr + nr, dc + nc]
            self.snakeBodyPoints.appendleft(self.curSnakePos)
            
            if (self.curSnakePos == self.curFoodPos):
                self.snakeLen += 1
                self.score += 1
                self.curFoodPos = self.food[0] if self.food else [-1, -1]
                self.food = self.food[1:]
            
            if self.snakeLen != len(self.snakeBodyPoints):
                self.snakeBodyPoints.pop()
            
            return self.score
        else:
            return -1
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)