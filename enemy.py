import pygame
import random 
#定义普通弹类（速度，屏幕，初始x，初始y，结束x，结束y）
class Enemy():
	def __init__(self,speed,screen,initx,inity,endx,endy,image):
		#初始化参数
		self.speed=speed
		self.screen=screen
		self.initx=initx
		self.inity=inity
		self.endx=endx
		self.endy=endy
		self.image=pygame.image.load(image)
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		#初始位置
		self.rect.centerx=initx
		self.rect.bottom=inity
		
		
		#self.screen_rect[2]=300
		#self.screen_rect[3]=500
		#位置的浮点数表示（为进行精密的运动）
		self.center=[float(self.rect.centerx),float(self.rect.bottom)]
		
		#计算x、y方向和总的移动距离
		self.lengthx=float(abs(endx-initx))
		self.lengthy=float(abs(endy-inity))
		self.length=(self.lengthx**2+self.lengthy**2)**0.5
		
	#刷新函数
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
	#更新位置
	def update(self):
		#定义结束后的新的初始位置和结束位置
		p_initx=0
		p_inity=0
		p_endx=0
		p_endy=0
		#如果没有到达屏幕边缘，则进行移动
		if ((self.center[0]<=self.screen_rect[2]+30)and(self.center[0]>=-30))and((self.center[1]>=-30)and(self.center[1]<=self.screen_rect[2]+30)):
			if self.endx<=self.initx:
				self.center[0]-=self.speed/self.length*self.lengthx
			else:
				self.center[0]+=self.speed/self.length*self.lengthx
			if self.endy<=self.inity:
				self.center[1]-=self.speed/self.length*self.lengthy
			else:
				self.center[1]+=self.speed/self.length*self.lengthy
		#到达屏幕边缘，刷新
		else:
			i1=random.randint(0,3)
			i2=random.randint(0,2)
		
			#up->right,down,left
			if i1==0:
				p_initx=random.randint(-15,self.screen_rect[2]+15)
				p_inity=-15
				if i2==0:
					p_endx=self.screen_rect[2]+15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
				if i2==1:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=self.screen_rect[3]+15
				if i2==2:
					p_endx=-15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
				
			#right->down,left,up
			if i1==1:
				p_initx=self.screen_rect[2]+15
				p_inity=random.randint(-15,self.screen_rect[3]+15)
				if i2==0:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=self.screen_rect[3]+15
				if i2==1:
					p_endx=-15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
				if i2==2:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=-15
					
			#down->left,up,right		
			if i1==2:
				p_initx=random.randint(-15,self.screen_rect[2]+15)
				p_inity=self.screen_rect[3]+15
				if i2==0:
					p_endx=-15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
				if i2==1:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=-15
				if i2==2:
					p_endx=self.screen_rect[2]+15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
								
			#left->up,right,down
			if i1==3:
				p_initx=-15
				p_inity=random.randint(-15,self.screen_rect[3]+15)
				if i2==0:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=-15
				if i2==1:
					p_endx=self.screen_rect[2]+15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
				if i2==2:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=self.screen_rect[3]+15
			
			self.initx=p_initx
			self.inity=p_inity
			self.endx=p_endx
			self.endy=p_endy
			self.center[0]=self.initx
			self.center[1]=self.inity
		#更新位置
		self.rect.centerx=self.center[0]
		self.rect.bottom=self.center[1]
	
class SEnemy(Enemy):
	def __init__(self,speed,screensize,initx,inity,endx,endy,image):
		super().__init__(speed,screensize,initx,inity,endx,endy,image)
		#激活符号
		self.flag=0
		#重新定义update
	def update(self):
		#定义结束后的新的初始位置和结束位置
		p_initx=0
		p_inity=0
		p_endx=0
		p_endy=0
		i1=0
		i2=0
		#如果没有到达屏幕边缘，则进行移动
		if self.flag==1:
			if ((self.center[0]<=self.screen_rect[2]+30)and(self.center[0]>=-30))and((self.center[1]>=-30)and(self.center[1]<=self.screen_rect[3]+30)):

				if self.endx<=self.initx:
					self.center[0]-=self.speed/self.length*self.lengthx
				else:
					self.center[0]+=self.speed/self.length*self.lengthx
				if self.endy<=self.inity:
					self.center[1]-=self.speed/self.length*self.lengthy
				else:
					self.center[1]+=self.speed/self.length*self.lengthy
			#到达屏幕边缘，刷新
			else:
				self.flag=0
				i1=random.randint(0,3)
				i2=random.randint(0,2)
		
				#up->right,down,left
			if i1==0:
				p_initx=random.randint(-15,self.screen_rect[2]+15)
				p_inity=-15
				if i2==0:
					p_endx=self.screen_rect[2]+15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
				if i2==1:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=self.screen_rect[3]+15
				if i2==2:
					p_endx=-15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
				
			#right->down,left,up
			if i1==1:
				p_initx=self.screen_rect[2]+15
				p_inity=random.randint(-15,self.screen_rect[3]+15)
				if i2==0:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=self.screen_rect[3]+15
				if i2==1:
					p_endx=-15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
				if i2==2:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=-15
					
			#down->left,up,right		
			if i1==2:
				p_initx=random.randint(-15,self.screen_rect[2]+15)
				p_inity=self.screen_rect[3]+15
				if i2==0:
					p_endx=-15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
				if i2==1:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=-15
				if i2==2:
					p_endx=self.screen_rect[2]+15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
								
			#left->up,right,down
			if i1==3:
				p_initx=-15
				p_inity=random.randint(-15,self.screen_rect[3]+15)
				if i2==0:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=-15
				if i2==1:
					p_endx=self.screen_rect[2]+15
					p_endy=random.randint(-15,self.screen_rect[3]+15)
				if i2==2:
					p_endx=random.randint(-15,self.screen_rect[2]+15)
					p_endy=self.screen_rect[3]+15
			
				self.initx=p_initx
				self.inity=p_inity
				self.endx=p_endx
				self.endy=p_endy
				self.center[0]=self.initx
				self.center[1]=self.inity
				
			self.rect.centerx=self.center[0]
			self.rect.bottom=self.center[1]	

