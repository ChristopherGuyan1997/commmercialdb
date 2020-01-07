import sqlite3
import xlrd


# @Author  : amarao
# @File    : ExcelToDbUtils.py
# @Date    : 2019-07-16 10:36
# @Desc    : Excel 转sqlite工具
# 参考链接
# [Python初接触：SQLite和Excel操作](https://blog.csdn.net/chlk118/article/details/52702396)
# [PYTHON 连接和创建SQLite数据库](https://blog.csdn.net/ANXIN997483092/article/details/79774158)
# [Python的可变长参数](https://www.cnblogs.com/QLeelulu/archive/2009/09/09/1563148.html)
# [python获取Excel数据](https://www.cnblogs.com/mxhmxh/p/9367680.html)
# [python读取excel中单元格的内容返回的5种类型](https://www.bbsmax.com/A/Ae5RD8jNzQ/)
# [python中判断输入是否为数字(包括浮点数)](https://www.cnblogs.com/zxmbky/p/9160822.html)

class ExcelToSqlite(object):
    exe = "     执行: "
    output = "     输出: "
    sheetDataStartIndex = 1  # 数据开始计算的行数，如第0行是表头，第1行及之后是数据

    def __init__(self, dbName):
        print("初始化数据库实例")
        super(ExcelToSqlite, self).__init__()
        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()

    def __del__(self):
        print("释放数据库实例")

        self.cursor.close()
        self.conn.close()
        print('程序结束，成功释放所有游标，成功断开连接')

    def ExcelToDb(self, excelName, sheetIndex, tableName):
        """
        excel转化为sqlite数据库表
        :param excelName:excel名
        :param sheetIndex:excel中sheet位置
        :param tableName:数据库表名
        """
        print("Excel文件 转 db")
        self.tableName = tableName
        excel = xlrd.open_workbook(excelName)
        sheet = excel.sheets()[sheetIndex]  # sheets 索引
        self.sheetRows = sheet.nrows  # excel 行数
        self.sheetCols = sheet.ncols  # excle 列数
        fieldNames = sheet.row_values(0)  # 得到表头字段名
        # 创建表
        fieldTypes = ""
        for index in range(fieldNames.__len__()):
            if (index != fieldNames.__len__() - 1):
                fieldTypes += fieldNames[index] + " text,"
            else:
                fieldTypes += fieldNames[index] + " text"
        self.__CreateTable(tableName, fieldTypes)
        # 插入数据
        for rowId in range(self.sheetDataStartIndex, self.sheetRows):
            fieldValues = sheet.row_values(rowId)
            self.__Insert(fieldNames, fieldValues)

    def __CreateTable(self, tableName, field):
        """
        创建表
        :param tableName: 表名
        :param field: 字段名及类型
        :return:
        """
        print("创建表 " + tableName)
        sql = 'create table if not exists %s(%s)' % (self.tableName, field)  # primary key not null
        print(self.exe + sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def __Insert(self, fieldNames, fieldValues):
        """
        插入数据
        :param fieldNames: 字段list
        :param fieldValues: 值list
        """
        # 通过fieldNames解析出字段名
        names = ""  # 字段名，用于插入数据
        nameTypes = ""  # 字段名及字段类型，用于创建表
        for index in range(fieldNames.__len__()):
            if (index != fieldNames.__len__() - 1):
                names += fieldNames[index] + ","
                nameTypes += fieldNames[index] + " text,"
            else:
                names += fieldNames[index]
                nameTypes += fieldNames[index] + " text"
        # 通过fieldValues解析出字段对应的值
        values = ""
        for index in range(fieldValues.__len__()):
            cell_value = str((fieldValues[index]))
            if (isinstance(fieldValues[index], float)):
                cell_value = str((int)(fieldValues[index]))  # 读取的excel数据会自动变为浮点型，这里转化为文本
            if (index != fieldValues.__len__() - 1):
                values += "\'" + cell_value + "\',"
            else:
                values += "\'" + cell_value + "\'"
        # 将fieldValues解析出的值插入数据库
        sql = 'insert into %s(%s) values(%s)' % (self.tableName, names, values)
        print(self.exe + sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def Query(self, tableName):
        """
        查询数据库表中的数据
        :param tableName:表名
        """
        print("查询表 " + tableName)
        sql = 'select * from %s' % (tableName)
        print(self.exe + sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()  # 获取所有记录列表
        index = 0
        for row in results:
            print(self.output + "index=" + index.__str__() + " detail=" + str(row))  # 打印结果
            index += 1
        print(self.output + "共计" + results.__len__().__str__() + "条数据")

    def executeSqlCommand(self, sqlCommand):
        """
        执行输入的sql命令
        :param sqlCommand: sql命令
        """
        print("执行自定义sql " + tableName)
        print(self.exe + sqlCommand)
        self.cursor.execute(sqlCommand)
        results = self.cursor.fetchall()
        print(self.output + str(results))
        for index in range(0, results.__len__()):
            print(self.output + str(results[index]))
        self.conn.commit()


dbName = "wangdb"  # 数据库名,数据库不存在会自动创建，路径不存在会执行失败
tableName = "student1"  # 数据库表名，表存不存在都可以
excelName = "student.xlsx"  # excel名(可加路径)

es = ExcelToSqlite(dbName)  # 创建一个对象

es.ExcelToDb(excelName, 0, tableName)  # 对这个对象将Excel导入数据库中(每次都会导入一次，所以应该设置只运行一次)
es.Query(tableName)     # 查询数据库内容
es.executeSqlCommand("delete from " + tableName)  # 禅窟跑路，慎用
# es.executeSqlCommand("drop " + tableName)
# es.executeSqlCommand("select * from " + tableName)

