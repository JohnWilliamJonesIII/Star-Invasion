from game_object import Game_Object

class Laser(Game_Object):
    def __init__(self, image, x_coordinate, y_coordinate):
        super().__init__(image, x_coordinate, y_coordinate)

    def move(self):
        self.ycor += 8
        
    def collided_with_bottom_wall(self, bottom_wall_y_location):
        return self.ycor > bottom_wall_y_location