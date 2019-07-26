
class Game_Object():
    def __init__(self, image, x_coordinate, y_coordinate):
        self.is_alive = True
        self.img = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.xcor = x_coordinate
        self.ycor = y_coordinate

    def show(self, game_display):
        game_display.blit(self.img, (self.xcor, self.ycor))

    def get_right_edge(self):
        return self.xcor + self.width

    def get_bottom_edge(self):
        return self.ycor + self.height

    def has_collided_with(self, other_object):
        return self.get_right_edge() >= other_object.xcor \
            and self.xcor <= other_object.get_right_edge() \
            and self.get_bottom_edge() >= other_object.ycor \
            and self.ycor <= other_object.get_bottom_edge()