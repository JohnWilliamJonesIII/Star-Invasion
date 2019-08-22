from enemy import Enemy
from laser import Laser
import random
from game_object import Game_Object


class Fleet(Game_Object):

    def __init__(self, row_count, column_count, initial_speed, enemy_img, starting_xcor, starting_ycor):
        self.direction = 1
        self.speed = initial_speed
        self.ships = self.get_initial_ships(row_count, column_count, enemy_img, starting_xcor, starting_ycor)
        self.lasers_fired = []
        self.width = enemy_img.get_width()
        self.height = enemy_img.get_height() 
        self.xcor = random.randrange(500)
        self.ycor = starting_ycor

    def get_initial_ships(self, row_count, column_count, enemy_img, starting_xcor, starting_ycor):
        initial_ships = []
        for row in range(0, row_count):
            for col in range(0, column_count):
                current_xcor = starting_xcor + col * enemy_img.get_width() 
                current_ycor = starting_ycor + row  * enemy_img.get_height()
                initial_ships.append(Enemy(enemy_img, current_xcor, current_ycor))
        return initial_ships

    def show(self,game_display):
        for ship in self.ships:
            ship.show(game_display)

    def handle_wall_collision(self, left_wall, right_wall):
        for ship in self.ships:
            if ship.collided_with_left_wall(left_wall) or ship.collided_with_right_wall(right_wall):
                self.move_down()
                self.change_direction()
                break

    def title_screen_fleet_wall_collision(self, left_wall, right_wall):
        for ship in self.ships:
            if ship.collided_with_left_wall(left_wall) or ship.collided_with_right_wall(right_wall):
                self.change_direction()
                break
            
    def move_down(self):
        for ship in self.ships:
            ship.move_down(10)

    def change_direction(self):
        self.direction *= -1

    def move_over(self):      
        for ship in self.ships:
            ship.move_over(self.direction * self.speed)
            self.xcor = random.randrange(500)
         
    def remove_dead_ships(self):
        for i in range(len(self.ships) -1, -1, -1):
            if self.ships[i].is_alive == False:
                self.ships.pop(i)

    def remove_dead_lasers(self):
        for i in range(len(self.lasers_fired) -1, -1, -1):
            if self.lasers_fired[i].is_alive == False:
                self.lasers_fired.pop(i)
                
    def shoot(self, laser_image):
        new_laser = Laser(laser_image, self.xcor + self.width / 2 - laser_image.get_width() / 2, self.ycor)
        self.lasers_fired.append(new_laser)

    def remove_lasers_after_level_change(self):
        for i in range(len(self.lasers_fired) -1, -1, -1):
            if self.lasers_fired[i].is_alive == True:
                self.lasers_fired.pop(i)
                
    def move_all_lasers(self):
        for laser in self.lasers_fired:
            laser.move()

    def show_all_lasers(self, game_display):
        for laser in self.lasers_fired:
            laser.show(game_display)


    def handle_laser_wall_collision(self, bottom_wall):
        for laser in self.lasers_fired:
            if laser.collided_with_bottom_wall(bottom_wall):
                laser.is_alive = False

        self.remove_dead_lasers()

