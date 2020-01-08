#python sqlite
#Author : Hongten
#Create : 2013-08-09
#Version: 1.0
#DB-API 2.0 interface for SQLite databases
import sqlite3
import os
'''SQLite数据库是一款非常小巧的嵌入式开源数据库软件，也就是说
没有独立的维护进程，所有的维护都来自于程序本身。
在python中，使用sqlite3创建数据库的连接，当我们指定的数据库文件不存在的时候
连接对象会自动创建数据库文件；如果数据库文件已经存在，则连接对象不会再创建
数据库文件，而是直接打开该数据库文件。
  连接对象可以是硬盘上面的数据库文件，也可以是建立在内存中的，在内存中的数据库
  执行完任何操作后，都不需要提交事务的(commit)
  创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
  创建在内存上面： conn = sqlite3.connect('"memory:')
  下面我们一硬盘上面创建数据库文件为例来具体说明：
  conn = sqlite3.connect('c:\\test\\hongten.db')
  其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：
    commit()      --事务提交
    rollback()     --事务回滚
    close()       --关闭一个数据库链接
    cursor()      --创建一个游标
  cu = conn.cursor()
  这样我们就创建了一个游标对象：cu
  在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
  对于游标对象cu，具有以下具体操作：
    execute()      --执行一条sql语句
    executemany()    --执行多条sql语句
    close()       --游标关闭
    fetchone()     --从结果中取出一条记录
    fetchmany()     --从结果中取出多条记录
    fetchall()     --从结果中取出所有记录
    scroll()      --游标滚动
'''
#global var
#数据库文件绝句路径
DB_FILE_PATH = ''
#表名称
TABLE_NAME = ''
#是否打印sql
SHOW_SQL = True
def get_conn(path):
  '''获取到数据库的连接对象，参数为数据库文件的绝对路径
  如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
  路径下的数据库文件的连接对象；否则，返回内存中的数据接
  连接对象'''
  conn = sqlite3.connect(path)
  if os.path.exists(path) and os.path.isfile(path):
    print('硬盘上面:[{}]'.format(path))
    return conn
  else:
    conn = None
    print('内存上面:[:memory:]')
    return sqlite3.connect(':memory:')
def get_cursor(conn):
  '''该方法是获取数据库的游标对象，参数为数据库的连接对象
  如果数据库的连接对象不为None，则返回数据库连接对象所创
  建的游标对象；否则返回一个游标对象，该对象是内存中数据
  库连接对象所创建的游标对象'''
  if conn is not None:
    return conn.cursor()
  else:
    return get_conn('').cursor()
###############################################################
####      创建|删除表操作   START
###############################################################
def drop_table(conn, table):
  '''如果表存在,则删除表，如果表中存在数据的时候，使用该
  方法的时候要慎用！'''
  if table is not None and table != '':
      sql = 'DROP TABLE IF EXISTS ' + table
      if SHOW_SQL:
          print('执行sql:[{}]'.format(sql))
      cu = get_cursor(conn)
      cu.execute(sql)
      conn.commit()
      print('删除数据库表[{}]成功!'.format(table))
      close_all(conn, cu)
  else:
      print('the [{}] is empty or equal None!'.format(table))


def create_table(conn, sql):
  '''创建数据库表：student'''
  if sql is not None and sql != '':
    cu = get_cursor(conn)
    if SHOW_SQL:
      print('执行sql:[{}]'.format(sql))
    cu.execute(sql)
    conn.commit()
    print('创建数据库表[student]成功!')
    close_all(conn, cu)
  else:
    print('the [{}] is empty or equal None!'.format(sql))
###############################################################
####      创建|删除表操作   END
###############################################################
def close_all(conn, cu):
  '''关闭数据库游标对象和数据库连接对象'''
  try:
    if cu is not None:
      cu.close()
  finally:
    if conn is not None:                                           #我把这里的cu改成了conn!!!!
      conn.close()
###############################################################
####      数据库操作CRUD   START
###############################################################
def save(conn, sql, data):
  '''插入数据'''
  if sql is not None and sql != '':
    if data is not None:
      cu = get_cursor(conn)
      for d in data:
        if SHOW_SQL:
          print('执行sql:[{}],参数:[{}]'.format(sql, d))
        cu.execute(sql, d)
        conn.commit()
      close_all(conn, cu)
  else:
    print('the [{}] is empty or equal None!'.format(sql))
def fetchall(conn, sql):
  '''查询所有数据'''
  if sql is not None and sql != '':
    cu = get_cursor(conn)
    if SHOW_SQL:
      print('执行sql:[{}]'.format(sql))
    cu.execute(sql)
    r = cu.fetchall()
    if len(r) > 0:
      for e in range(len(r)):
        print(r[e])
  else:
    print('the [{}] is empty or equal None!'.format(sql))
def fetchone(conn, sql, data):
  '''查询一条数据'''
  if sql is not None and sql != '':
    if data is not None:
      #Do this instead
      d = (data,)
      cu = get_cursor(conn)
      if SHOW_SQL:
        print('执行sql:[{}],参数:[{}]'.format(sql, data))
      cu.execute(sql, d)
      r = cu.fetchall()
      if len(r) > 0:
        for e in range(len(r)):
          print(r[e])
    else:
      print('the [{}] equal None!'.format(data))
  else:
    print('the [{}] is empty or equal None!'.format(sql))
