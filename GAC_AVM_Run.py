# 导入打开Excel包和配置文件
import BasePage, GAC_AVM_Setting as se

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
# 用来统计每一块会占EXCEL多少行
sumx = 1
# 创建Excel程序
bp = BasePage.BasePage()
# 创建表格名称为  全景测试
sheet = bp.add_sheets("全景测试")
# 设置列宽
bp.cell_wide(sheet[0], "A1:D1", 45)
# 存储所有调用方法
new_dict = [se.input_01(new_input01), se.input_02(new_input01, new_middle01),
            se.input_03(new_input01, new_middle02, new_quit), se.input_04(new_input01, new_quit)]
for i in range(0, 4):
    bp.add_cell(sheet[0], "A" + str(sumx), new_dict[i][0])
    sumx += new_dict[i][1]
# 退出
bp.quit()
