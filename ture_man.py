import sys
import pygame
import time
from title_text import GameTitle
from gamestates import GameStates
from settings import Settings
from ship import Ship
from enemy import Enemy
from enemy import SEnemy
from enemy import FEnemy
from enemy import TEnemy
from enemy import Target

import game_functions as gf 


def run_game():
	
	
	#pygame 初始化
	pygame.init()
	
	
	#初始化参数
	ai_settings=Settings()
	game_states=GameStates()
	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("20 SECONDS TURE MAN")
	
	
	#初始化舰船
	ship=Ship(screen)
	
	
	#初始化敌人数量
	enemy_number=80
	p1_enemy_number=10
	p2_enemy_number=10
	p3_enemy_number=10
	p4_enemy_number=10
	
	
	#初始化随机位置（普通、巨大、快速、分裂、追踪）
	initx,inity,endx,endy=gf.random_range(enemy_number)
	initx_big,inity_big,endx_big,endy_big=gf.random_range(p1_enemy_number)
	initx_speed,inity_speed,endx_speed,endy_speed=gf.random_range(p1_enemy_number)
	initx_fen,inity_fen,endx_fen,endy_fen=gf.random_range(p2_enemy_number)
	initx_trace,inity_trace,endx_trace,endy_trace=gf.random_range(p2_enemy_number)
	
	
	#初始化循环数组
	num=list(range(0,enemy_number))
	num1=list(range(0,p1_enemy_number))
	num2=list(range(0,p2_enemy_number))
	num3=list(range(0,p3_enemy_number))
	num4=list(range(0,p4_enemy_number))
	
	
	#蛋组初始化
	enemy=[]
	enemy_big=[]
	enemy_speed=[]
	enemy_fen=[]
	enemy_trace=[]
	target=[]
	
	
	#普通弹初始化
	for i in num:
		enemy.append(Enemy(0.1,screen,initx[i],inity[i],endx[i],endy[i],'images/p2.bmp'))
	#重型弹初始化
	for i in num1:
		enemy_big.append(SEnemy(0.15,screen,initx_big[i],inity_big[i],endx_big[i],endy_big[i],'images/b.bmp'))
	#高速弹初始化
	for i in num1:
		enemy_speed.append(SEnemy(0.3,screen,initx_speed[i],inity_speed[i],endx_speed[i],endy_speed[i],'images/s.bmp'))
	#分裂弹初始化
	for i in num2:
		enemy_fen.append(FEnemy(0.1,screen,initx_fen[i],inity_fen[i],endx_fen[i],endy_fen[i],'images/d.bmp'))
	#追踪弹初始化
	for i in num2:
		enemy_trace.append(TEnemy(0.12,screen,initx_trace[i],inity_trace[i],endx_trace[i],endy_trace[i],'images/t.bmp'))
	#标记初始化（调试用）
	for i in num2:
		target.append(Target(screen,'images/h1.bmp'))
	
	
	#主标题绘制
	title=GameTitle(ai_settings,screen,"20 SECONDS TRUE MAN",0,200,48,100,(0,0,0))
	#子标题绘制
	title1=GameTitle(ai_settings,screen,"PRESS SPACE TO START",0,100,30,100,(0,0,0))
	#油料表绘制
	title2=GameTitle(ai_settings,screen,"FUEL 30.0",0,0,20,600,(100,100,100))
	#特殊弹药提示
	title3=GameTitle(ai_settings,screen,"1111 ",200,0,20,100,(100,100,100))
	#结束评价
	endtitle1=GameTitle(ai_settings,screen,"What are you doing?",0,200,60,200,(0,0,0))
	endtitle2=GameTitle(ai_settings,screen,"Trashcan cleaner",0,200,60,200,(0,0,0))
	endtitle3=GameTitle(ai_settings,screen,"Green hand",0,200,60,200,(0,0,0))
	endtitle4=GameTitle(ai_settings,screen,"Old gun",0,200,60,200,(0,0,0))
	endtitle5=GameTitle(ai_settings,screen,"True man",0,200,60,200,(0,0,0))
	endtitle6=GameTitle(ai_settings,screen,"Good day commander",0,200,60,200,(0,0,0)) 
	#结束时间显示初始化
	endtitle=GameTitle(ai_settings,screen,str(game_states.endtime-game_states.starttime),0,0,30,600,(0,0,0))
	
	
	#主循环
	while True:
		#键盘事件检测
		gf.check_events(ship,game_states)
		#刷新屏幕
		gf.update_screen(ai_settings,screen,ship,game_states,title,
		title1,title2,title3,enemy,enemy_big,enemy_speed,enemy_fen,
		enemy_trace,enemy_number,p1_enemy_number,p2_enemy_number,
		p3_enemy_number,p4_enemy_number,endtitle,endtitle1,endtitle2,
		endtitle3,endtitle4,endtitle5,endtitle6)
		
		
#启动游戏
run_game()
	
