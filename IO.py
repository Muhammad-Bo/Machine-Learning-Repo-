# Checking The Text in Lines:

# jabber = open("H:\\Python Tut\\Masterclass Assignment\\1.txt") #Open
#
# for line in jabber: # Reading
#     if "1" in line:
#         print(line)
#
# jabber.close() # Closing the File


# with open("H:\\Python Tut\\Masterclass Assignment\\1.txt") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

#Method 3

# with open("H:\\Python Tut\\Masterclass Assignment\\1.txt") as jabber:
#     lines = jabber.readline()
#
# for line in lines[::-1]:
#     print(line)

# ### Writing
# cities = ["SDN", "IOT", "SECURITY"]
# with open("H:\\Python Tut\\Masterclass Assignment\\1.txt", 'w') as city:
#     for city1 in cities:
#         print(city1, file=city)

## Binary File

with open("H:\\Python Tut\\Masterclass Assignment\\2", 'bw') as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))