def update(conn, sql, data):
  '''更新数据'''
  if sql is not None and sql != '':
    if data is not None:
      cu = get_cursor(conn)
      for d in data:
        if SHOW_SQL:
          print('执行sql:[{}],参数:[{}]'.format(sql, d))
        cu.execute(sql, d)
        conn.commit()
      close_all(conn, cu)
  else:
    print('the [{}] is empty or equal None!'.format(sql))
def delete(conn, sql, data):
  '''删除数据'''
  if sql is not None and sql != '':
    if data is not None:
      cu = get_cursor(conn)
      for d in data:
        if SHOW_SQL:
          print('执行sql:[{}],参数:[{}]'.format(sql, d))
        cu.execute(sql, d)
        conn.commit()
      close_all(conn, cu)
  else:
    print('the [{}] is empty or equal None!'.format(sql))
###############################################################
####      数据库操作CRUD   END
###############################################################
###############################################################
####      测试操作   START
###############################################################
def drop_table_test():
  '''删除数据库表测试'''
  print('删除数据库表测试...')
  conn = get_conn(DB_FILE_PATH)
  drop_table(conn, TABLE_NAME)
def create_table_test(command_create):
  '''创建数据库表测试'''
  print('创建数据库表测试...')
  create_table_sql = command_create
  conn = get_conn(DB_FILE_PATH)
  create_table(conn, create_table_sql)
def save_test(command_save,command_savedata):
  '''保存数据测试...'''
  print('保存数据测试...')
  save_sql = command_save
  data = command_savedata
  conn = get_conn(DB_FILE_PATH)
  save(conn, save_sql, data)
def fetchall_test(command_showall):
  '''查询所有数据...'''
  print('查询所有数据...')
  fetchall_sql = command_showall
  conn = get_conn(DB_FILE_PATH)
  fetchall(conn, fetchall_sql)
def fetchone_test(command_showone):
  '''查询一条数据...'''
  print('查询一条数据...')
  fetchone_sql = command_showone
  data = 3
  conn = get_conn(DB_FILE_PATH)
  fetchone(conn, fetchone_sql, data)
def update_test(command_update,command_updatedata):
  '''更新数据...'''
  print('更新数据...')
  update_sql = command_update
  data = command_updatedata
  conn = get_conn(DB_FILE_PATH)
  update(conn, update_sql, data)
def delete_test(command_delete,command_deletedata):
  '''删除数据...'''
  print('删除数据...')
  delete_sql = command_delete
  data = command_deletedata
  conn = get_conn(DB_FILE_PATH)
  delete(conn, delete_sql, data)
###############################################################
####      测试操作   END
###############################################################



def init():
  '''初始化方法'''
  #数据库文件绝句路径
  global DB_FILE_PATH
  DB_FILE_PATH = '焊接刀总览表.db'                        #这里是新建的数据库的名称
  #数据库表名称
  global TABLE_NAME
  TABLE_NAME = '焊接刀总览表'
  #是否打印sql
  global SHOW_SQL
  SHOW_SQL = True
  print('show_sql : {}'.format(SHOW_SQL))
  #如果存在数据库表，则删除表
  drop_table_test()
  #创建数据库表student
  create_table_test(command_create)
  #向数据库表中插入数据
  save_test(command_save,command_savedata)


def main():
  init()
  fetchall_test(command_showall)
  print('#' * 50)
  fetchone_test(command_showone)
  print('#' * 50)
  update_test(command_update, command_updatedata)
  fetchall_test(command_showall)
  print('#' * 50)
  delete_test(command_delete, command_deletedata)
  fetchall_test(command_showall)

#建立表格，表格内容的每一列的列名写在这里
command_create = '''CREATE TABLE `焊接刀总览表` (
             `序号` int(11) NOT NULL,
             `焊接刀规格` varchar(20) NOT NULL,
             `熔接刀申请数` int(11) DEFAULT NULL,
             `熔接刀入库数` int(11) DEFAULT NULL,
             `焊接刀出库数` int(11) DEFAULT NULL,
             `熔接刀库存数` int(11) DEFAULT NULL,
             `库位` varchar(20) NOT NULL,
             `备注` varchar(20) NOT NULL,
              PRIMARY KEY (`序号`)
            )'''

#插入需要插入的数据
command_save = '''INSERT INTO 焊接刀总览表 values (?, ?, ?, ?, ?, ?,?,?)'''
command_savedata = [(1, '20454-20p', 5, 5, -4, 1, 'A1','备注'),
      (2, '20454-30p', 20, 20, -4, 16, 'A2','备注'),
      (3, '20454-40p', 20, 20, -4, 16, 'A3','备注'),
      (4, '20454-50p', 10, 10, -4, 6, 'A4','备注')]

#查询总览表的情况
command_showall = '''SELECT * FROM 焊接刀总览表'''
command_showone = 'SELECT * FROM 焊接刀总览表 WHERE 序号 = ? '

#修改指定的数据，事例是更新序号是？时的焊接刀规格
command_update = 'UPDATE 焊接刀总览表 SET 焊接刀规格 = ? WHERE 序号 = ? '
command_updatedata = [('改动1号焊接刀的规格', 1),
      ('改动2号焊接刀的规格', 2),
      ('改动3号焊接刀的规格', 3),
      ('改动4号焊接刀的规格', 4)]

#删除指定的数据，下例是删除满足序号是？和焊接刀规格是？的数据，因为之前修改过，所以现在的规格是修稿后的规格
command_delete = 'DELETE FROM 焊接刀总览表 WHERE 焊接刀规格 = ? AND 序号 = ? '
command_deletedata = [('改动1号焊接刀的规格', 1),
      ('改动2号焊接刀的规格', 3)]

if __name__ == '__main__':
  main()