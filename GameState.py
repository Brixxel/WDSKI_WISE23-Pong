import pygame, random
import Player

class GameState_Manager:
    
    def __init__(self, ball_group, paddle_group, screen):
        
        self.player_score = 0
        self.opponent_score = 0
        
        self.ball_group = ball_group
        self.paddle_group = paddle_group
        
        self.screen = screen
        self.screen_width = screen.get_width()
        
    def run_game(self):
		# Drawing the game objects
        self.paddle_group.draw(self.screen)
        self.ball_group.draw(self.screen)

		# Updating the game objects
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        #self.draw_score()
    
    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= self.screen_width:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

	# def draw_score(self):
	# 	player_score = basic_font.render(str(self.player_score),True,accent_color)
	# 	opponent_score = basic_font.render(str(self.opponent_score),True,accent_color)

	# 	player_score_rect = player_score.get_rect(midleft = (screen_width / 2 + 40,screen_height/2))
	# 	opponent_score_rect = opponent_score.get_rect(midright = (screen_width / 2 - 40,screen_height/2))

	# 	screen.blit(player_score,player_score_rect)
	# 	screen.blit(opponent_score,opponent_score_rect)