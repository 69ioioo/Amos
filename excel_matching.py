import tkinter as tk
from tkinter import * 
import pandas as pd
from pandas import DataFrame
from PIL import ImageTk, Image

def SetFile():
    file1=input.get()+'.csv'
    print(file1)
    df = pd.read_csv(file1,encoding = "UTF-8")
    df_2 = df.iloc[0:,2]
    df_3 = df.iloc[0:,3]
    print(df_3.size)
    print(df_2.size)
    pk=[]
    dp=[]
    time=[]
    match=[]
    file_size=int(df_2.size)

    for i in range(0,file_size):
        pk.append(df.iloc[i,2])
        dp.append(df.iloc[i,3])
        time.append(df.iloc[i,1])
    for j in range(0,file_size):
        for k in range(0,file_size):
            if (pk[j]==dp[k] and pk[k]==dp[j] and time[j]<time[k]):
                zzz=str(time[j]) + '_'+pk[j] + '_' + str(time[k]) + '_'+pk[k]
                match.append(zzz)
                break
        
    print(match)
    export = DataFrame(match, columns= ['value'])
    export_csv = export.to_csv (r'C:\Users\Win10\Desktop\PYTHON\#'+file1, index = None, header=True)

#window
win=tk.Tk()
win.title("我ㄉ方法")
win.geometry('400x400')

#輸入
input = tk.Entry(win)
input.pack()

#Button
bt_Importer = tk.Button(win,text="File name",width=15,height=2,command=SetFile)
bt_Importer.pack()#物件ㄉ顯示

#import graph

img = ImageTk.PhotoImage(Image.open("cw.jpg"))
panel = tk.Label(win, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#file1=str(input("請輸入檔案名稱"))

win.mainloop()