from random import random, randint, uniform, choice
from time import localtime, time, sleep


'''-----------------------------------------------准备工作-----------------------------------------------'''
# 属性结构体
class Myclass(object):
    class Struct(object):
        def __init__(self, name, hp, mp, atk, dfc, crh, cre, rhp, rmp, thp, fhp, mis):
            self.hp = hp
            self.mp = mp
            self.atk = atk
            self.dfc = dfc
            self.crh = crh
            self.cre = cre
            self.rhp = rhp
            self.rmp = rmp
            self.thp = thp
            self.fhp = fhp
            self.mis = mis

    def make_struct(self, name, hp, mp, atk, dfc, crh, cre, rhp, rmp, thp, fhp, mis):
        return self.Struct(name, hp, mp, atk, dfc, crh, cre, rhp, rmp, thp, fhp, mis)

# 创建快捷方式
myclass = Myclass()

# 创建概率机制
def probability(p):
	if random() < p:
		return True
	else:
		return False

# 敌方属性声明
global E_HP    # 血量
global E_MP    # 能量
global E_ATK   # 攻击
global E_DFC   # 防御
global E_CRH   # 暴率
global E_CRE   # 暴伤
global E_RHP   # 回血
global E_RMP   # 充能
global E_THP   # 穿透
global E_FHP   # 吸血
global E_MIS   # 闪避

# 主角属性声明
global HP    # 血量
global MP    # 能量
global ATK   # 攻击
global DFC   # 防御
global CRH   # 暴率
global CRE   # 暴伤
global RHP   # 回血
global RMP   # 充能
global THP   # 穿透
global FHP   # 吸血
global MIS   # 闪避

# 主角初始属性
HP = 300    # 血量
MP = 0      # 能量
ATK = 25    # 攻击
DFC = 8     # 防御
CRH = 0     # 暴率
CRE = 2     # 暴伤
RHP = 10    # 回血
RMP = 0.5   # 充能
THP = 0     # 穿透
FHP = 0     # 吸血
MIS = 0     # 闪避

# 敌方初始属性
E_HP = 0    # 血量
E_MP = 0    # 能量
E_ATK = 0   # 攻击
E_DFC = 0   # 防御
E_CRH = 0   # 暴率
E_CRE = 0   # 暴伤
E_RHP = 0   # 回血
E_RMP = 0   # 充能
E_THP = 0   # 穿透
E_FHP = 0   # 吸血
E_MIS = 0   # 闪避

# 天赋机制
talent_list = [None, "坚如磐石", "锋芒毕露", "摧枯拉朽", "不死之身"]
talent = randint(1, 4)

# 技能时计
skill_clock = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# 初始化
def setup():
	lead.hp = round(HP, 2)
	lead.mp = round(MP, 2)
	lead.atk = round(ATK, 2)
	lead.dfc = round(DFC, 2)
	lead.crh = round(CRH, 2)
	lead.cre = round(CRE, 2)
	lead.rhp = round(RHP, 2)
	lead.rmp = round(RMP, 2)
	lead.thp = round(THP, 2)
	lead.fhp = round(FHP, 2)
	lead.mis = round(MIS, 2)
	for i in range(3):
		for j in range(4):
			skill_clock[i][j] = 0

# 输出属性表
def prppt(obj):
	global HP    # 血量
	global MP    # 能量
	global ATK   # 攻击
	global DFC   # 防御
	global CRH   # 暴率
	global CRE   # 暴伤
	global RHP   # 回血
	global RMP   # 充能
	global THP   # 穿透
	global FHP   # 吸血
	global MIS   # 闪避

	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避

	if obj == 0:
		print("——————————————————————————————————————")
		print("血量:", round(HP, 2))
		print("攻击:", round(ATK, 2))
		print("防御:", round(DFC, 2))
		print("暴击率:", round(CRH * 100, 2), "%")
		print("暴击效果:", round(CRE, 2))
		print("回血:", round(RHP, 2))
		print("穿透:", round(THP * 100, 2), "%")
		print("吸血:", round(FHP * 100, 2), "%")
		print("闪避:", round(MIS * 100, 2), "%")
		print("——————————————————————————————————————\n")
		sleep(interval)
	else:
		print("——————————————————————————————————————")
		print("血量:", E_HP)
		print("攻击:", E_ATK)
		print("防御:", E_DFC)
		print("暴击率:", round(E_CRH * 100, 2), "%")
		print("暴击效果:", E_CRE)
		print("回血:", E_RHP)
		print("穿透:", round(E_THP * 100, 2), "%")
		print("吸血:", round(E_FHP * 100, 2), "%")
		print("闪避:", round(E_MIS * 100, 2), "%")
		print("——————————————————————————————————————\n")
		sleep(interval)

