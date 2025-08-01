#---------------File Handling---------------

# file = open("Data.txt", "r")
# print(file.read())
# print(file.readline())
# print(file.readlines())

# file = open("Data.txt", "w")
# file.write("Hello World")

# file = open("Data.txt", "a")
# file.write("\nHi World")


# copy data from 1 to other file
file = open("Data.txt", "r")
file2 = open("CopiedData.txt", "w")


for data in file:
    file2.write(data)

file2.close()
# file2 = open("CopiedData.txt", "r")
# print(file2.read())


with open("CopiedData.txt", "r") as file:
    print(file.read())

print(file.read())