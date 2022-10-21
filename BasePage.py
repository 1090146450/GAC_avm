import xlwings as xl


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
    def cell_wide(self, bt, name, len):
        if isinstance(name,list) or isinstance(len,list):
            for i in 
        bt.range(name).column_width = len

    # 单元格合并
    def cell_merge(self, bt, name):
        bt.range(name).api.Merge()

    # 退出保存
    def quit(self, id="D:/常温测试.xlsx"):
        self.book.save(id)
        self.book.close()
        self.app.quit()