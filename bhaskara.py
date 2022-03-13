import math

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

delta =  (math.pow(b,2)) - 4 * a * c

if(delta < 0):
    print ("esta equação não possui raízes reais")

elif(delta == 0):
    x1 = (-b + (math.sqrt(delta))) / (2 * a)
    print("a raiz desta equação é {} ".format(x1))

else:
    x1 = (-b + (math.sqrt(delta))) / (2 * a)
    x2 = (-b + (math.sqrt(delta))) / (2 * a)
    print("as raízes da equação são {} e {}".format(x1,x2))