# 输出技能表
def prskl():
	print("技能表: ")
	sleep(interval)
	print("——————————————————————————————————————")
	print("消耗 1 能量: ")
	print("【恢复】 回复三倍回血的血量。")
	print("【强化】 攻击增加 50%，持续 1 回合。")
	print("【守护】 防御增加 80%，持续 1 回合。")
	print("【斩杀】 对目标造成 20% 目标已损生命值的伤害。")
	print("消耗 2 能量: ")
	print("【圣光】 增加 300% 回血，减少目标 50% 的防御，持续 2 回合。")
	print("【诡步】 增加 20% 穿透，25% 暴击率，30% 闪避，持续 2 回合。")
	print("消耗 3 能量: ")
	print("【狂暴】 增加 40% 穿透，5% 吸血，30% 暴击率，75% 攻击，持续 3 回合。")
	print("【压制】 使目标无法防御，无法闪避，持续 3 回合。")
	print("——————————————————————————————————————\n")
	sleep(interval)


'''-----------------------------------------------技能设置-----------------------------------------------'''
# 恢复
def recovery():
	lead.mp -= 1
	lead.hp += 3 * lead.rhp

# 强化
def enhancement():
	lead.mp -= 1
	lead.atk *= 1.5
	skill_clock[0][1] = 1

# 守护
def guard():
	lead.mp -= 1
	lead.dfc *= 1.8
	skill_clock[0][2] = 1

# 斩杀
def kill():
	lead.mp -= 1
	enemy.hp -= (E_HP - enemy.hp) * 0.2

# 圣光
def holy_light():
	lead.mp -= 2
	lead.rhp *= 4
	enemy.dfc /= 2
	skill_clock[1][0] = 2

# 诡步
def sneaking():
	lead.mp -= 2
	lead.thp += 0.2
	lead.crh += 0.25
	lead.mis += 0.3
	skill_clock[1][1] = 2

# 狂暴
def rage():
	lead.mp -= 3
	lead.thp += 0.4
	lead.fhp += 0.05
	lead.crh += 0.3
	lead.atk *= 1.75
	skill_clock[2][0] = 3

# 压制
def suppress():
	lead.mp -= 3
	enemy.dfc = 0
	enemy.mis = 0
	skill_clock[2][1] = 3

'''-----------------------------------------------关卡设置-----------------------------------------------'''
# 第 1 关
def level_1():
	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避
	enemy.name = "哥布林"
	enemy.hp = E_HP = randint(400, 420)
	enemy.atk = E_ATK = randint(30, 40)
	enemy.dfc = E_DFC = randint(10, 12)
	enemy.crh = E_CRH = 0
	enemy.cre = E_CRE = 0
	enemy.rhp = E_RHP = 0
	enemy.thp = E_THP = 0
	enemy.fhp = E_FHP = 0
	enemy.mis = E_MIS = 0

# 第 2 关
def level_2():
	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避
	enemy.name = "哥布林国王"
	enemy.hp = E_HP = randint(600, 800)
	enemy.atk = E_ATK = randint(42, 48)
	enemy.dfc = E_DFC = randint(20, 30)
	enemy.crh = E_CRH = round(uniform(0.02, 0.04), 2)
	enemy.cre = E_CRE = round(uniform(1.6, 1.9), 2)
	enemy.rhp = E_RHP = randint(5, 7)
	enemy.thp = E_THP = round(uniform(0.02, 0.04), 2)
	enemy.fhp = E_FHP = 0
	enemy.mis = E_MIS = 0

# 第 3 关
def level_3():
	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避
	enemy.name = "羊头人"
	enemy.hp = E_HP = randint(1000, 1100)
	enemy.atk = E_ATK = randint(60, 70)
	enemy.dfc = E_DFC = randint(38, 50)
	enemy.crh = E_CRH = round(uniform(0.1, 0.15), 2)
	enemy.cre = E_CRE = round(uniform(2, 2.8), 2)
	enemy.rhp = E_RHP = randint(12, 15)
	enemy.thp = E_THP = round(uniform(0.02, 0.04), 2)
	enemy.fhp = E_FHP = 0
	enemy.mis = E_MIS = round(uniform(0.01, 0.02), 2)

# 第 4 关
def level_4():
	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避
	enemy.name = "卓柏卡布拉"
	enemy.hp = E_HP = randint(1500, 1800)
	enemy.atk = E_ATK = randint(82, 90)
	enemy.dfc = E_DFC = randint(60, 68)
	enemy.crh = E_CRH = round(uniform(0.2, 0.25), 2)
	enemy.cre = E_CRE = round(uniform(3, 3.5), 2)
	enemy.rhp = E_RHP = randint(25, 30)
	enemy.thp = E_THP = round(uniform(0.1, 0.14), 2)
	enemy.fhp = E_FHP = round(uniform(0.7, 0.75), 2)
	enemy.mis = E_MIS = round(uniform(0.03, 0.05), 2)


# 第 5 关
def level_5():
	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避
	enemy.name = "深渊之主"
	enemy.hp = E_HP = randint(2000, 2500)
	enemy.atk = E_ATK = randint(105, 120)
	enemy.dfc = E_DFC = randint(80, 100)
	enemy.crh = E_CRH = round(uniform(0.3, 0.4), 2)
	enemy.cre = E_CRE = round(uniform(3.9, 4.4), 2)
	enemy.rhp = E_RHP = randint(40, 50)
	enemy.thp = E_THP = round(uniform(0.2, 0.3), 2)
	enemy.fhp = E_FHP = round(uniform(0.3, 0.36), 2)
	enemy.mis = E_MIS = round(uniform(0.1, 0.12), 2)

