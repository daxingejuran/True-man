import pygame
import time
class Ship():
	def __init__(self,screen):
		#输入屏幕信息
		self.screen=screen
		#载入图形
		self.image=pygame.image.load('images/tm.bmp')
		#载入图形尺寸
		self.rect=self.image.get_rect()
		#载入屏幕尺寸
		self.screen_rect=screen.get_rect()
		#初始位置定为屏幕中心
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.centery
		#移动标记初始化
		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False
		self.boost=False
		#油料表定义
		self.oil=float(100) 
		#位置的浮点数表示（为进行精密的运动）
		self.center=[float(self.rect.centerx),float(self.rect.bottom)]
		#舰船的速度定义
		self.speed=0.1
		#舰船开始加速的时刻
		self.boost_start_time=float(0)
		#舰船结束加速的时刻
		self.boost_end_time=float(0)
		
	#刷新舰船函数(左移和右移为不同的图像)
	def blitme(self):
		if self.moving_left:
			self.screen.blit(pygame.image.load('images/tm1.bmp'),self.rect)
		elif self.moving_right:
			self.screen.blit(pygame.image.load('images/tm2.bmp'),self.rect)
		else:
			self.screen.blit(self.image,self.rect)
		
	#更新舰船位置函数
	def update(self):
		if self.moving_right:
			if self.center[0]<=self.screen_rect[2]-10:
				self.center[0]+=self.speed
		if self.moving_left:
			if self.center[0]>=10:
				self.center[0]-=self.speed
		if self.moving_up:
			if self.center[1]>=20:
				self.center[1]-=self.speed
		if self.moving_down:
			if self.center[1]<=self.screen_rect[3]-25:
				self.center[1]+=self.speed
		self.rect.centerx=self.center[0]
		self.rect.bottom=self.center[1]
		
	#加速函数
	def boost1(self):	
		if self.boost:
			if self.oil>0:
					self.speed=0.4
					self.oil=self.oil-(time.time()-self.boost_start_time)
					if self.oil<0:
						self.oil=0
						self.speed=0.2
			else:
				self.speed=0.2
		else:
			a=time.time()-self.boost_end_time
			if a>=5.0:
				self.oil=self.oil+a-5.0
				if self.oil>100.0:
					self.oil=100.0
			self.speed=0.2
			
