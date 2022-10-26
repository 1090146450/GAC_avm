# 导入控制Excel的包
from BasePage import BasePage

# 车速
speed = ["车速>20KM/H", "车速<=20KM/H"]
# 档位
gear = ["R档", "D档", "N档", "P档（30S）", "P档（立即）"]
# 特殊情况
special = ["转向灯未复位", "雷达条件仍满足"]
# 设置所有的情况
new_sum = []
# 设置循环
for i in range(0, len(speed)):
    for x in range(0, len(gear)):
        new_sum.append("车机画面\n" + speed[i] + "\n" + gear[x])
        if speed[i] == "车速<=20KM/H":
            new_sum.append("车机画面\n" + speed[i] + "\n" + gear[x] + "\n" + special[0])
            if gear[x] == "D档" or gear[x] == "N档":
                new_sum.append("车机画面\n" + speed[i] + "\n" + gear[x] + "\n" + special[1])
bp = BasePage()
sheet = bp.add_sheets("固定条件")
bp.add_cell(sheet[0], "A1", new_sum, transpose=True)
bp.cell_wide(sheet[0], "A1:B1", 40)
bp.quit()
