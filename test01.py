import BasePage

# 创建存储每一行的列表  分别代表：输入，中间条件，输出,结果
line_date = [[], [], [], []]
# 输入条件
new_input01 = ["1首次按全景开关",
               "2首次D档（一个上电周期）",
               "3R档",
               "4硬按键",
               "5软按键",
               "6语音",
               "7转向灯",
               "8N档后溜",
               "9雷达（N/D）"
               ]
# 满足条件1
new_middle01 = ["车速（影响全景进入）",
                "P档（不应影响全景进入）"
                ]
# 满足条件2
new_middle02 = ["触摸屏（不应影响全景退出）",
                "R档（软硬按键退出时不影响全景退出）",
                "切换非R档：其中P档退出30s",
                "打转向灯（不应影响全景退出）",
                "雷达检测到障碍物距离满足要求（不应影响全景退出）"
                ]
# 退出条件
new_quit = ["1车速",
            "2硬按键",
            "3软按键",
            "4P档退出",
            "5无操作30s",
            "6雷达激活雷达不满足退出",
            "7转向灯激活转向灯回正退出"
            ]
sumx = 1
# 创建Excel表格APP
bp = BasePage.BasePage()
sheet = bp.add_sheets("全景测试")
bp.cell_wide(sheet[0],"A1",40)
bp.cell_wide(sheet[0],"B1",40)
bp.cell_wide(sheet[0],"C1",40)
bp.cell_wide(sheet[0],"D1",40)
# 1、正常激活全景（输入条件1-9）
for i in range(0, len(new_input01)):
    line_date[0].append(new_input01[i])
    line_date[3].append("全景正常")
# 筛选完数据后进行填写Excel表格
bp.add_cell(sheet[0], "A" + str(sumx), line_date[0], transpose=True)
bp.add_cell(sheet[0], "D" + str(sumx), line_date[3], transpose=True)
sumx += len(line_date[0])
line_date = [[], [], [], []]
# 2、满足条件1退出全景
for i in range(0, len(new_input01)):
    for x in range(0, len(new_middle01)):
        line_date[0].append(new_input01[i])
        line_date[1].append(new_middle01[x])
        if new_middle01[x] == "车速（影响全景进入）":
            line_date[3].append("全景退出")
        else:
            line_date[3].append("全景正常")
bp.add_cell(sheet[0], "A" + str(sumx), line_date[0], transpose=True)
bp.add_cell(sheet[0], "B" + str(sumx), line_date[1], transpose=True)
bp.add_cell(sheet[0], "D" + str(sumx), line_date[3], transpose=True)
sumx += len(line_date[0])
line_date = [[], [], [], []]
# 3、激活后满足条件2退出全景
test_sum = new_middle02
while True:
    for x in range(0, len(test_sum)):
        for i in range(0, 5):
            if new_middle02[i] not in test_sum[x]:
                text = test_sum[x] + "\n" + new_middle02[i]
                if text not in test_sum:
                    test_sum.append(text)
    if len(test_sum) == 325:
        break


for i in range(0, len(new_input01)):
    for x in range(0, len(new_quit)):
        for y in range(0, len(test_sum)):
            line_date[0].append(new_input01[i])
            line_date[1].append(test_sum[y])
            line_date[2].append(new_quit[x])
            line_date[3].append("全景退出")
bp.add_cell(sheet[0], "A" + str(sumx), line_date[0], transpose=True)
bp.add_cell(sheet[0], "B" + str(sumx), line_date[1], transpose=True)
bp.add_cell(sheet[0], "C" + str(sumx), line_date[2], transpose=True)
bp.add_cell(sheet[0], "D" + str(sumx), line_date[3], transpose=True)
sumx += len(line_date[0])
line_date = [[], [], [], []]
# 4、满足输入条件后退出
for i in range(0, len(new_input01)):
    for x in range(0, len(new_quit)):
        line_date[0].append(new_input01[i])
        line_date[2].append(new_quit[x])
        line_date[3].append("全景退出")
bp.add_cell(sheet[0], "A" + str(sumx), line_date[0], transpose=True)
bp.add_cell(sheet[0], "C" + str(sumx), line_date[2], transpose=True)
bp.add_cell(sheet[0], "D" + str(sumx), line_date[3], transpose=True)
bp.quit()
