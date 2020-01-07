#!/usr/bin/python
import sqlite3


# conn = sqlite3.connect('test.db')
# print('opened database successfully')
# c = conn.cursor()


def create():
    conn = sqlite3.connect('test.db')
    print('1opened database successfully')
    c = conn.cursor()
    c.execute("CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR(50),SALARY REAL)")
    print("2Table created successfully")
    conn.commit()
    c.close()
    conn.close()


def insert():
    conn = sqlite3.connect('test.db')
    print('3opened database successfully')
    c = conn.cursor()
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
    print("4Records created successfully")
    conn.commit()
    c.close()
    conn.close()


def select():
    conn = sqlite3.connect('test.db')
    print('5opened database successfully')
    c = conn.cursor()
    cursor = c.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    print("6Operation done successfully")
    conn.commit()
    c.close()
    conn.close()


def update():
    conn = sqlite3.connect('test.db')
    print('7opened database successfully')
    c = conn.cursor()
    c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    conn.commit()
    print("8Total number of rows updated :", conn.total_changes)
    conn.commit()
    c.close()
    conn.close()


def delete():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("9Opened database successfully")
    c.execute("DELETE from COMPANY where ID=2;")
    conn.commit()
    print("10Total number of rows deleted :", conn.total_changes)
    conn.commit()
    c.close()
    conn.close()


def show_all():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("11Opened database successfully")
    cursor = c.execute("SELECT id, name, address, salary from COMPANY")
    values = cursor.fetchall() #取出所有的记录
    print('ssssssss')
    print(values)
    print("12Operation done successfully")
    conn.commit()
    c.close()
    conn.close()


def main():
    try:
        create()
    except Exception as e:
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        print("13Opened database successfully")
        conn.execute('DROP TABLE COMPANY')
        conn.commit()
        c.close()
        conn.close()

        create()
    finally:
        pass
    insert()
    select()
    update()
    delete()
    show_all()


if __name__ == '__main__':
  main()
