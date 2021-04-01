n = input()

num = int(n) % 2
    
if (int(n) >= 1 and int(n) <= 100): 
    if (int(n) >= 2 and int(n) <= 5):
        if (num == 0):
            print("Not Weird")
        else:
            print("Weird")
    elif (int(n) >= 6 and int(n) <= 20):
            print("Weird")
    elif (int(n) > 20):
        if (num == 0):
            print("Not Weird")
        else:
            print("Weird")


