import os
import time
from tkinter.constants import ACTIVE, COMMAND, FALSE, SOLID, TRUE
import tkinter.ttk as ttk
import tkinter.font
import tkinter as tk
import han as hn

hanjalist = hn.hanja

root = tk.Tk()

#폰트 설정
font1=tkinter.font.Font(family="바탕", size=20)
font=tkinter.font.Font(family="바탕", size=60)
font2=tkinter.font.Font(family="바탕", size=28)
font3=tkinter.font.Font(family="바탕", size=20)

#콤보박스: 스트링바=텍스트를 바꿔야할 때 사용/ 기본설정/선택값설정/콤보박스이름설정/초기값설정/위치설정
str=tk.StringVar()
combobox = ttk.Combobox(height=0, textvariable=str)
combobox['values']=('1-200', '201-400', '401-600', '601-800', '801-1000', '1001-1200', '1201-1400', '1401-1600', '1601-1800')
combobox.set("정렬")
combobox.current=(0)
combobox.grid(row=0,column=2)

strs=tk.StringVar()
comboboxs = ttk.Combobox(height=0, textvariable=strs, width=5)
comboboxs['values']=('0-10','0-20','0-30','10-10','10-20','10-30','20-10','20-20','20-30')
comboboxs.set("초설정")
comboboxs.current=(0)
comboboxs.grid(row=0,column=0)

#숫자출력라벨: 스트링바/초기값/기본값(위치, textvariable=변경되는텍스트값=변수, 폰트)/위치설정/위치설정2(넓이값, y좌표값)
label1 = tk.StringVar()
label1.set("0")
reallabel1 = tk.Label(anchor='s', textvariable=label1, font=font1, bg='white')
reallabel1.grid(row=1, column=0)
reallabel1.place(width=80, rely=0.45)

label = tk.StringVar()
label.set("漢")                                                   #배경선 굵기/  배경색    /선 옵션
reallabel = tk.Label(anchor='center', textvariable=label, font=font, bg='white')
reallabel.grid(row=1, column=1)
reallabel.place(width=75, rely=0.2, relx=0.20)

label3 = tk.StringVar()
label3.set("뜻")
reallabel3 = tk.Label(anchor='w', textvariable=label3, font=font3, bg='white')
reallabel3.grid(row=1, column=2)
reallabel3.place(width=180, rely=0.45, relx=0.45)

label4 = tk.StringVar()
label4.set("부수")
reallabel4 = tk.Label(anchor='w', textvariable=label4, font=font3, bg='white')
reallabel4.grid(row=2, column=1)
reallabel4.place(width=300, rely=0.7, relx=0.25)


#박스 투명도
tp=tk.DoubleVar()
tp.set(1.0)
#중지를 위한 변수
k=1
#콤보박스 값 받아온 변수
cbv=str.get()
cbv2=strs.get()
#def bttn에 들어가는 range용 변수 /d =역순용
b=int(0)
c=int(0)
d=int(1)
#초설정용
bs1=int(1)
bs2=int(2)
#유사for문용
bttni=int(0)
#일시정지용
fausei = int(0)

#combobox 값을 받아서 split한뒤 int로 바꿈
def number():
    global cbv,b,c,d,k,bttni #global k 문장은 함수 안에서 함수 밖의 k 변수를 직접 사용
    a= str.get().split("-")
    b= int(a[0])
    c= int(a[1])
    if b>c:
        d=-1
        bttni=b
    else:
        d=1
        bttni=b-2
    k= 1
    print(b,type(b),c,type(c), d)
    cl.set(str.get())
    root.update()

def setTime():
    global bs1,bs2,cbv2
    a= strs.get().split("-")
    bs1= int(a[0])
    bs2= int(a[1])

#b = 앞숫자 c=뒤 d= 앞뒤
# 실행용
def bttn():
    global b,c,d,bttni
    if k!=1:
        print("stop")
    else:
        if d==1:
            if bttni == c-1:
                bttni = b-1
                root.after(0,bttnF)
            else:
                bttni += 1
                root.after(0,bttnF)
        elif d==-1:
            if bttni == c-1:
                bttni = b-1
                root.after(0,bttnF)
            else:
                print(bttni,c)
                bttni -= 1
                root.after(0,bttnF)


def bttnF():
    global bttni
    label1.set(bttni+1) #번호
    label.set(hn.hanja[bttni][0]) #한자
    label4.set(" ")#부수
    label3.set(" ")
    root.update()
    root.after(bs1*100, bttnS) 

def bttnS():
    mean=(hn.hanja[bttni][1],hn.hanja[bttni][2])
    label3.set(mean) #뜻음
    label4.set(hn.hanja[bttni][4])
    root.update() #update 해야 반영됨
    root.after(bs2*100, bttn)

# 중지용
def bttn2():
    global k,bttni  #global k 문장은 함수 안에서 함수 밖의 k 변수를 직접 사용
    k=0
    bttni=b
    label1.set("0")
    label.set("漢")
    label3.set("stop")
    label4.set(" ")
    root.update()


def set_tp(v):
    global tp
    global scaleTP
    # either get the new volume from given argument v (type: str):
    # value = int(v)
    # or get it directly from Scale widget (type: int)
    value = scaleTP.get()
    tp.set(value)
    root.after(bs2*100, tp2)
 #바로 root.update()를 하면 재귀호출이 너무 많이 일어나므로 tp2로 나눈다
def tp2():
    root.attributes('-alpha', tp.get())
    root.update()


#일시정지용
def fause():
    global fausei,bttni,k,btnf
    if fausei==0:
        fausei=bttni
        k=0
        btnf.configure(bg='red',text='  ▶  ')
        root.update()
    else:
        k=1
        bttni=fausei-1
        btnf.configure(bg='white',text='fause')
        bttn()
        fausei=0


scaleTP=tk.Scale(root, label='Scale', resolution=0.1, from_=0.1, to=1.0, variable=tp, command=set_tp)
scaleTP.place(rely=0.2, relx=0.9)

btns=tk.Button(text="sec", command=setTime)
btns.grid(row=0, column=1)   
btn0 =tk.Button(text="set", command=number)#command=number()을 쓸 경우 안눌러도 호출해버림
btn0.grid(row=0, column=3)
btn =tk.Button(text="start", command=bttn)
btn.grid(row=0, column=4)
btn2 =tk.Button(text="stop", command=bttn2)
btn2.grid(row=0, column=5)
cl = tk.StringVar()
cl.set(str.get())
checklabel=tk.Label(textvariable=cl)
checklabel.grid(row=0, column=6)
btnf=tk.Button(text="fause", command=fause, background='white')
btnf.grid(row=4, column=1)
btnf.place(rely=0.88, relx=0.01)


#for문 속에서는 after(sec) 때문에 창 이동, 다른 def 실행할 시 딜레이 발생/after(sec,func)쓸 수도 없음
#if문으로 for문 구현해서 순차실행.

#tkinter 기본설정. 제목. 창크기설정

root.title("한자")
root.geometry("400x200+0+0")
root.configure(bg='white')
root.attributes('-topmost', 'true')
root.attributes('-alpha', tp.get())
root.mainloop()