# 第 6 关
def level_6():
	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避
	enemy.name = "变形幽灵"
	enemy.hp = E_HP = randint(1900, 2000)
	enemy.atk = E_ATK = randint(150, 175)
	enemy.dfc = E_DFC = randint(70, 80)
	enemy.crh = E_CRH = round(uniform(0.5, 0.55), 2)
	enemy.cre = E_CRE = round(uniform(3, 3.5), 2)
	enemy.rhp = E_RHP = randint(54, 60)
	enemy.thp = E_THP = round(uniform(0.3, 0.35), 2)
	enemy.fhp = E_FHP = round(uniform(0.2, 0.23), 2)
	enemy.mis = E_MIS = round(uniform(0.5, 0.65), 2)

# 第 7 关
def level_7():
	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避
	enemy.name = "血魔猎手"
	enemy.hp = E_HP = randint(3000, 3500)
	enemy.atk = E_ATK = randint(200, 230)
	enemy.dfc = E_DFC = randint(120, 150)
	enemy.crh = E_CRH = round(uniform(0.75, 0.8), 2)
	enemy.cre = E_CRE = round(uniform(4.2, 4.5), 2)
	enemy.rhp = E_RHP = randint(80, 90)
	enemy.thp = E_THP = round(uniform(0.5, 0.6), 2)
	enemy.fhp = E_FHP = round(uniform(0.18, 0.3), 2)
	enemy.mis = E_MIS = round(uniform(0.3, 0.36), 2)

# 第 8 关
def level_8():
	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避
	enemy.name = "暗黑玄武"
	enemy.hp = E_HP = randint(5500, 6000)
	enemy.atk = E_ATK = randint(500, 600)
	enemy.dfc = E_DFC = randint(5000, 6000)
	enemy.crh = E_CRH = round(uniform(0.3, 0.4), 2)
	enemy.cre = E_CRE = round(uniform(2.5, 3), 2)
	enemy.rhp = E_RHP = randint(105, 120)
	enemy.thp = E_THP = round(uniform(0.85, 0.9), 2)
	enemy.fhp = E_FHP = round(uniform(0.5, 0.6), 2)
	enemy.mis = E_MIS = 0

# 第 9 关
def level_9():
	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避
	enemy.name = "恶魔之眼"
	enemy.hp = E_HP = randint(4000, 4500)
	enemy.atk = E_ATK = randint(200, 250)
	enemy.dfc = E_DFC = randint(300, 350)
	enemy.crh = E_CRH = round(uniform(0.7, 0.85), 2)
	enemy.cre = E_CRE = round(uniform(5.8, 6.5), 2)
	enemy.rhp = E_RHP = randint(100, 120)
	enemy.thp = E_THP = round(uniform(0.55, 0.65), 2)
	enemy.fhp = E_FHP = round(uniform(0.6, 0.7), 2)
	enemy.mis = E_MIS = round(uniform(0.4, 0.5))

# 第 10 关
def level_10():
	global E_HP    # 血量
	global E_MP    # 能量
	global E_ATK   # 攻击
	global E_DFC   # 防御
	global E_CRH   # 暴率
	global E_CRE   # 暴伤
	global E_RHP   # 回血
	global E_RMP   # 充能
	global E_THP   # 穿透
	global E_FHP   # 吸血
	global E_MIS   # 闪避
	enemy.name = "不灭之源"
	enemy.hp = E_HP = 1
	enemy.atk = E_ATK = 1
	enemy.dfc = E_DFC = 0
	enemy.crh = E_CRH = 0
	enemy.cre = E_CRE = 0
	enemy.rhp = E_RHP = 0
	enemy.thp = E_THP = 0
	enemy.fhp = E_FHP = 0
	enemy.mis = E_MIS = 0.999


