import re
txt = "Here comes the rain again falling on my head like a memory"
st = re.findall("[abc]",txt)
print(st)
sp = re.split("\s",txt)
print(sp)
#Returns a match if specified characters are at the end of the string
a = re.findall("memory\Z",txt)
print(a)
txt1 = "There you are baby"
b = re.findall("e\W",txt)
print(b)