class FEnemy(SEnemy):
	def __init__(self,speed,screensize,initx,inity,endx,endy,image):
		super().__init__(speed,screensize,initx,inity,endx,endy,image)
		
		self.middle=[float(endx+initx)/2,float(endy+inity)/2]
		self.center4=[0.0,0.0]
		self.fflag=0
		self.lflag=0
		self.rect4=self.image.get_rect()
		self.rect4.centerx=self.middle[0]
		self.rect4.bottom=self.middle[1]
		self.endx4=self.endx
		self.endy4=self.endy
		self.lengthx4=0
		self.lengthy4=0
		self.length4=0

		
	#重新定义update	
	def update(self):
		p_initx=0
		p_inity=0
		p_endx=0
		p_endy=0
		if self.flag==1:
			if ((self.center[0]<=self.screen_rect[2]+30)and(self.center[0]>=-30))and((self.center[1]>=-30)and(self.center[1]<=self.screen_rect[3]+30)):
				#到达分裂位置，分裂符号置1
				if abs(self.center[0]-self.middle[0])<=30 and abs(self.center[1]-self.middle[1])<=30 and self.fflag==0: 
					self.center4[0]=self.center[0]
					self.center4[1]=self.center[1]
				#	if self.endx==-15 or self.endx==615:
					self.endy4=self.endy+150
				#	elif self.endy==-15 or self.endy==415:					
					self.endx4=self.endx+200
					
					self.lengthx4=float(abs(self.endx4-self.center[0]))
					self.lengthy4=float(abs(self.endy4-self.center[1]))
					self.length4=(self.lengthx4**2+self.lengthy4**2)**0.5
				
					self.fflag=1
				#开始分裂
				elif self.fflag==1:
					#原弹直线行进
					
					if self.endx<=self.initx:
						self.center[0]-=self.speed/self.length*self.lengthx
					else:
						self.center[0]+=self.speed/self.length*self.lengthx
					if self.endy<=self.inity:
						self.center[1]-=self.speed/self.length*self.lengthy
					else:
						self.center[1]+=self.speed/self.length*self.lengthy
					#新增弹路线
					
					if self.endx4<=self.middle[0]:
						self.center4[0]-=self.speed/self.length4*self.lengthx4
					else:
						self.center4[0]+=self.speed/self.length4*self.lengthx4
					if self.endy4<=self.middle[1]:
						self.center4[1]-=self.speed/self.length4*self.lengthy4
					else:
						self.center4[1]+=self.speed/self.length4*self.lengthy4
				
				#如果没到达分裂位置继续前进
				else:
					if self.endx<=self.initx:
						self.center[0]-=self.speed/self.length*self.lengthx
					else:
						self.center[0]+=self.speed/self.length*self.lengthx
					if self.endy<=self.inity:
						self.center[1]-=self.speed/self.length*self.lengthy
					else:
						self.center[1]+=self.speed/self.length*self.lengthy
					
			else:
				self.flag=0
				self.fflag=0
				i1=random.randint(0,3)
				i2=random.randint(0,2)
		
				#up->right,down,left
				if i1==0:
					p_initx=random.randint(-15,self.screen_rect[2]+15)
					p_inity=-15
					if i2==0:
						p_endx=self.screen_rect[2]+15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
					if i2==1:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=self.screen_rect[3]+15
					if i2==2:
						p_endx=-15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
				
				#right->down,left,up
				if i1==1:
					p_initx=self.screen_rect[2]+15
					p_inity=random.randint(-15,self.screen_rect[3]+15)
					if i2==0:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=self.screen_rect[3]+15
					if i2==1:
						p_endx=-15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
					if i2==2:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=-15
					
				#down->left,up,right		
				if i1==2:
					p_initx=random.randint(-15,self.screen_rect[2]+15)
					p_inity=self.screen_rect[3]+15
					if i2==0:
						p_endx=-15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
					if i2==1:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=-15
					if i2==2:
						p_endx=self.screen_rect[2]+15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
								
				#left->up,right,down
				if i1==3:
					p_initx=-15
					p_inity=random.randint(-15,self.screen_rect[3]+15)
					if i2==0:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=-15
					if i2==1:
						p_endx=self.screen_rect[2]+15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
					if i2==2:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=self.screen_rect[3]+15
						
				self.middle=[float(p_endx+p_initx)/2,float(p_endy+p_inity)/2]
				
				self.initx=p_initx
				self.inity=p_inity
				self.endx=p_endx
				self.endy=p_endy
				self.center[0]=self.initx
				self.center[1]=self.inity
				self.center4[0]=self.initx
				self.center4[1]=self.inity
															
			self.rect4.centerx=self.center4[0]
			self.rect4.bottom=self.center4[1]
						
				
			self.rect.centerx=self.center[0]
			self.rect.bottom=self.center[1]	
					
			
	def blitme(self):
		if self.fflag==1:
			
			self.screen.blit(self.image,self.rect4)
		
			self.screen.blit(self.image,self.rect)

				
		else:
			self.screen.blit(self.image,self.rect)





