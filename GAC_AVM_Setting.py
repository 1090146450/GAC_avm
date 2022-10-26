# 1、正常激活全景（输入条件1-9）
def input_01(self):
    sum_new = []
    for i in range(0, len(self)):
        # 添加A、B、C、D列的数据
        one_new = [self[i], "", "", "全景正常"]
        sum_new.append(one_new)
    return sum_new,len(sum_new)


# 2、满足条件1退出全景
def input_02(self, middle1):
    sum_new = []
    for i in range(0, len(self)):
        for x in range(0, len(middle1)):
            # 添加A、B、C、D列的数据
            one_new = [self[i], middle1[x], ""]
            if middle1[x] == "车速（影响全景进入）":
                one_new.append("全景退出")
            else:
                one_new.append("全景正常")
            sum_new.append(one_new)
    return sum_new,len(sum_new)


# 3、激活后满足条件2退出全景 self输入条件，middle01中间条件，new_quit退出条件
def input_03(self, middle01, new_quit):
    # 中间条件的所有的组合情况
    sum_middle01 = middle01
    # 获取所有的组合情况
    while True:
        for i in range(0, len(sum_middle01)):
            for x in range(0, 5):
                if middle01[x] not in sum_middle01[i]:
                    text = sum_middle01[x] + "\n" + middle01[i]
                    if text not in sum_middle01:
                        sum_middle01.append(text)
        if len(sum_middle01) == 325:
            break
    # 创建所有返回条件
    new_sum = []
    # 将中间条件和前提条件组合
    for i in range(0, len(self)):
        for x in range(0, len(sum_middle01)):
            for y in range(0, len(new_quit)):
                new_sum.append([self[i], sum_middle01[x], new_quit[y], "全景退出"])
    return new_sum,len(new_sum)


# 4、满足输入条件后退出 self输入，new_quit退出
def input_04(self, new_quit):
    new_sum = []
    for i in range(0, len(self)):
        for x in range(0, len(new_quit)):
            new_sum.append([self[i], "", new_quit[x], "全景退出"])
    return new_sum,len(new_sum)
