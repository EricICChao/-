"""
重點

python沒有XOR運算子，要自行設計
c值的作用為與a.b值結果再進行一次運算，最為同學的判斷與實際運算決果是否有落差的檢測
依題目要求，a,b是正整數，需大於0，c是邏輯值0與1


"""


'''#=====================前置作業=======================#'''


ans_word = ['AND','OR','XOR','IMPOSSIBLE']  #可輸出的內容，做成一個組合包
ans_word_TF = [0,0,0,0] #初始化邏輯運算結果，用於設計XOR運算子、a,b的邏輯運算結果存放、運算結果與c的判斷之用
ans_list = []  #最後要輸出的內容，運用list的排序特性以及該物件所提供的方法，讓回答的答案可以依序輸入，並依序輸出


#先將a,b,c設定初始值。
a = 0
b = 0
c = 0

'''#=====================前置作業=======================#'''


'''#=====================前置作業=======================#'''
'''#=====================前置作業=======================#'''


'''#=====================前置作業=======================#'''
'''#=====================前置作業=======================#'''



'''#=====================前置作業=======================#'''
'''#=====================前置作業=======================#'''


#python的input()的輸入會變成字串形式，因此必須強制轉型成int或是float等可以表示為數字形式的內容，以利後續的運算
print("請依a,b,c順序，分別輸入三個數字，其中，c必須是0或1: ")
a = int(input())             
b = int(input())
c = int(input())





#運用while敘述，控制a , b, c三個變數在輸入上遇到無效情況時，可以確保讓使用者重新輸入，依題目要求，a,b是正整數，需大於0，c是邏輯值0與1
while a<0 or b<0 or c != 1 and c != 0:
    print("請依a,b,c順序，分別輸入三個數字，其中，c必須是0或1: ")
    a = int(input())             
    b = int(input())
    c = int(input())




#設計邏輯運算子 AND、OR和XOR的判斷機制。最值觀的方式就是if...else結構，
#但是我們要考慮到第三組輸入c是邏輯值，因此我們才在上面多了一個a_and_b的邏輯運算元，用來存放a,b的邏輯判斷結果，進一步與c進行邏輯運算


if a and b == True:
    ans_list.append(ans_word[0])
    ans_word_TF[0] = 1
else:
    pass
if a or b == True:
    ans_list.append(ans_word[1])
    ans_word_TF[1] = 1
else:
    pass


#XOR運算
if ans_word_TF[0] != ans_word_TF[1]:
    ans_list.append(ans_word[2])
    ans_word_TF[2] = 1
else:
    pass


#impossibe的情況下，#需要把之前有取得的答案全部清空，只留下'IMPOSSIBLE'，採用一個變數judgement，作為與c判斷用的運算元
judgement = 0

if (ans_word_TF[0] and ans_word_TF[1] == True) or (ans_word_TF[0] or ans_word_TF[1] == True):
    judgement = 1
else:
    judgement = 0

if c != judgement:
        ans_list.clear()
        ans_list.append(ans_word[3])

#使用for迴圈，調用ans_list裡面所有依序寫入的答案
for x in ans_list:
    print(x,end='\n')   #為符合換行輸出的需求，我們可以調整print()的參數 "end"，運用end參數，可以輸出的最後加上換行符號\n，達到換行需求

#剩  0 0 0有問題
    #語言特性是否造成以下問題:
        #input()如何在同一行
        #如何在輸入時多一個空白間隔