class TEnemy(SEnemy):
	def __init__(self,speed,screensize,initx,inity,endx,endy,image):
		super().__init__(speed,screensize,initx,inity,endx,endy,image)
	
	#重新定义update
	def update(self,ship):
		p_initx=0
		p_inity=0
		p_endx=0
		p_endy=0
		if self.flag==1:
			if ((self.center[0]<=self.screen_rect[2]+30)and(self.center[0]>=-30))and((self.center[1]>=-30)and(self.center[1]<=self.screen_rect[3]+30)):
				if self.endx<=self.initx:
					self.center[0]-=self.speed/self.length*self.lengthx#+self.speed/10*(self.center[0]-ship.center[0])
				else:
					self.center[0]+=self.speed/self.length*self.lengthx#+self.speed/100*(self.center[0]-ship.center[0])
				if self.endy<=self.inity:
					self.center[1]-=self.speed/self.length*self.lengthy#+self.speed/100*(self.center[1]-ship.center[1])
				else:
					self.center[1]+=self.speed/self.length*self.lengthy#+self.speed/100*(self.center[0]-ship.center[0])
				if self.center[0]>=ship.center[0]:
					self.center[0]-=self.speed/2
				else:
					self.center[0]+=self.speed/2
				if self.center[1]>=ship.center[1]:
					self.center[1]-=self.speed/2
				else:
					self.center[1]+=self.speed/2
			else:
				self.flag=0
				i1=random.randint(0,3)
				i2=random.randint(0,2)
		
				#up->right,down,left
				if i1==0:
					p_initx=random.randint(-15,self.screen_rect[2]+15)
					p_inity=-15
					if i2==0:
						p_endx=self.screen_rect[2]+15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
					if i2==1:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=self.screen_rect[3]+15
					if i2==2:
						p_endx=-15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
				
				#right->down,left,up
				if i1==1:
					p_initx=self.screen_rect[2]+15
					p_inity=random.randint(-15,self.screen_rect[3]+15)
					if i2==0:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=self.screen_rect[3]+15
					if i2==1:
						p_endx=-15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
					if i2==2:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=-15
					
				#down->left,up,right		
				if i1==2:
					p_initx=random.randint(-15,self.screen_rect[2]+15)
					p_inity=self.screen_rect[3]+15
					if i2==0:
						p_endx=-15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
					if i2==1:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=-15
					if i2==2:
						p_endx=self.screen_rect[2]+15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
								
				#left->up,right,down
				if i1==3:
					p_initx=-15
					p_inity=random.randint(-15,self.screen_rect[3]+15)
					if i2==0:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=-15
					if i2==1:
						p_endx=self.screen_rect[2]+15
						p_endy=random.randint(-15,self.screen_rect[3]+15)
					if i2==2:
						p_endx=random.randint(-15,self.screen_rect[2]+15)
						p_endy=self.screen_rect[3]+15
			
				self.initx=p_initx
				self.inity=p_inity
				self.endx=p_endx
				self.endy=p_endy
				self.center[0]=self.initx
				self.center[1]=self.inity
				
			self.rect.centerx=self.center[0]
			self.rect.bottom=self.center[1]	


#调试用
class Target():
	def __init__(self,screensize,image):	
		self.screen=screensize
	
		
		self.image=pygame.image.load(image)
		self.rect=self.image.get_rect()
		
		self.rect.centerx=0
		self.rect.bottom=0
		
		self.center=[float(self.rect.centerx),float(self.rect.bottom)]
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
	def update(self,enemy):
		
		self.rect.centerx=enemy.middle[0]
		self.rect.bottom=enemy.middle[1]
