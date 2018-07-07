#yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器，
# 当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象
#当你使用for进行迭代的时候，函数中的代码才会执行
# 第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值.
# 然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。
# def createGenerator() :
#     mylist = [x * x for x in range(3)]
#     for i in mylist:
#         print("$$$$$$$")
#         yield i
#
# generator = createGenerator()
# print(generator)
#
# for i in generator:
#     print(i)

# class Bank(): # let's create a bank, building ATMs
#     crisis = False
#     def create_atm(self) :
#         while not self.crisis :
#             yield "$100"
#會出現无尽的循环
# bc = Bank();
# atm = bc.create_atm();
# for i in atm:
#     print(i)