'''-----------------------------------------------游戏逻辑-----------------------------------------------'''
def start(level):
	global HP    # 血量
	global MP    # 能量
	global ATK   # 攻击
	global DFC   # 防御
	global CRH   # 暴率
	global CRE   # 暴伤
	global RHP   # 回血
	global RMP   # 充能
	global THP   # 穿透
	global FHP   # 吸血
	global MIS   # 闪避
	global con   # 通关判断
	global both  # 一次性彩蛋判断
	con = False
	both = True
	if level < 10:
		setup()
	else:
		lead.hp = HP = 500     # 血量
		lead.mp = MP = 0       # 能量
		lead.atk = ATK = 1     # 攻击
		lead.dfc = DFC = 0     # 防御
		lead.crh = CRH = 0     # 暴率
		lead.cre = CRE = 0     # 暴伤
		lead.rhp = RHP = 0     # 回血
		lead.rmp = RMP = 0     # 充能
		lead.thp = THP = 0     # 穿透
		lead.fhp = FHP = 0     # 吸血
		lead.mis = MIS = 0     # 闪避
		print("历经千辛万苦，你终于找到了不灭之源……")
		sleep(interval)
		print("突然，不灭之源散发出了阵阵魔气，被魔气沾染的你，受到了极大的削弱! ")
		sleep(interval)
		print("而且因为魔气的沾染，你失去了充能的能力! ")
		print(interval)
		print("你感觉被蒙住了双眼，不得不开始战斗……")
		print(interval)
		print("你的属性: ")
		sleep(interval)
		prppt(0)
	if level == 1:
		level_1()
	if level == 2:
		level_2()
	if level == 3:
		level_3()
	if level == 4:
		level_4()
	if level == 5:
		level_5()
	if level == 6:
		level_6()
	if level == 7:
		level_7()
	if level == 8:
		level_8()
	if level == 9:
		level_9()
	if level == 10:
		level_10()
	print("\n第", level, "关:", enemy.name)
	sleep(interval)
	print("正在调取其属性……")
	sleep(interval)
	print("调取成功！")
	sleep(interval)
	prppt(1)  # 显示敌方属性
	while(enemy.hp > 0 and lead.hp > 0):
		sleep(interval)
		if lead.mp < 3:  # 充能
			lead.mp += lead.rmp
		print("\n成功充能，当前能量: ", lead.mp)

		# 逐一倒计时，取消效果
		if skill_clock[0][1] > 0:
			skill_clock[0][1] -= 1
			if skill_clock[0][1] == 0:
				lead.atk /= 1.5
				print("【强化】 效果已结束。")
				sleep(interval)

		if skill_clock[0][2] > 0:
			skill_clock[0][2] -= 1
			if skill_clock[0][2] == 0:
				lead.dfc /= 1.8
				print("【守护】 效果已结束。")
				sleep(interval)

		if skill_clock[1][0] > 0:
			skill_clock[1][0] -= 1
			if skill_clock[1][0] == 0:
				lead.rhp /= 4
				enemy.dfc *= 2
				print("【圣光】 效果已结束。")
				sleep(interval)

		if skill_clock[1][1] > 0:
			skill_clock[1][1] -= 1
			if skill_clock[1][1] == 0:
				lead.thp -= 0.2
				lead.crh -= 0.25
				lead.mis -= 0.3
				print("【诡步】 效果已结束。")
				sleep(interval)

		if skill_clock[2][0] > 0:
			skill_clock[2][0] -= 1
			if skill_clock[2][0] == 0:
				lead.thp -= 0.4
				lead.fhp -= 0.05
				lead.crh -= 0.3
				lead.atk /= 1.75 
				print("【狂暴】 效果已结束。")
				sleep(interval)

		if skill_clock[2][1] > 0:
			skill_clock[2][1] -= 1
			if skill_clock[2][1] == 0:
				enemy.dfc = E_DFC
				enemy.mis = E_MIS
				print("【压制】 效果已结束。")
				sleep(interval)

		# 逐一判断所使用的技能
		if lead.mp >= 1:
			prskl()
			skill_statue = input("◈请使用技能（按回车键跳过）: ") 

			if skill_statue == "恢复":
				recovery()
				print("【恢复】 回复三倍回血的血量。")
				sleep(interval)
				if lead.hp > HP:
					lead.hp = HP
				print("你回复了", round(lead.rhp * 3, 2), "点血量。")
				sleep(interval)
				print("当前血量:", round(lead.hp, 2))
				sleep(interval)

			elif skill_statue == "强化":
				enhancement()
				print("【强化】 攻击增加 50%，持续 1 回合。")
				sleep(interval)
				print("你增加了", round(lead.atk / 3, 2), "点攻击，当前攻击:", round(lead.atk, 2))
				sleep(interval)

			elif skill_statue == "守护":
				guard()
				print("【守护】 防御增加 80%，持续 1 回合。")
				sleep(interval)
				print("你增加了", round(lead.dfc * 4 / 9, 2), "点防御，当前防御:", round(lead.dfc, 2))
				sleep(interval)

			elif skill_statue == "斩杀":
				kill_rtn = (E_HP - enemy.hp) * 0.2
				kill()
				print("【斩杀】 对目标造成 20% 目标已损生命值的伤害。")
				sleep(interval)
				if enemy.hp < 0:
					enemy.hp = 0
				print(enemy.name + "受到了", round(kill_rtn, 2), "点伤害，剩余血量:", round(enemy.hp, 2))
				sleep(interval)

			elif skill_statue == "圣光":
				if lead.mp >= 2:
					holy_light()
					print("【圣光】 增加 300% 回血，减少目标 50% 的防御，持续 2 回合。")
					sleep(interval)
					print("你增加了", round(lead.rhp / 4 * 3, 2), "点回血，当前回血:", round(lead.rhp, 2))
					sleep(interval)
					print(enemy.name + "减少了", round(enemy.dfc, 2), "点防御，剩余防御:", round(enemy.dfc, 2))
					sleep(interval)
				else:
					print("能量不足，无法使用！")
					sleep(interval)

			elif skill_statue == "诡步":
				if lead.mp >= 2:
					sneaking()
					if lead.thp > 1:
						lead.thp = 1
					if lead.crh > 1:
						lead.crh = 1
					if lead.mis > 1:
						lead.mis = 1
					print("【诡步】 增加 20% 穿透，25% 暴击率，30% 闪避，持续 2 回合。")
					sleep(interval)
					print("当前穿透:", round(lead.thp * 100, 2), "%")
					sleep(interval)
					print("当前暴击率:", round(lead.crh * 100, 2), "%")
					sleep(interval)
					print("当前闪避:", round(lead.mis * 100, 2), "%")
					sleep(interval)
				else:
					print("能量不足，无法使用！")
					sleep(interval)

			elif skill_statue == "狂暴":
				if lead.mp == 3:
					rage()
					if lead.thp > 1:
						lead.thp = 1
					if lead.fhp > 1:
						lead.fhp = 1
					if lead.crh > 1:
						lead.crh = 1
					print("【狂暴】 增加 40% 穿透，5% 吸血，30% 暴击率，75% 攻击，持续 3 回合。")
					sleep(interval)
					print("当前穿透:", round(lead.thp * 100, 2), "%")
					sleep(interval)
					print("当前吸血:", round(lead.fhp * 100, 2), "%")
					sleep(interval)
					print("当前暴击率:", round(lead.crh * 100, 2), "%")
					sleep(interval)
					print("你增加了", round(lead.atk / 7 * 3, 2), "点攻击，当前攻击:", round(lead.atk, 2))
					sleep(interval)
				else:
					print("能量不足，无法使用！")
					sleep(interval)

			elif skill_statue == "压制":
				if lead.mp == 3:
					suppress()
					print("【压制】 使目标无法防御，无法闪避，持续 1 回合。")
					sleep(interval)
					print("对方防御: 0")
					sleep(interval)
					print("对方闪避: 0 %")
					sleep(interval)
				else:
					print("能量不足，无法使用！")
					sleep(interval)

			else:
				print("跳过……")
				sleep(interval)
			print()

		# 计算伤害		
		lead_atp = lead.atk - enemy.dfc * (1 - lead.thp)
		if lead_atp < 0:
			lead_atp = 0
		enemy_atp = enemy.atk - lead.dfc * (1 - enemy.thp)
		if enemy_atp < 0:
			enemy_atp = 0
		lead_crit = "伤害"
		enemy_crit = "伤害"
		if probability(lead.crh):
			lead_atp *= lead.cre
			lead_crit = "暴击"
		if probability(enemy.crh):
			enemy_atp *= enemy.cre
			enemy_crit = "暴击"
		if probability(enemy.mis):
			print(enemy.name + "闪避了你的攻击")
			sleep(interval)
		else:
			enemy.hp -= lead_atp
			if enemy.hp < 0:
				enemy.hp = 0
			print("你对" + enemy.name + "造成了", round(lead_atp, 2), "点" + lead_crit + "，对方血量为", round(enemy.hp, 2))
			sleep(interval)
			if lead.fhp > 0 and lead.hp > 0:
				lead.hp += lead_atp * lead.fhp
				if lead.hp > HP:
					lead.hp = HP
				print("【吸血】 你回复了", round(lead_atp * lead.fhp, 2), "点血量，你的血量为", round(lead.hp, 2))
				sleep(interval)
		if probability(lead.mis):
			print("你闪避了" + enemy.name + "的攻击。")
			sleep(interval)
		else:
			lead.hp -= enemy_atp
			if lead.hp < 0:
				lead.hp = 0
			print(enemy.name + "对你造成了", round(enemy_atp, 2), "点" + enemy_crit + "，你的血量为", round(lead.hp, 2))
			sleep(interval)
			if enemy.fhp > 0 and enemy.hp > 0:
				enemy.hp += enemy_atp * enemy.fhp
				if enemy.hp > E_HP:
					enemy.hp = E_HP
				print("【吸血】 " + enemy.name + "回复了", round(enemy_atp * enemy.fhp, 2), "点血量，当前血量为", round(enemy.hp, 2))
				sleep(interval)

		# 回血
		if lead.hp > 0:
			lead.hp += lead.rhp
			if lead.hp > HP:
				lead.hp = HP
			print("你回复了", round(lead.rhp, 2), "点血量，当前血量:", round(lead.hp, 2))
		if enemy.hp > 0:
			enemy.hp += enemy.rhp
			if enemy.hp > E_HP:
				enemy.hp = E_HP
			if enemy.rhp > 0:
				print(enemy.name + "回复了", round(enemy.rhp, 2), "点血量，当前血量:", round(enemy.hp, 2))

	else:
		# 被击败
		if lead.hp == 0 and enemy.hp > 0:
			sleep(interval)
			print("\n你被" + enemy.name + "击败了。")
			sleep(interval)
			print("你感觉世界一片灰白……")
			sleep(interval)
			print("注: 5 秒后将自动退出游戏。")
			sleep(5)

		# 击败	
		elif enemy.hp == 0 and lead.hp > 0:
			sleep(interval)
			if level < 10:
				level_list[level + 1] = True
			print("\n你击败了" + enemy.name + "。")
			basic = level * 0.03
			crhhigh = 0.6  # 暴率上限
			thphigh = 0.5  # 穿透上限
			fhphigh = 0.5  # 吸血上限
			mishigh = 0.3  # 闪避上限
			hundred_crh = level * (crhhigh / 50)
			hundred_thp = level * (thphigh / 50)
			hundred_fhp = level * (fhphigh / 50)
			hundred_mis = level * (mishigh / 50)
			if level < 10:

				# 掉宝
				if probability(level / 5):
					ppt = " "
					while ppt != "血量" and ppt != "攻击" and ppt != "防御" and ppt != "暴击率" and ppt != "暴击效果" and ppt != "回血" and ppt != "穿透" and ppt != "吸血" and ppt != "闪避":
						ppt = input("◈" + enemy.name + "掉落了一个属性点，请选择加点属性: ")
						if ppt == "血量":
							HP += round(HP * basic, 2)
						elif ppt == "攻击":
							ATK += round(ATK * basic, 2)
						elif ppt == "防御":
							DFC += round(DFC * basic, 2)
						elif ppt == "暴击率":
							CRH += hundred_crh
							if CRH > crhhigh:
								CRH = crhhigh
								print("此属性已达上限! ")
								sleep(interval)
						elif ppt == "暴击效果":
							CRE += round(CRE * basic, 2)
						elif ppt == "回血":
							RHP += round(RHP * basic, 2)
						elif ppt == "穿透":
							THP += hundred_thp
							if THP > thphigh:
								THP = thphigh
								print("此属性已达上限! ")
								sleep(interval)
						elif ppt == "吸血":
							FHP += hundred_fhp
							if FHP > fhphigh:
								FHP = fhphigh
								print("此属性已达上限! ")
								sleep(interval)
						elif ppt == "闪避":
							MIS += hundred_mis
							if MIS > mishigh:
								MIS = mishigh
								print("此属性已达上限! ")
								sleep(interval)
						else:
							print("你的输入不符合规则，请重试! ")
					sleep(interval)
					print("加点成功! ")
					sleep(interval)

				if probability(level / 25):
					print(enemy.name + "掉落了一颗宝石。")
					sleep(interval)
					print("正在检测其属性: ")
					sleep(interval)
					hundred_statue = ""
					fhundred_statue = ""
					gem = choice(["血量", "攻击", "防御", "暴击率", "暴击效果", "回血", "穿透", "吸血", "闪避"])
					fgem = choice(["血量", "攻击", "防御", "暴击率", "暴击效果", "回血", "穿透", "吸血", "闪避"])
					basic_gem = basic * round(uniform(3, 6), 2)
					basic_cre_gem = basic * round(uniform(1.5, 2), 2)
					hundred_crh_gem = hundred_crh * round(uniform(3, 6), 2)
					hundred_thp_gem = hundred_thp * round(uniform(3, 6), 2)
					hundred_fhp_gem = hundred_fhp * round(uniform(3, 6), 2)
					hundred_mis_gem = hundred_mis * round(uniform(3, 6), 2)
					if gem == "血量":
						out_gem = HP * basic_gem
						hundred_statue = "点"
					if gem == "攻击":
						out_gem = ATK * basic_gem
						hundred_statue = "点"
					if gem == "防御":
						out_gem = DFC * basic_gem
						hundred_statue = "点"
					if gem == "暴击率":
						out_gem = hundred_crh_gem * 100
						hundred_statue = "%"
					if gem == "暴击效果":
						out_gem = CRE * basic_cre_gem
						hundred_statue = "点"
					if gem == "回血":
						out_gem = RHP * basic_gem
						hundred_statue = "点"
					if gem == "穿透":
						out_gem = hundred_thp_gem * 100
						hundred_statue = "%"
					if gem == "吸血":
						out_gem = hundred_fhp_gem * 100
						hundred_statue = "%"
					if gem == "闪避":
						out_gem = hundred_mis_gem * 100
						hundred_statue = "%"
					basic_fgem = basic * round(uniform(-1, -3), 2)
					basic_cre_fgem = basic * round(uniform(-0.5, -1), 2)
					hundred_crh_fgem = hundred_crh * round(uniform(-1, -3), 2)
					hundred_thp_fgem = hundred_thp * round(uniform(-1, -3), 2)
					hundred_fhp_fgem = hundred_fhp * round(uniform(-1, -3), 2)
					hundred_mis_fgem = hundred_mis * round(uniform(-1, -3), 2)
					if fgem == "血量":
						out_fgem = HP * basic_fgem
						fhundred_statue = "点"
					if fgem == "攻击":
						out_fgem = ATK * basic_fgem
						fhundred_statue = "点"
					if fgem == "防御":
						out_fgem = DFC * basic_fgem
						fhundred_statue = "点"
					if fgem == "暴击率":
						out_fgem = hundred_crh_fgem * 100
						fhundred_statue = "%"
					if fgem == "暴击效果":
						out_fgem = CRE * basic_cre_fgem
						fhundred_statue = "点"
					if fgem == "回血":
						out_fgem = RHP * basic_fgem
						fhundred_statue = "点"
					if fgem == "穿透":
						out_fgem = hundred_thp_fgem * 100
						fhundred_statue = "%"
					if fgem == "吸血":
						out_fgem = hundred_fhp_fgem * 100
						fhundred_statue = "%"
					if fgem == "闪避":
						out_fgem = hundred_mis_fgem * 100
						fhundred_statue = "%"

					print("检测成功! ")
					sleep(interval)
					print("其正属性为:", gem + "，增加", round(abs(out_gem), 2), hundred_statue)
					sleep(interval)
					print("其负属性为:", fgem + "，减少", round(abs(out_fgem), 2), fhundred_statue)
					sleep(interval)
					have_statue = input("◈是否吸收? ")
					if have_statue == "是":
						if gem == "血量":
							HP += HP * basic_gem
						if gem == "攻击":
							ATK += ATK * basic_gem
						if gem == "防御":
							DFC += DFC * basic_gem
						if gem == "暴击率":
							CRH += hundred_crh_gem
							if CRH > crhhigh:
								CRH = crhhigh
								print("此属性已达上限! ")
								sleep(interval)
						if gem == "暴击效果":
							CRE += CRE * basic_cre_gem
						if gem == "回血":
							RHP += RHP * basic_gem
						if gem == "穿透":
							THP += hundred_thp_gem
							if THP > thphigh:
								THP = thphigh
								print("此属性已达上限! ")
								sleep(interval)
						if gem == "吸血":
							FHP += hundred_fhp_gem
							if FHP > fhphigh:
								FHP = fhphigh
								print("此属性已达上限! ")
								sleep(interval)
						if gem == "闪避":
							MIS += hundred_mis_gem
							if MIS > mishigh:
								MIS = mishigh
								print("此属性已达上限! ")
								sleep(interval)

						if fgem == "血量":
							HP += HP * basic_fgem
							if HP < 1:
								HP = 1
								print("此属性已达下限! ")
								sleep(interval)
						if fgem == "攻击":
							ATK += ATK * basic_fgem
							if ATK < 0:
								ATK = 0
								print("此属性已达下限! ")
								sleep(interval)
						if fgem == "防御":
							DFC += DFC * basic_fgem
							if DFC < 0:
								DFC = 0
								print("此属性已达下限! ")
								sleep(interval)
						if fgem == "暴击率":
							CRH += hundred_crh_fgem
							if CRH < 0:
								CRH = 0
								print("此属性已达下限! ")
								sleep(interval)
						if fgem == "暴击效果":
							CRE += CRE * basic_cre_fgem
							if CRE < 0:
								CRE = 0
								print("此属性已达下限! ")
								sleep(interval)								
						if fgem == "回血":
							RHP += RHP * basic_fgem
							if RHP < 0:
								RHP = 0
								print("此属性已达下限! ")
								sleep(interval)
						if fgem == "穿透":
							THP += hundred_thp_fgem
							if THP < 0:
								THP = 0
								print("此属性已达下限! ")
								sleep(interval)
						if fgem == "吸血":
							FHP += hundred_fhp_fgem
							if FHP < 0:
								FHP = 0
								print("此属性已达下限! ")
								sleep(interval)
						if fgem == "闪避":
							MIS += hundred_mis_fgem
							if MIS < 0:
								MIS = 0
								print("此属性已达下限! ")
								sleep(interval)
							sleep(interval)
							print("已吸收。")

				print("目前属性为: ")
				sleep(interval)
				prppt(0)
				print("注: 1 秒后退出关卡。")
				sleep(1)
			else:
				con = True
		else:
			print("\n你与" + enemy.name + "同归于尽……")
			sleep(interval)
			print("你感觉世界一片灰白……")
			sleep(interval)
			if both:
				print("恭喜你触发了 【同归于尽】 彩蛋! ")
				sleep(interval)
				print("在你生命消逝的最后一刻，大家看到了你直面魔物的勇气，用圣泉水挽救了你! ")
				sleep(interval)
				print("但也由于精灵药水的副作用，你失去了一半的战斗力! ")
				sleep(interval)
				print("当前属性: ")
				HP /= 2
				MP /= 2
				ATK /= 2
				DFC /= 2
				CRH /= 2
				CRE /= 2
				RHP /= 2
				RMP /= 2
				THP /= 2
				FHP /= 2
				MIS /= 2
				sleep(interval)
				prppt(0)
				level_list[level] = True
				both = False
				print("注: 1 秒后退出关卡，本彩蛋每局只可触发一次。")
				sleep(1)
			else:
				print("注: 5 秒后将自动退出游戏。")
				sleep(5)


