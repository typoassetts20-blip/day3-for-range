# Day3 
# forループとRangeの学習
# Author : Typo職人

# 1.for 
fruits = ["apple","banana","cherry"]
for fruit in fruits :
    print (fruit)

# indexアクセスではなくコレクション直でループ
# keyValue
prices = {"apple":100, "banana":200,"cherry":300 }
for key in prices :
    print(key, prices[key])

# indexがほしいなら enumerate の戻りを番号+リスト要素で受ける
# enumerate のstartで開始idx指定も可能(リスト内容は0から)
for idx,fruit in enumerate(fruits) :
    print(idx, fruit) # 0 apple , 1 banana , 2 cherry

for idx,fruit in enumerate(fruits, start= 1) :
    print(idx, fruit)  # 1 apple , 2 banana , 3 cherry

# 2.range 基本
for i in range(5) :
    print(f"i = {i}") # 0,1,2,3,4! 5はでない。

# 開始終了指定
for j in range(2,5) :
    print (f"j = {j}") # 2,3,4

# step指定
for k in range(2,10,2):
    print (f"k = {k}") # 2,4,6,8

# 負数step
for l in range(3,0,-1):
    print(f"l = {l}") # 3,2,1

# index文化対応
for m in range(len(fruits)):
    print(f"m = {m}, furit = {fruits[m]}") 
    # 0 apple , 1 banana ,2 cherry


