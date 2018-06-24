import unicodedata


#設定交錯字串是K-交錯字串
k = int(input("請設定交錯字串是K-交錯字串:"))


#判斷使用者輸入的字串是否只有大小寫
def LST_LCT(a_str,result):
    for x in a_str:
        x_1 = unicodedata.name(x)
        if x_1[:18] == LST or x_1[:20] == LCT:
            result.append(1)
        else:
            result.append(0)
#輸入交錯字串
a_str = input("請輸入一組英文字母組成的字串:")
#判定大小寫的參數
LST = 'LATIN SMALL LETTER'
LCT = 'LATIN CAPITAL LETTER'
#存放大小寫字母輸入的判定結果
result = []
#檢驗使用者輸入的字串是否只有大小寫字母
LST_LCT(a_str,result)
while 0 in result:
    result.clear()
    a_str = input("請輸入一組字串英文字母組成的字串:")
    LST_LCT(a_str,result)
  


#該題應採用剃除策略

"""參考

1. 使用del删除指定元素
li = [1, 2, 3, 4]
del li[3]
print(li)
# Output [1, 2, 3]
1
2
3
4
2. 使用list方法pop删除元素
li = [1, 2, 3, 4]
li.pop(2)
print(li)
# Output [1, 2, 4]
1
2
3
4
注：指定pop参数，将会删除该位置的元素；无参数时默认删除最后一个元素

3. 使用切片删除元素
li = [1, 2, 3, 4]
li = li[:2] + li[3:]
print(li)
# Output [1, 2, 4]
1
2
3
4
4. 使用list方法remove删除指定值的元素
li = [1, 2, 3, 4]
li.remove(3)
print(li)
# Output [1, 2, 4]

"""
    


###################
s=k
result[k-s:K]
s = s-1

先判斷前k個位址內的字元是否都是大寫或小寫，如果不是，砍掉第一個元素，累計計算變數s重新變回k
if result[k-s] == result[k-s+1] && r
else:
    remove result[k-s]
    s = k


以判斷前k個字元都是大寫或小寫後，判斷k+1個字元是否有反轉成小寫或大寫，如果不是，砍掉第一個元素，累計計算變數s重新變回k
    result[k-1] != result[k-1]
###################

進入交錯字串判定後，就開始定位，從初始切片到交錯字串中斷的最後位址要紀錄，並把這一段字串紀錄到一個另一個list裡。
然後再砍掉第一個元素，重複繼續檢測。


直到檢測到最後一個字元為止


把記錄到的所有有交錯字串的切片麻出來測量字串長度，回報字串長度。



#使用len()函數回傳字串長度
a_str_length = len(a_str)

k = 4

for x in a[:4]:
    







#使用字串切片，切出符合要求的交錯字串

"""以下為參考
起始值如果不填就代表由最前方算起，結束值如果不填就代表算到最後。例如：

string = "python"
print(string[:3])
# 輸出為 pyt
print(string[3:])
# 輸出為 hon
print(string[:])
# 輸出為 python

"""
