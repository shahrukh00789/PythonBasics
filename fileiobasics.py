# FILEIO_ BASICS
"""
"r" open file for reading deafult
"w" open a file for writing
"x" create file if not exists
"a" add more content to a file
"t" text mode default
"b" binary mode
"+" read and write
"""

# f= open("data/srk.txt")
# read
# content = f.read()
# print(content)

# readline
# content = f.readline()
# print(content)
# print(content)

# for line in f:
#     print(line,end="")

# content = f.readline()
# print(content)
# print(content)

# content = f.readlines()
# print(type(content))
# print(content)

# f= open("data/write.txt","a")
# a = f.write("This is Writing append\n")
# print(a)


f= open("data/write.txt","r+")
# print(f.readlines())
f.write("thanks")
print(f.readlines())







f.close()