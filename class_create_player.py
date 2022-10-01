import random

#自定義class
class Player(object):
	"""docstring for Player"""
	def __init__(self, name, hp, ack):
		self.name = name
		self.hp = hp
		self.ack = ack

players = []	#儲存玩家list
time = 0 		#是否為第一次創建玩家
while(True):
	if(time == 0):
		create = input('要創建角色嗎? (Y/N)')
	else:
		create = input('要繼續創建角色嗎? (Y/N)')
	time += 1
	if(create in ['Y', 'y']):
		name = input('請輸入姓名 : ')
		# hp 和 ack 為自動生成
		hp = random.randint(1,100)
		ack = random.randint(1,100)
		players.append([name, hp, ack])
	elif(create in ['N', 'n']):
		print('--END--')
		break
	else:
		print('請輸入Y or N')

print('-----玩家列表-----')
for p in players:
	#引用自定義的class
	p = Player(p[0], p[1], p[2])
	print('玩家 : ', p.name, ' 生命值為:', p.hp, ';攻擊力為:', p.ack)		