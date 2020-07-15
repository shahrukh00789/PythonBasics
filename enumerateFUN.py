li = ["Bhindi","Aloo","Chopstick","chowmein"]

i= 1

# for item in li:
#     if i%2!=0:
#         print(item)
#     i+=1

for index,item in enumerate(li):
    if index%2==0:
        print(item)