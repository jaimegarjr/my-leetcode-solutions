class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.COLS, self.ROWS = width, height
        self.snakePoints = collections.deque([[0, 0]])
        self.food = food
        self.score = 0
        self.directions = {
            'R': [0, 1],
            'L': [0, -1],
            'U': [-1, 0],
            'D': [1, 0]
        }

    def move(self, direction: str) -> int:
        dr, dc = self.snakePoints[0]
        nr, nc = self.directions[direction]
        newHead = [dr + nr, dc + nc]
        
        if (dr + nr >= self.ROWS or
            dr + nr < 0 or
            dc + nc >= self.COLS or 
            dc + nc < 0):
            return -1
        
        if newHead in self.snakePoints:
            if self.snakePoints[-1] != newHead:
                return -1
        
        self.snakePoints.appendleft(newHead)
        if (self.food and newHead == self.food[0]):
            self.food.pop(0)
            self.score += 1
        else:
            self.snakePoints.pop()

        return self.score
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)