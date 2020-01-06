


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_score(self):
        print('%s: %s' % (self.name, self.age))

    def change(self, a, b):
        self.name = a
        self.age = b
        print('%s: %s' % (self.name, self.age))

    def delete(self):
        self.name = None
        self.age = None
        print('%s: %s' % (self.name, self.age))

    def get_age(self):
        if self.age <= 30:
            return '少年'
        elif self.age >= 30:
            return '中年'
        else:
            return '狗屁'

bart4 = Student('guyan', 23)
bart4.print_score()
print(bart4.get_age())
bart4.change('luyaliang',54)
print(bart4.get_age())
bart4.delete()

bart5 = Student('gujufang',10)
bart5.sex = 'male'
print(bart5.get_age(), bart5.sex)

# bart4.get_age()
'''
bart = Student('sd',111)
bart.name= 'chanping'
print(bart.name)
bart.print_score()
bart2 = Student('houwangye',79)
print(bart2.name)

def cha_ru(a,b):
    bart3= Student(a,b)
    print(bart3.name,bart3.age)
cha_ru('guyan',23)

'''