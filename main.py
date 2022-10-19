def supply(x,y):
    b = int((x - (x // 2)) * (y - (y // 2)))
    return b
x, y = eval(input("please input the grid :"))
print("the amount of supplies neccesary is", supply(x,y))