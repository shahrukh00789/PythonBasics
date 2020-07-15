number = int(input("Enter Number For which you want table "))
for i in range(1,11):
    result = number*i
    print(result,end=" ")


list1 =["Shahrukh","Sam","Asif","Nadeem"]
for item in list1:
    print(item)

list_sublist =[["SAM",1],["Shahrukh",1],["Nadeem",2]]
for item in list_sublist:
    print(item)


for item,rank in list_sublist:
    print(item,rank)

