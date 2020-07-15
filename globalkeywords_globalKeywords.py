# global_var = 10;
#
# def testing(str):
#     # global_var = 10+14  #local Variable
#     global global_var
#     global_var = global_var + 45
#     print(str,global_var)
#     return
#
# testing("Shahrukh khan")
# print(global_var)

def firstfunction():
    x= 88
    def secondfunction():
        global x
        x= 109
        print(x)
    secondfunction()
    print(x)

firstfunction()
