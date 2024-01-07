import math as m
import pandas as pd
from IPython.display import display
pd.set_option('display.unicode.east_asian_width', True)

print('** 売り上げ予測 **')
print("各コースの人数を入力")
print("彩 : ",end='')
a = int(input())
print("結 : ",end='')
b = int(input())
print("ひむか : ",end='')
c = int(input())
print("特別郷土 : ",end='')
d = int(input())
print("伊勢海老 : ",end='')
e = int(input())
print("カルト : ",end='')
f = int(input())
print("目標金額 : ",end='')
g = int(input())
print("当月実績 : ",end='')
h = int(input())

aya = a * 4500
yui = b * 5000
him = c * 6000
kyo = d * 8000
ise = e * 10000
kar = f * 4500

data = [a,b,c,d,e,f,g]
data2 = [aya,yui,him,kyo,ise,kar]

list1 = [[a,aya,m.floor(aya/110*100)],[b,yui,m.floor(yui/110*100)],[c,him,m.floor(him/110*100)],[d,kyo,m.floor(kyo/110*100)],[e,ise,m.floor(ise/110*100)],[f,kar,m.floor(kar/110*100)]]
columns1 = ["人数","税込","税抜"]
index1 = ["彩","結い","ひむか","特別郷土","伊勢海老","カルト"]
df = pd.DataFrame(data=list1,index=index1,columns=columns1)

print('------------------------------------')

print(df)

print('合計人数',' コース：',m.floor(aya/110*100)+m.floor(yui/110*100)+m.floor(him/110*100)+m.floor(kyo/110*100)+m.floor(ise/110*100),' カルト：',m.floor(kar/110*100))
print('合計金額(税抜き):',m.floor(aya/110*100)+m.floor(yui/110*100)+m.floor(him/110*100)+m.floor(kyo/110*100)+m.floor(ise/110*100)+m.floor(kar/110*100))
print('合計金額(税込)  :',aya+yui+him+kyo+ise+kar)
print('目標金額        :',g)
print('差額            :',g-h)