'''-----------------------------------------------开始游戏-----------------------------------------------'''

# 设置对话间隔
interval = float(input("请在游戏开始前设置对话的时间间隔（秒）: "))
sleep(interval)

# 公告栏
print("\n公告栏")
sleep(interval)
print("——————————————————————————————————————")
sleep(interval)
print("1.修复了天赋系统属性异常的 bug。")
sleep(interval)
print("2.修复了斩杀技能异常的 bug。")
sleep(interval)
print("3.改善了掉宝质量。")
sleep(interval)
print("4.优化了视觉体验。")
sleep(interval)
print("\n这就是本次更新的主要内容，祝各位游戏愉快! ")
sleep(interval)
print("——————————————————————————————————————")
sleep(interval)

# 讲述游戏背景
print("\n在一个遥远的地方，有一个国家，这个国家里的人，都拥有着或多或少的魔力，能够施展魔法。 ")
sleep(interval)
print("因为魔法，大家都生活得十分幸福: 农田能够自己耕种，厨房能够自己做菜，狩猎也变得更加轻松。")
sleep(interval)
print("大家本以为这样的生活能够一直这样下去，直到那一天……")
sleep(interval)
print("一位不知名的邪恶魔法师放出了至恶之物——不灭之源，它污染了四周的生灵，使其魔化。")
sleep(interval)
print("魔物烧杀抢掠，众人苦不堪言……")
sleep(interval)
print("国王通过推选，赋予你 “弑魔勇士” 的重任，前去讨伐不灭之源……")
sleep(interval)

