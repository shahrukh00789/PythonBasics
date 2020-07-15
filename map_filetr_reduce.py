# numbers = ["12","22","43","43","65"]
# #
# # print(numbers)
# #
# # # for i in  range(len(numbers)):
# # #     numbers[i] = int(numbers[i])
# #
# # numbers = list(map(int,numbers))
# #
# # print(numbers[3]+1)
#
# # def sq(a):
# #     return a*a
#
# num = [1,2,3,4,5,6,7,8]
#
# square = list(map(lambda x:x*x,num))
# print(square)
#
#

# def sq(a):
#     return a*a
#
# def cude(a):
#     return a*a*a
#
# func = [sq,cude]
#
# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)


#
# def is_grt_5(num):
#     return num>5
#
# list1 = [12,32,5,6,5,23,3,4]
#
# is_grt_5_yes = list(filter(is_grt_5,list1))
# print(is_grt_5_yes)

from functools import reduce

list1 = [1,2,3,4]
# num = 0
# for i in list1:
#     num = num+i
num = reduce(lambda x,y:x+y ,list1)

print(num)











