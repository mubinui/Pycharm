
f =open("yourfile.txt","w")
f.write("Hello baby")
f.close();
g = open("yourfile.txt","r")

print(g.read())
g.close()

k = open("Text.txt","a")
k.write("I love you baby ")
k.close()
import os
os.remove("yourfile.txt")

h = open("yourfile.txt","r")
print(h.read())
h.close()


# import os
#os.rmdir("myfolder") for deleting a directory

