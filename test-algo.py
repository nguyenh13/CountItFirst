import random

ranNum = random.randint(10,30)
print(ranNum)
sum = 0
while sum < ranNum:
    addNum =-1
    while addNum < 1 or addNum > 2:
        for j in range(0,3):
            print("PLAYER ",j," TURN")
            addNum = int(input("Add 1 or 2? "))
            sum += addNum
            if sum <= ranNum:
                print("Current number: ",sum)
                print("\n")
            if sum == ranNum or sum == ranNum+1:
                print("You win")
                break
            for i in range(1,3):
                if sum == ranNum-i :
                    print("Let's win it")
