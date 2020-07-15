# def func1():
#     print("hellow func1")
#
# func2 = func1
#
# del func1
#
# func2()


# def funcret(num):
#     if num ==0:
#         return print
#     if num ==1:
#         return int
#
# a= funcret(0)
# print(a)


#
# def executor(func):
#     func("this")
#
# executor(print)




def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec
@dec1
def whoisharry():
    print("Harry is good boy")

# whoisharry = dec1(whoisharry)
whoisharry()