import highscore

class GameStats():
	def __init__(self,setting):
		self.setting=setting
		self.reset()
		self.game_state=0
		self.hscore=highscore.HSCORE

	def reset(self):
		self.life_left=self.setting.life_limit
		self.score=0