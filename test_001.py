import copy
import math

import GAC_AVM_Setting

new = [["触摸屏", "切换R档", "切换非R档"],
       ["非转向灯激活全景，打转向灯", "非雷达激活全景，雷达条件满足"]]


def order_array(self):
    # 0代表每次循环的数 1代表总数  使用时要考虑深浅拷贝问题
    new_sum = [copy.copy(self), copy.copy(self)]
    t = 0
    # 设置死循环保证数量够才能输出
    while True:
        # 循环的次数，你循环几个数就减一就行
        if t == (len(self) - 1):
            break
        new_list = []
        # 第一次循环主要是存储每一波的值例如两位数【12,13,23....】
        for i in range(0, len(new_sum[0])):
            # 这次循环主要是要遍历的初始值【1,2,3】
            for x in range(0, len(self)):
                # 这里的筛选条件是防止出现重复的例如：【1,11】
                if self[x] not in new_sum[0][i]:
                    # 下面的test_number数是结合后的数字，是要往最终结果输入的
                    test_number = new_sum[0][i] + self[x]
                    # 这里可以对要添加的数进行筛选
                    if (self[1] in test_number) and (self[2] in test_number):
                        continue
                    else:
                        new_list.append(test_number)
        # 将每一组数来添加到要循环的数组中
        new_sum[0] = new_list
        # 将每一组数添加到要返回的总列表中
        new_sum[1] += new_list
        # 将t自加，计算经过了几轮
        t += 1
    return new_sum[1]

