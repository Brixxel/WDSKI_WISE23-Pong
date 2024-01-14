import pygame, random
import Player, Paddel, AiPlayer, Ball

class GameState_Manager:
    
    def __init__(self, screen):
        
        self.player_score = 0
        self.opponent_score = 0
        
        
        self.paddle_player_1 = 0
        self.paddle_player_2 = 0
        self.paddle_Ai = 0
        self.ball = 0
        
        self.ball_group = pygame.sprite.GroupSingle()
        self.paddle_group = pygame.sprite.Group()
        
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
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
 
 
# New Game Methode, die den Speilstand des bisherigen Spiels löscht und mit den neuen Paddels beginnt

    def Start_PvAi_Game(self):
        self.paddle_player_1 = Paddel.Paddel('skins/Paddle.png', self.screen_width - 20, self.screen_height/2, 5, self.screen_height)
        self.paddle_Ai = AiPlayer.AIPlayer(r'skins\Unbenannt.png',20,self.screen_width/2, 5, self.screen_height)

        self.paddle_group.add(self.paddle_player_1)
        self.paddle_group.add(self.paddle_Ai)
        
        # ... (Alle weiteren Paddels)

        self.ball = Ball.Ball('Ball.png', self.screen_width/2, self.screen_height/2, 4, 4, self.paddle_group, self.screen_height, self.screen_width, self.screen)
        self.ball_group.add(self.ball)
