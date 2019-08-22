from game_object import Game_Object

class Hero_Shield(Game_Object):
    def __init__(self, image, x_coordinate, y_coordinate):
        super().__init__(image, x_coordinate, y_coordinate)

    def move(self):
        self.ycor -= .25
    