# 输入角色名
lead_name = input("\n◈请输入你的名字（按回车键跳过）: ")
enemy_name = "None"
sleep(interval)

# 游戏规则
print("\n国王交代给你一些事情: ")
sleep(interval)
print("1.角色的能量上限为 3，每回合充能 0.5，用以使用技能。")
sleep(interval)
print("2.关卡一共 10 关，每关的怪物都有几率掉落属性点和宝石，可以改变属性。")
sleep(interval)

# 输出主角属性
print("\n正在为你随机你的天赋: ")
sleep(interval)
if lead_name == "小麦" or lead_name == "阿W" or lead_name == "滚滚" or lead_name == "车失":
	print("恭喜你发现了 【内测猿】 彩蛋! ")
	sleep(interval)
	print("感谢你们这段时间的内测，这个让玩家们破大防的游戏离不开你们的吐槽。")
	sleep(interval)
	print("为此，给予你们隐藏天赋: 唯我独尊! ")
	sleep(interval)
	HP += randint(150, 200)
	DFC += randint(10, 20)
	ATK += randint(25, 40)
	THP += round(uniform(0.3, 0.5), 2)
	CRH += round(uniform(0.4, 0.6), 2)
	CRE += round(uniform(1, 1.4), 2)
	RHP += randint(10, 20)
	FHP += round(uniform(0.3, 0.4), 2)
	MIS += round(uniform(0.1, 0.2), 2)
