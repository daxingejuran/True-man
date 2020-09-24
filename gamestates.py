class GameStates():
	def __init__(self):
		#开始标志初始化
		self.game_active=0
		#0开始，1运行，2结束
		self.starttime=0.0
		self.stime=0.0
		self.ptime=0.0
		self.st=0
		self.pt=0
		self.endtime=0.0
		self.pflag=0
		self.flag=0
		#0 无特殊，1 一个特殊正在执行，2 两个特殊正在执行，三个特殊正在执行
