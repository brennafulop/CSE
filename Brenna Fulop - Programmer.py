class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, uniform):
        super(Employee, self).__init__(name, age)
        self.uniform = uniform

    def instruction(self, boss):
        print('%s tells %s to work.' % (boss.name, self.name))


class Programmer(Employee):
    def __init__(self, name, age, uniform, computer):
        super(Programmer, self).__init__(name, age, uniform)
        self.computer = computer

    def coding(self):
        print('%s is coding' % self.name)


man = Programmer('John', '40', 'Casual', 'Macbook Air')
boss1 = Employee('Jim', '60', 'Formal')
man.work()
man.instruction(boss1)
man.coding()
