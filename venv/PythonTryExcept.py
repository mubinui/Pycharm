#we didn't define x here
try:
    print(x)
except:
    print("Exception occured")

#There are many exceptions in python
#Now we are working on name error
try:
    print(x)
except NameError:
    print("Variable name is not defined ")
except:
    print("Something else gone wrong")

# Lets work on else block
try:
    print("Hello")
except:
    print("Something goes wrong")
else:
    print("What the fuck the else is doing here ")
