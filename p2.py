import unicodedata

#設定交錯字串是K-交錯字串
k = int(input("請設定交錯字串是K-交錯字串:"))


#判斷使用者輸入的字串是否只有大小寫，將結果轉成0,1,2的形式，以利後續的判斷機制的設計
def LST_LCT(a_str,result):
    for x in a_str:
        x_1 = unicodedata.name(x)
        if x_1[:18] == LST:
            result.append(1)       #如果是小寫字母，存入1
        elif x_1[:20] == LCT:
            result.append(2)       #如果是大寫字母，存入2       
        else:
            result.append(0)
#輸入交錯字串
a_str = input("請輸入一組英文字母組成的字串:")
#判定大小寫的參數
LST = 'LATIN SMALL LETTER'
LCT = 'LATIN CAPITAL LETTER'
#存放大小寫字母輸入的判定結果，後續的判斷會使用到
result = []
#檢驗使用者輸入的字串是否只有大小寫字母
LST_LCT(a_str,result)
while 0 in result:
    result.clear()
    a_str = input("請輸入一組字串英文字母組成的字串:")
    LST_LCT(a_str,result)


#該題應採用剃除策略，逐一比對並剔除不符合條件之元素，執行該策略需要有以下的準備:
#存放被截取的交錯字串長度
interlaced_strings = []
#使用len()函數回傳字串長度，len()也可用於計算list的元素數量，所以也可透過檢測result[]內的元素數量可得知輸入的字串長度
a_str_length = len(a_str)  
#用於要控制交錯字串判斷的迴圈次數，依字串的長度要進行多次的迴圈運算
s = a_str_length 
#交錯字串初始位址，用於以下判斷迴圈控制，預設是第0個字元
strat_add = 0
#交錯字串最後位址，用於以下判斷迴圈控制，預設是第0個字元
end_add = 0
control_list = []   #用於暫存要判斷用的字串     

"""
進行k長度的字串切片
依據交錯字串條件進行迴圈判斷
判斷完畢之後，將字串的第一個元素剪除，成為一新字串，繼續下一輪的交錯字串判斷，
直到字串無法再切片為止
"""


while s != 0:
    if s - s%k >0:
        num_times = int(a_str_length/k)    #設計一控制數，用於控制字串切片的次數以及切片位址。使用int強制轉換商數成整數，因為尾巴餘數不會符合交錯字串條件，因此可以直接忽略，留下整數的結果。
        #先進行字串切片
        while num_times > 0:   
            end_add = num_times*k - 1
            start_add = end_add - k + 1   #因為字串是0~7，所以要再加回1。
            if len(set(result[start_add:end_add])) == 1:                     #透過len(set())組合，可以判斷切片裡是否都是同一種元素，因為前面已將大小寫轉換成1,2，所以可以用該方式進行判斷
                control_list.append(result[start_add:end_add])
                num_times = num_times - 1
            else:
                pass


#進行字串長度計算(可能有問題的地方)
        if len(control_list) >1:    #當判斷用的交錯字串切片有兩個以上
            a = len(control_list)    #迴圈次數控制器
            interlaced_strings_length = k #當有兩個以上符合字串切片被存入於暫存判斷用的字串切片list中時，依照題目說明，至少會有長度k的交錯字串，因此初始化為k
            while a > 0:
                if control_list[a-1][0] != result[a-2][k-1]:   #判斷暫存要判斷用的字串切片list裡面，前面字串的最後一個元素是否和後面字串的第一個元素是否不同，如不同，表示前後兩者是交錯字串，兩者的長度要列入計算
                    interlaced_strings_length = interlaced_strings_length + k
                else:
                    pass
                a = a - 1  #計算完成後，要讓迴圈次數控制器減1，準備執行下一輪的計算
            interlaced_strings.append(interlaced_strings_length)
        elif len(control_list) == 1:      #當判斷用的交錯字串切片有1個時
            interlaced_strings.append(k)  #如果至少有一組切片符合交錯字串的條件，至少就有一組k個長度的交錯字串
        else:
            interlaced_strings.append(0)  #要留一組讓max()可以判斷
        #計算完成後，進行第一個元素的刪除，迴圈次數控制器減1，準備執行下一輪的計算，暫存判斷字串的list要清除
        result.pop(0)
        s = s -1
        control_list.clear()
    else:
        break

    
print(max(interlaced_strings), end = '\n')  #運用max()判斷在所有的切片結果中，找出所存入的最長的字串長度的紀錄

