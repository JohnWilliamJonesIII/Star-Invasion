from life_bar import Life_Bar
import random
from game_object import Game_Object

class Life_Bars(Game_Object):
    def __init__(self, row_count, column_count, life_bar_img, starting_xcor, starting_ycor):
        self.bars = self.get_initial_life_bars(row_count, column_count, life_bar_img, starting_xcor, starting_ycor)
        # self.width = hero_first_life_image.get_width()
        # self.height = hero_first_life_image.get_height() 
        self.xcor = random.randrange(500)
        self.ycor = starting_ycor

    def get_initial_life_bars(self, row_count, column_count, life_bar_img, starting_xcor, starting_ycor):
        life_bars = []
        for row in range(0, row_count):
            for col in range(0, column_count):
                current_xcor = starting_xcor + col * life_bar_img.get_width() 
                current_ycor = starting_ycor + row  * life_bar_img.get_height()
                life_bars.append(Life_Bar(life_bar_img, current_xcor, current_ycor))
        return life_bars

    def show(self,game_display):
        for bar in self.bars:
            bar.show(game_display)

    def remove_dead_life_bars(self):
        for i in range(len(self.bars) -1, -1, -1):
            if self.bars[i].is_alive == False:
                self.bars.pop(i)
