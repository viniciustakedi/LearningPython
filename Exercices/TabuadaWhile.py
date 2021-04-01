num = input("Insira o numero: ")

i = 0
while (i <= 10):
    account = int(num) * i
    result = str(num)+" x "+str(i)+" = "+str(account)
    print(result)
    i = i+1
    