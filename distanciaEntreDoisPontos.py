import math

x1 = int(print("Digite o x1"))
y1 = int(print("Digite o x2"))
x2 = int(print("Digite o y1"))
y2 = int(print("Digite o y2"))

d = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))

if(d >= 10):
    print("longe")

else:
    print ("perto")