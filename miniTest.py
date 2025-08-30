# 入力された値の偶数を表示する

inputItem = int(input("任意の100までの整数を入力してください。"))
if inputItem > 100 :
    print("数字が大きすぎます")
else :
    for i in range(inputItem, 101):
        if  i % 2 == 0 :
            print (f"{i},")


