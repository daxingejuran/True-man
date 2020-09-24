import sys
import pygame
import time
import title_text
import random
from enemy import Enemy
from time import sleep

#检测事件
def check_events(ship,game_states):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			key_down_event(event,ship,game_states)
		elif event.type==pygame.KEYUP:	
			key_up_event(event,ship)	
			
		
#键盘按下事件
def key_down_event(event,ship,game_states):	
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_UP:
		ship.moving_up=True
	elif event.key==pygame.K_DOWN:
		ship.moving_down=True
	if event.key==pygame.K_SPACE:
		if game_states.game_active==0:
			game_states.game_active=1
			game_states.starttime=time.time()
			game_states.stime=time.time()
		elif game_states.game_active==1:		
			ship.boost=True
			ship.boost_start_time=time.time()
		elif game_states.game_active==2:
			game_states.game_active=0
			

#键盘抬起事件
def key_up_event(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False
	elif event.key==pygame.K_UP:
		ship.moving_up=False		
	elif event.key==pygame.K_DOWN:
		ship.moving_down=False	
	elif event.key==pygame.K_SPACE:		
		ship.boost=False
		ship.boost_end_time=time.time()	
		

#刷新屏幕
def update_screen(ai_settings,screen,ship,game_states,title,title1,title2,
title3,enemy,enemy_big,enemy_speed,enemy_fen,enemy_trace,enemy_number,p1_enemy_number,p2_enemy_number,
p3_enemy_number,p4_enemy_number,endtitle,endtitle1,
endtitle2,endtitle3,endtitle4,endtitle5,endtitle6):
	j=0
	finishflag=0
	finishflag_big=0
	finishflag_speed=0
	finishflag_trace=0
	finishflag_fen=0
	#定义循环用数组
	num=list(range(0,enemy_number))
	num1=list(range(0,p1_enemy_number))
	num2=list(range(0,p2_enemy_number))
	num3=list(range(0,p3_enemy_number))
	num4=list(range(0,p4_enemy_number))
	#screen.fill(ai_settings.bg_color)
	#如果游戏没开始
	if game_states.game_active==0:
		screen.fill(ai_settings.bg_color)
		title.draw_button()
		title1.draw_button()
		pygame.display.flip()
	#如果游戏开始
	elif game_states.game_active==1:
		screen.fill(ai_settings.bg_color)
		
		ship.update()
		ship.blitme()
		ship.boost1()
		for i in num:
			enemy[i].update()
			enemy[i].blitme()
			enemies=pygame.sprite.collide_rect(ship, enemy[i])
			if int(enemies)>0:
				game_states.endtime=time.time()
				ship.screen.blit(pygame.image.load('images/bl.bmp'),ship.rect)
				game_states.game_active=2
				
				initx,inity,endx,endy=random_range(enemy_number)
				for i in num:
					enemy[i].center=[float(initx[i]),float(inity[i])]
					enemy[i].rect.centerx=initx[i]
					enemy[i].rect.bottom=inity[i]
					enemy[i].blitme()					
				initx,inity,endx,endy=random_range(p1_enemy_number)
				for i in num1:
					enemy_big[i].center=[float(initx[i]),float(inity[i])]
					enemy_big[i].rect.centerx=initx[i]
					enemy_big[i].rect.bottom=inity[i]
					enemy_big[i].blitme()
					enemy_big[i].flag=0
				initx,inity,endx,endy=random_range(p1_enemy_number)
				for i in num1:
					enemy_speed[i].center=[float(initx[i]),float(inity[i])]
					enemy_speed[i].rect.centerx=initx[i]
					enemy_speed[i].rect.bottom=inity[i]
					enemy_speed[i].blitme()
					enemy_speed[i].flag=0
				for i in num2:
					enemy_fen[i].center=[float(initx[i]),float(inity[i])]
					enemy_fen[i].rect.centerx=initx[i]
					enemy_fen[i].rect.bottom=inity[i]
					enemy_fen[i].rect4.centerx=initx[i]
					enemy_fen[i].rect4.bottom=inity[i]
					enemy_fen[i].middle=[float(endx[i]+initx[i])/2,float(endy[i]+inity[i])/2]
					enemy_fen[i].blitme()
					enemy_fen[i].flag=0
				for i in num2:
					enemy_trace[i].center=[float(initx[i]),float(inity[i])]
					enemy_trace[i].rect.centerx=initx[i]
					enemy_trace[i].rect.bottom=inity[i]
					enemy_trace[i].blitme()
					enemy_trace[i].flag=0
				ship.center=[float(300),float(200)]
				ship.rect.centerx=300
				ship.rect.bottom=200
				ship.blitme()
				
				
				enemies=0
		
		
		#加入特殊弹种
		if (time.time()-game_states.stime<=(game_states.st+2+0.1))and(time.time()-game_states.stime>=(game_states.st+2-0.1)):
			game_states.st+=2
			game_states.stime=time.time()
			for i in num1:
					finishflag_big+=enemy_big[i].flag
					finishflag_speed+=enemy_speed[i].flag
					
			for i in num2:
					finishflag_fen+=enemy_fen[i].flag
					finishflag_trace+=enemy_trace[i].flag
					
			if game_states.stime-game_states.starttime<20: 
			#j=0
				j=random.randint(0,2)
				
				
				if j==0:
					if finishflag_big==0:
						for i in num1:	
							enemy_big[i].flag=1
				
				if j==1:
					if finishflag_speed==0:
						for i in num1:	
							enemy_speed[i].flag=1
				
				if j==3:
					if finishflag_fen==0:
						for i in num2:	
							enemy_fen[i].flag=1	
				if j==2:
					if finishflag_trace==0:
						for i in num2:	
							enemy_trace[i].flag=1	
			elif game_states.stime-game_states.starttime<30:
				
				j=random.randint(0,2)
				if j==0:
					if finishflag_big+finishflag_speed==0:
						for i in num1:	
							enemy_big[i].flag=1
							enemy_speed[i].flag=1
				if j==1:
					if finishflag_big+finishflag_trace==0:
						for i in num1:
							enemy_big[i].flag=1
						for i in num2:
							enemy_trace[i].flag=1	
				if j==2:
					if finishflag_speed+finishflag_trace==0:
						for i in num1:
							enemy_speed[i].flag=1
						for i in num2:
							enemy_trace[i].flag=1
			else:
				if finishflag_big+finishflag_speed+finishflag_trace==0:
					for i in num1:	
						enemy_big[i].flag=1
						enemy_speed[i].flag=1
					for i in num2:
						enemy_trace[i].flag=1
		for i in num1:
			enemy_big[i].update()
			enemy_big[i].blitme()
			enemies=pygame.sprite.collide_rect(ship, enemy_big[i])
			if int(enemies)>0:
				game_states.endtime=time.time()
				ship.screen.blit(pygame.image.load('images/bl.bmp'),ship.rect)
				game_states.game_active=2
				
				
				initx,inity,endx,endy=random_range(enemy_number)
				for i in num:
					enemy[i].center=[float(initx[i]),float(inity[i])]
					enemy[i].rect.centerx=initx[i]
					enemy[i].rect.bottom=inity[i]
					enemy[i].blitme()
					
				initx,inity,endx,endy=random_range(p1_enemy_number)
				for i in num1:
					enemy_big[i].center=[float(initx[i]),float(inity[i])]
					enemy_big[i].rect.centerx=initx[i]
					enemy_big[i].rect.bottom=inity[i]
					enemy_big[i].blitme()
					enemy_big[i].flag=0
				initx,inity,endx,endy=random_range(p1_enemy_number)
				for i in num1:
					enemy_speed[i].center=[float(initx[i]),float(inity[i])]
					enemy_speed[i].rect.centerx=initx[i]
					enemy_speed[i].rect.bottom=inity[i]
					enemy_speed[i].blitme()
					enemy_speed[i].flag=0
				for i in num2:
					enemy_fen[i].center=[float(initx[i]),float(inity[i])]
					enemy_fen[i].rect.centerx=initx[i]
					enemy_fen[i].rect.bottom=inity[i]
					enemy_fen[i].rect4.centerx=initx[i]
					enemy_fen[i].rect4.bottom=inity[i]
					
					enemy_fen[i].middle=[float(endx[i]+initx[i])/2,float(endy[i]+inity[i])/2]	
					enemy_fen[i].blitme()
					enemy_fen[i].flag=0
				for i in num2:
					enemy_trace[i].center=[float(initx[i]),float(inity[i])]
					enemy_trace[i].rect.centerx=initx[i]
					enemy_trace[i].rect.bottom=inity[i]
					enemy_trace[i].blitme()
					enemy_trace[i].flag=0
				ship.center=[float(300),float(200)]
				ship.rect.centerx=300
				ship.rect.bottom=200
				ship.blitme()
				enemies=0
				
		for i in num1:
			enemy_speed[i].update()
			enemy_speed[i].blitme()
			enemies=pygame.sprite.collide_rect(ship, enemy_speed[i])
			if int(enemies)>0:
				game_states.endtime=time.time()
				ship.screen.blit(pygame.image.load('images/bl.bmp'),ship.rect)
				game_states.game_active=2
				
				
				
				initx,inity,endx,endy=random_range(enemy_number)
				for i in num:
					enemy[i].center=[float(initx[i]),float(inity[i])]
					enemy[i].rect.centerx=initx[i]
					enemy[i].rect.bottom=inity[i]
					enemy[i].blitme()
					
				initx,inity,endx,endy=random_range(p1_enemy_number)
				for i in num1:
					enemy_big[i].center=[float(initx[i]),float(inity[i])]
					enemy_big[i].rect.centerx=initx[i]
					enemy_big[i].rect.bottom=inity[i]
					enemy_big[i].blitme()
					enemy_big[i].flag=0
				initx,inity,endx,endy=random_range(p1_enemy_number)
				for i in num1:
					enemy_speed[i].center=[float(initx[i]),float(inity[i])]
					enemy_speed[i].rect.centerx=initx[i]
					enemy_speed[i].rect.bottom=inity[i]
					enemy_speed[i].blitme()
					enemy_speed[i].flag=0
				for i in num2:
					enemy_fen[i].center=[float(initx[i]),float(inity[i])]
					enemy_fen[i].rect.centerx=initx[i]
					enemy_fen[i].rect.bottom=inity[i]
					enemy_fen[i].rect4.centerx=initx[i]
					enemy_fen[i].rect4.bottom=inity[i]	
					enemy_fen[i].middle=[float(endx[i]+initx[i])/2,float(endy[i]+inity[i])/2]
					enemy_fen[i].blitme()
					enemy_fen[i].flag=0
				for i in num2:
					enemy_trace[i].center=[float(initx[i]),float(inity[i])]
					enemy_trace[i].rect.centerx=initx[i]
					enemy_trace[i].rect.bottom=inity[i]
					enemy_trace[i].blitme()
					enemy_trace[i].flag=0
				ship.center=[float(300),float(200)]
				ship.rect.centerx=300
				ship.rect.bottom=200
				ship.blitme()
				enemies=0
	##	
		for i in num2:
			enemy_fen[i].update()
			enemy_fen[i].blitme()
			enemies=pygame.sprite.collide_rect(ship, enemy_fen[i])
			if int(enemies)>0:
				game_states.endtime=time.time()
				ship.screen.blit(pygame.image.load('images/bl.bmp'),ship.rect)
				game_states.game_active=2
				initx,inity,endx,endy=random_range(enemy_number)
				for i in num:
					enemy[i].center=[float(initx[i]),float(inity[i])]
					enemy[i].rect.centerx=initx[i]
					enemy[i].rect.bottom=inity[i]
					enemy[i].blitme()
					
				initx,inity,endx,endy=random_range(p1_enemy_number)
				for i in num1:
					enemy_big[i].center=[float(initx[i]),float(inity[i])]
					enemy_big[i].rect.centerx=initx[i]
					enemy_big[i].rect.bottom=inity[i]
					enemy_big[i].blitme()
					enemy_big[i].flag=0
				initx,inity,endx,endy=random_range(p1_enemy_number)
				for i in num1:
					enemy_speed[i].center=[float(initx[i]),float(inity[i])]
					enemy_speed[i].rect.centerx=initx[i]
					enemy_speed[i].rect.bottom=inity[i]
					enemy_speed[i].blitme()
					enemy_speed[i].flag=0
				initx,inity,endx,endy=random_range(p2_enemy_number)
				for i in num2:
					enemy_fen[i].center=[float(initx[i]),float(inity[i])]
					enemy_fen[i].rect.centerx=initx[i]
					enemy_fen[i].rect.bottom=inity[i]
					enemy_fen[i].rect4.centerx=initx[i]
					enemy_fen[i].rect4.bottom=inity[i]
					enemy_fen[i].middle=[float(endx[i]+initx[i])/2,float(endy[i]+inity[i])/2]
					enemy_fen[i].blitme()
					enemy_fen[i].flag=0
				for i in num2:
					enemy_trace[i].center=[float(initx[i]),float(inity[i])]
					enemy_trace[i].rect.centerx=initx[i]
					enemy_trace[i].rect.bottom=inity[i]
					enemy_trace[i].blitme()
					enemy_trace[i].flag=0	
				ship.center=[float(300),float(200)]
				ship.rect.centerx=300
				ship.rect.bottom=200
				ship.blitme()
				enemies=0
##		
		for i in num2:
			enemy_trace[i].update(ship)
			enemy_trace[i].blitme()
			enemies=pygame.sprite.collide_rect(ship, enemy_trace[i])
			if int(enemies)>0:
				game_states.endtime=time.time()
				ship.screen.blit(pygame.image.load('images/bl.bmp'),ship.rect)
				game_states.game_active=2
				
				
				
				initx,inity,endx,endy=random_range(enemy_number)
				for i in num:
					enemy[i].center=[float(initx[i]),float(inity[i])]
					enemy[i].rect.centerx=initx[i]
					enemy[i].rect.bottom=inity[i]
					enemy[i].blitme()
					
				initx,inity,endx,endy=random_range(p1_enemy_number)
				for i in num1:
					enemy_big[i].center=[float(initx[i]),float(inity[i])]
					enemy_big[i].rect.centerx=initx[i]
					enemy_big[i].rect.bottom=inity[i]
					enemy_big[i].blitme()
					enemy_big[i].flag=0
				initx,inity,endx,endy=random_range(p1_enemy_number)
				for i in num1:
					enemy_speed[i].center=[float(initx[i]),float(inity[i])]
					enemy_speed[i].rect.centerx=initx[i]
					enemy_speed[i].rect.bottom=inity[i]
					enemy_speed[i].blitme()
					enemy_speed[i].flag=0
				for i in num2:
					enemy_fen[i].center=[float(initx[i]),float(inity[i])]
					enemy_fen[i].rect.centerx=initx[i]
					enemy_fen[i].rect.bottom=inity[i]
					enemy_fen[i].rect4.centerx=initx[i]
					enemy_fen[i].rect4.bottom=inity[i]	
					enemy_fen[i].middle=[float(endx[i]+initx[i])/2,float(endy[i]+inity[i])/2]
					enemy_fen[i].blitme()
					enemy_fen[i].flag=0
				for i in num2:
					enemy_trace[i].center=[float(initx[i]),float(inity[i])]
					enemy_trace[i].rect.centerx=initx[i]
					enemy_trace[i].rect.bottom=inity[i]
					enemy_trace[i].blitme()
					enemy_trace[i].flag=0
				ship.center=[float(300),float(200)]
				ship.rect.centerx=300
				ship.rect.bottom=200
				ship.blitme()
				enemies=0	
		title2.prep_msg("FUEL "+str(int(ship.oil)))
		title2.draw_button()
		if enemy_big[p1_enemy_number-1].flag==1:
				title3.prep_msg("Big bomb has come")
				title3.draw_button()
		if enemy_speed[p1_enemy_number-1].flag==1:	
				title3.prep_msg("Speeding bomb has come")
				title3.draw_button()
		if enemy_fen[p2_enemy_number-1].flag==1:	
				title3.prep_msg("Spliting bomb has come")
				title3.draw_button()
		if enemy_trace[p2_enemy_number-1].flag==1:	
				title3.prep_msg("Tracing bomb has come")
				title3.draw_button()
		pygame.display.flip()		
	#如果游戏结束
	elif  game_states.game_active==2:
		
		#screen.fill(ai_settings.bg_color)
		endtitle.prep_msg(str(round(game_states.endtime-game_states.starttime, 2)))
		endtitle.draw_button()
		if game_states.endtime-game_states.starttime<=5:
			endtitle1.draw_button()	
		elif game_states.endtime-game_states.starttime<=10:
			endtitle2.draw_button()	
		elif game_states.endtime-game_states.starttime<=15:
			endtitle3.draw_button()	
		elif game_states.endtime-game_states.starttime<=20:
			endtitle4.draw_button()	
		elif game_states.endtime-game_states.starttime<=25:
			endtitle5.draw_button()	
		else:
			endtitle6.draw_button()
		#print(game_states.pflag)
		pygame.display.flip()				

def random_range(num):
	rr=list(range(0,num))
	rr1=list(range(0,num))
	initx=list(range(0,num))
	inity=list(range(0,num))
	endx=list(range(0,num))
	endy=list(range(0,num))
	for i in rr:
		rr[i]=random.randint(0,3)
		rr1[i]=random.randint(0,2)
		
		#up->right,down,left
		if rr[i]==0:
			initx[i]=random.randint(-15,615)
			inity[i]=-15
			if rr1[i]==0:
				endx[i]=615
				endy[i]=random.randint(-15,415)
			if rr1[i]==1:
				endx[i]=random.randint(-15,615)
				endy[i]=415
			if rr1[i]==2:
				endx[i]=-15
				endy[i]=random.randint(-15,415)
				
		#right->down,left,up
		if rr[i]==1:
			initx[i]=615
			inity[i]=random.randint(-15,415)
			if rr1[i]==0:
				endx[i]=random.randint(-15,615)
				endy[i]=415
			if rr1[i]==1:
				endx[i]=-15
				endy[i]=random.randint(-15,415)
			if rr1[i]==2:
				endx[i]=random.randint(-15,615)
				endy[i]=-15
				
		#down->left,up,right		
		if rr[i]==2:
			initx[i]=random.randint(-15,615)
			inity[i]=415
			if rr1[i]==0:
				endx[i]=-15
				endy[i]=random.randint(-15,415)
			if rr1[i]==1:
				endx[i]=random.randint(-15,615)
				endy[i]=-15
			if rr1[i]==2:
				endx[i]=615
				endy[i]=random.randint(-15,415)
								
		#left->up,right,down
		if rr[i]==3:
			initx[i]=-15
			inity[i]=random.randint(-15,415)
			if rr1[i]==0:
				endx[i]=random.randint(-15,615)
				endy[i]=-15
			if rr1[i]==1:
				endx[i]=615
				endy[i]=random.randint(-15,415)
			if rr1[i]==2:
				endx[i]=random.randint(-15,615)
				endy[i]=415		
	return initx,inity,endx,endy
