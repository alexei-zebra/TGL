import random
from color import color
class RandomColor():
    def __init__(self, screen_array):
        self.screen_array = screen_array

    def randomColor(self):
        return color(random.randint(0, 2), random.randint(0, 2), random.randint(0, 2))

    def randomColorFill(self, x, y, x2, y2,types='two_ang'):
        if types == 'two_ang':
            for i in range(x2-x):
                for j in range(y2-y):
                    self.screen_array[i+x][j+y] = self.randomColor()
        if types == 'one_ang':
            for i in range(x2):
                for j in range(y2):
                    self.screen_array[i+x][j+y] = self.randomColor()

    def randomOneColorFill(self, x, y, x2, y2,types='two_ang'):
        random_color = self.randomColor()
        if types == 'two_ang':
            for i in range(x2-x):
                for j in range(y2-y):
                    self.screen_array[i+x][j+y] = random_color
        if types == 'one_ang':
            for i in range(x2):
                for j in range(y2):
                    self.screen_array[i+x][j+y] = random_color