else:
	if talent == 1:
		HP += randint(60, 80)
		DFC += randint(3, 5)
	if talent == 2:
		ATK += randint(10, 14)
		THP += round(uniform(0.1, 0.2), 2)
	if talent == 3:
		CRH += round(uniform(0.1, 0.2), 2)
		CRE += round(uniform(0.3, 0.5), 2)
	if talent == 4:
		RHP += randint(4, 7)
		FHP += round(uniform(0.1, 0.15), 2)
	print("随机成功! 你的天赋:", talent_list[talent])
	sleep(interval)
print("\n你的属性: ")
prppt(0)
sleep(interval)

# 角色创建
lead = myclass.make_struct(lead_name, HP, MP, ATK, DFC, CRH, CRE, RHP, RMP, THP, FHP, MIS)
enemy = myclass.make_struct(enemy_name, E_HP, E_MP, E_ATK, E_DFC, E_CRH, E_CRE, E_RHP, E_RMP, E_THP, E_FHP, E_MIS)

# 进入关卡
global con
level_list = [None, True, False, False, False, False, False, False, False, False, False]
con = False
while lead.hp > 0:
	lv = input("◈请选择进入的关卡: ")
	if lv == "1" or lv == "2" or lv == "3" or lv == "4" or lv == "5" or lv == "6" or lv == "7" or lv == "8" or lv == "9" or lv == "10":
		if level_list[int(lv)]:
			start(int(lv))
		else:
			print("你还没有解锁这个关卡! ")
	else:
		print("你的输入不符合规则，请重试! ")
	# 通关
	if lead.hp > 0 and con:
		print("在你的努力下，不灭之源应声消散，国家恢复了和平……")
		sleep(interval)
		print("恭喜通关!")
		sleep(interval)
		# 彩蛋
		egg = input("\n◈按下回车键结束游戏…… ")
		if egg == "liujunyi0729":
			print("\n恭喜你发现了 【程序猿】 彩蛋! ")
			sleep(interval)
			print("没错，我就是创建这个文字游戏的程序猿，这是我爆头秃更了好久的作品。")
			sleep(interval)
			print("这次的游戏作品属于有感而发，所以做的比较赶。")
			sleep(interval)
			print("后续会增加更多有意思的机制，敬请期待! ")
			sleep(interval)
			print("这回没有彩蛋了哟，可以退出咯 ~")
			input()
		break



'''
--------------------------------------------------注解栏目--------------------------------------------------
HP:  血量
ATK: 攻击
MP:  能量
DFC: 防御
CRH: 暴率
CRE: 暴伤
RHP: 回血
RMP: 充能
THP: 穿透
FHP: 吸血
MIS: 闪避


1 能：
【恢复】 回复三倍回血的血量。
【强化】 攻击增加 50%，持续 1 回合。
【守护】 防御增加 80%，持续 1 回合。
【斩杀】 对目标造成20%目标已损生命值的伤害。

2 能：
【圣光】 增加 300% 回血，减少目标 50% 的防御，持续 2 回合。
【诡步】 增加 20% 穿透，25% 暴率，30% 闪避，持续 2 回合。

3 能：
【狂暴】 增加 80% 穿透，5% 吸血，30% 暴率，75% 攻击，持续 3 回合。
'''

