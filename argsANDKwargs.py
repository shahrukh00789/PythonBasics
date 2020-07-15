# def function_name_print(a,b,c,d):
#     print(a,b,c,d)


def funcrargs(normal,*args,**kwargs):
    print(normal)

    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(key,value)






# function_name_print("Shahrukh","Sam","Irfan","Aziz")

har = ["Shahrukh","Sam","Irfan","Aziz","Nisar"]
norm ="This is normal"
kw ={"Rohan":"Monitor","Harry":"Fitness","Theprogrammer":"Cord"}

funcrargs(norm,*har,**kw)