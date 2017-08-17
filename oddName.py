""""Vishula Gamaetige"""
name = str(input("what is your name: "))
while len(name) == 0:
    name = str(input("You haven't input a name, what is your name: "))
print(name[1::2])
