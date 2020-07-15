# i = 0
# while(True):
#     if i+1 < 5:
#         i=i+1
#         continue
#     print(i+1)
#     if(i == 44):
#         break
#     i=i+1



while(True):
    input_data = int(input("Enter Your Number"))
    if input_data > 100:
        print("Congrats you have enter number greater than 100")
        break
    else:
        print("Try Again")
        continue



