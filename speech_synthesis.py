'''
使用entry接收要播放的文字，点击button播放声音，使用label提示播放结束
'''
#1.创建 语音技术 客户端
from aip import AipSpeech
import os
from playsound import playsound
from tkinter import *
root=Tk()
root.title('语音合成')
root.geometry('600x200')
word_label=Label(text='请输入要合成的文字：',bg='green')
word_label.place(x=50,y=30)
word_entry=Text(width=60,height=4)
word_entry.place(x=80,y=60)
spd_text=Text(width=16,height=1)
spd_text.insert('1.0','语速(0-9):5')
spd_text.place(x=180,y=32)
pid_text=Text(width=16,height=1)
pid_text.insert('1.0','音调(0-9):5')
pid_text.place(x=290,y=32)
per_text=Text(width=16,height=1)
per_text.insert('1.0','发音人(0-4):0')
per_text.place(x=410,y=32)
global count
count=1
""" 你的 APPID AK SK """
APP_ID = '26288923'
API_KEY = '4kSBUOAU2PTjoSwZ41MznG2f'
SECRET_KEY = 'HTjAVBPBWWOmooxVkK6aPFOzaG0GXsLo'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def speak():
    text=word_entry.get('1.0',END)
    print(text)
    result  = client.synthesis(text, 'zh', 1, {'spd': eval(spd_text.get('1.8','1.9')),
                                               'pid':eval(pid_text.get('1.8','1.9')),
                                               'per':eval(per_text.get('1.9','1.10'))})
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        #wb表示以二进制方式打开文件，写入结果
        global count
        filename='audio{}.mp3'.format(count)
        count=count+1
        with open( filename, 'wb') as f:
            f.write(result)
    playsound(filename)
    word_entry.delete('1.0',END)
b=Button(text='语音播报',command=speak)
b.place(x=80,y=130)
root.mainloop()