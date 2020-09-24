import pygame

class GameTitle():
	def __init__(self,ai_settings,screen,msg,x,height2,size,size2,bgcolor):
		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.width, self.height = size2, 25
		self.button_color = (bgcolor[0], bgcolor[1], bgcolor[2])
		self.text_color = (0, 255, 0)
		self.font = pygame.font.SysFont(None, size)
        
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.centerx = self.screen_rect.centerx-x
		self.rect.bottom = self.screen_rect.bottom-height2
        
		self.prep_msg(msg)

	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg,True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
        
	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)

