from bullet import Bullet
from hero_shield import Hero_Shield
from ultra_bullet import Ultra_Bullet
from game_object import Game_Object

class Hero(Game_Object):
    def __init__(self, image, x_coordinate, y_coordinate):
        self.direction = 0
        self.speed = 10
        self.score = 0
        self.first_life = True
        self.second_life = False
        self.bullets_fired = []
        self.ultra_bullets_fired = []
        self.shields_placed = []
        super().__init__(image, x_coordinate, y_coordinate)

    def collided_with_right_wall(self, right_wall_x_location):
        return self.xcor + self.width >= right_wall_x_location

    def collided_with_left_wall(self, left_wall_x_location):
        return self.xcor <= left_wall_x_location

    def reload(self):
        if self.reloaded_bullets_fired <= 10:
            self.is_reloaded == False

    def shoot(self, bullet_image):
        new_bullet = Bullet(bullet_image, self.xcor + self.width / 2 - bullet_image.get_width() / 2, self.ycor)
        self.bullets_fired.append(new_bullet)

    def place_down_shield(self, hero_shield_image):
        new_hero_shield = Hero_Shield(hero_shield_image, self.xcor + self.width/2 - hero_shield_image.get_width() / 2, 500)
        self.shields_placed.append(new_hero_shield)

    def shoot_ultra_bullet(self, ultra_bullet_image):
        new_ultra_bullet = Ultra_Bullet(ultra_bullet_image, self.xcor + self.width / 2 - ultra_bullet_image.get_width() / 2, 535)
        self.ultra_bullets_fired.append(new_ultra_bullet)

    def handle_ultra_bullet_wall_collision(self, top_wall):
        for ultra_bullet in self.ultra_bullets_fired:
            if ultra_bullet.collided_with_top_wall(top_wall):
                ultra_bullet.is_alive = False

    def handle_bullet_wall_collision(self, top_wall):
        for bullet in self.bullets_fired:
            if bullet.collided_with_top_wall(top_wall):
                bullet.is_alive = False

        self.remove_dead_bullets()

    def remove_dead_shields(self):
        for i in range(len(self.shields_placed) -1, -1, -1):
            if self.shields_placed[i].is_alive == False:
                self.shields_placed.pop(i)

    def remove_dead_bullets(self):
        for i in range(len(self.bullets_fired) -1, -1, -1):
            if self.bullets_fired[i].is_alive == False:
                self.bullets_fired.pop(i)

    def remove_dead_ultra_bullets(self):
         for i in range(len(self.ultra_bullets_fired) -1, -1, -1):
            if self.ultra_bullets_fired[i].is_alive == False:
                  self.ultra_bullets_fired.pop(i)

    def remove_bullets_after_level_change(self):
        for i in range(len(self.bullets_fired) -1, -1, -1):
            if self.bullets_fired[i].is_alive == True:
                self.bullets_fired.pop(i)

    def remove_ultra_bullets_after_level_change(self):
        for i in range (len(self.ultra_bullets_fired) -1, -1, -1):
            if self.ultra_bullets_fired[i].is_alive == True:
                self.ultra_bullets_fired.pop(i)

    def move_all_bullets(self):
        for bullet in self.bullets_fired:
            bullet.move()
    
    def move_all_ultra_bullets(self):
        for ultra_bullet in self.ultra_bullets_fired:
            ultra_bullet.move()

    def show_all_bullets(self, game_display):
        for bullet in self.bullets_fired:
            bullet.show(game_display)

    def show_all_ultra_bullets(self, game_display):
        for ultra_bullet in self.ultra_bullets_fired:
            ultra_bullet.show(game_display)

    def show_all_hero_shields(self, game_display):
        for hero_shield in self.shields_placed:
            hero_shield.show(game_display)

    def move_all_shields(self):
        for hero_shield in self.shields_placed:
            hero_shield.move()
        
    def move(self, left_wall, right_wall):
        if self.direction == -1 and self.collided_with_left_wall(left_wall) == False:
            self.xcor += self.speed * self.direction
        elif self.direction == 1 and self.collided_with_right_wall(right_wall) == False:
            self.xcor += self.speed * self.direction

    def set_direction_right(self):
        self.direction = 1
    def set_direction_left(self):
        self.direction = -1
    def set_direction_none(self):
        self.direction = 0

