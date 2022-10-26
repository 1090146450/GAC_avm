# 导入xlwings包
import xlwings as xl
# 导入一个自定义的异常，可以使得程序出现故障后进行打印故障
from Exception.All_Exception import len_Exception


class BasePage:
    # 创建app
    app = xl.App(visible=False, add_book=False)
    # 创建工作蒲
    book = app.books.add()
    # 关闭提示信息加快运行速度
    app.display_alerts = False

    # 创建表
    def add_sheets(self, name):
        if isinstance(name, list):
            for i in range(len(name)):
                self.book.sheets.add(str(name[i]))
        else:
            self.book.sheets.add(str(name))
        return self.book.sheets

    # 单元格格式居中，默认全部单元格居中
    def cell_Center(self, bt, name="A1:S999"):
        bt.range(name).api.HorizontalAlignment = -4108

    # 添加数据，默认添加为横向添加
    def add_cell(self, bt, name, date, transpose=False):
        if transpose == False:
            bt.range(name).value = date
        else:
            bt.range(name).options(transpose=True).value = date

    # 设置单元格颜色
    def cell_colo(self, bt, name, colo=(226, 239, 218)):
        bt.range(name).color = colo

    # 设置一个区域的下划线
    def cell_Line(self, bt, name):
        for i in range(7, 13):
            bt.range(name).api.Borders(i).LineStyle = 1

    # 设置单元格列宽
    def cell_wide(self, bt, name, new_len):
        # 判断输入两个值是否为列表输入
        if isinstance(name, list) or isinstance(new_len, list):
            # 如果两个都为列表输入则判断是否长度相同
            if isinstance(name, list) and isinstance(new_len, list):
                try:
                    # 判断长度是否相同
                    if (len(name) != len(new_len)) or len(name) == 0:
                        raise len_Exception()
                #     如果不相同则会抛出异常
                except len_Exception:
                    print("请输入相同长度的两个列表，或者您输入了空列表")
                # 如果没有报错则说明列表相同
                else:
                    # 开始将每一行设置行宽
                    for i in range(0, len(name)):
                        bt.range(name[0]).column_width = new_len[0]
            # 如果列表宽不相同则抛出异常
            else:
                try:
                    raise len_Exception()
                except len_Exception:
                    print("请将参数输入两个列表或者两个单独值")
        # 只传入了一天数据后会直接进行传值
        else:
            bt.range(name).column_width = new_len

    # 单元格合并
    def cell_merge(self, bt, name):
        bt.range(name).api.Merge()

    # 退出保存
    def quit(self, id="D:/常温测试.xlsx"):
        self.book.save(id)
        self.book.close()
        self.app.quit()
