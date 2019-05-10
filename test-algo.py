import random

ranNum = random.randint(10,30)
print(ranNum)
sum = 0
while sum < ranNum:
    addNum =-1
    while addNum < 1 or addNum > 2:
        addNum = int(input("Add 1 or 2? "))
    sum += addNum
    print("Current number: ",sum)
    if sum == ranNum:
        print("You win")
        break
    for i in range(1,3):
        if sum == ranNum-i:
            print("Let's kill this love and win")

					   

          
