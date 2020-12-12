import os
import time
from openpyxl import *
from tkinter.constants import ACTIVE, COMMAND, FALSE, SOLID, TRUE
import tkinter.ttk as ttk
import tkinter.font
import tkinter as tk
import threading

from openpyxl.styles.colors import WHITE


#파이썬 실행 경로설정
#os.chdir('C:\PythonWorkspace\hanja')

#openpyxl 파일/시트 불러오기
load_wb = load_workbook("1800ff.xlsx", data_only=True)
load_ws = load_wb['1800']

#tkinter 기본설정. 제목. 창크기설정
root = tk.Tk()
root.title("한자")
root.geometry("400x200+0+0")
root.configure(bg='white')

#폰트 설정
font1=tkinter.font.Font(family="바탕", size=20)
font=tkinter.font.Font(family="바탕", size=34)
font2=tkinter.font.Font(family="바탕", size=28)
font3=tkinter.font.Font(family="바탕", size=20)


#콤보박스: 스트링바=텍스트를 바꿔야할 때 사용/ 기본설정/선택값설정/콤보박스이름설정/초기값설정/위치설정
str=tk.StringVar()
combobox = ttk.Combobox(height=0, textvariable=str)
combobox['values']=('1-200', '201-400', '401-600', '601-800', '801-1000', '1001-1200', '1201-1400', '1401-1600', '1601-1800')
combobox.set("정렬")
combobox.current=(0)
combobox.grid(row=0,column=0)

#숫자출력라벨: 스트링바/초기값/기본값(위치, textvariable=변경되는텍스트값=변수, 폰트)/위치설정/위치설정2(넓이값, y좌표값)
label1 = tk.StringVar()
label1.set("0")
reallabel1 = tk.Label(anchor='s', textvariable=label1, font=font1, bg='white')
reallabel1.grid(row=1, column=0)
reallabel1.place(width=65, rely=0.38)

label = tk.StringVar()
label.set("漢")                                                   #배경선 굵기/  배경색    /선 옵션
reallabel = tk.Label(anchor='center', textvariable=label, font=font, bg='white')
reallabel.grid(row=1, column=1)
reallabel.place(width=70, rely=0.3, relx=0.18)

label3 = tk.StringVar()
label3.set("뜻")
reallabel3 = tk.Label(anchor='w', textvariable=label3, font=font3, bg='white')
reallabel3.grid(row=1, column=2)
reallabel3.place(width=180, rely=0.4, relx=0.38)


#중지를 위한 변수
k=1
#콤보박스 값 받아온 변수
cbv=str.get()
#def bttn에 들어가는 range용 변수
b=int(0)
c=int(0)


#combobox 값을 받아서 split한뒤 int로 바꿈
def number():
    global cbv,b,c #global k 문장은 함수 안에서 함수 밖의 k 변수를 직접 사용
    a= str.get().split("-")
    b= int(a[0])+1
    c= int(a[1])+1
    print(b,type(b),c,type(c))
    cl.set(str.get())
    root.update()
    return c

# 실행용
def bttn():
    for i in range(b,c):
        try:
            if k!=1:
                print("stop")
                break
            else:
                label1.set(i-1) #번호
                label.set(load_ws.cell(row=i, column=2).value) #한자
                label3.set(load_ws.cell(row=i, column=3).value) #뜻음
                root.update() #update 해야 반영됨
                root.after(2000)
        except:
            break

# 중지용
def bttn2():
    label1.set("0")
    label.set("漢")
    label3.set("stop")
    global k  #global k 문장은 함수 안에서 함수 밖의 k 변수를 직접 사용
    k=0
    return k


         
btn0 =tk.Button(text="set", command=number)#command=number()을 쓸 경우 안눌러도 호출해버림
btn0.grid(row=0, column=1)
btn =tk.Button(text="start", command=bttn)
btn.grid(row=0, column=2)
btn2 =tk.Button(text="stop", command=bttn2)
btn2.grid(row=0, column=3)
cl = tk.StringVar()
cl.set(str.get())
checklabel=tk.Label(textvariable=cl)
checklabel.grid(row=0, column=4)

root.mainloop()
