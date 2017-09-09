
import requests #爬取模块
import queue
from bs4 import BeautifulSoup  #美味汤模块
import re   #正则表达式模块
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext
import time
print ("dy2018spider starting")
print ("wait 10s")
url = 'http://www.dy2018.com/html/gndy/dyzz/index.html'
hd = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
moive_url_list = [] #定义电影名称列表
def get_info():  # 定义爬取函数
    try:
        get_film = requests.get(url,headers = hd)#爬取网页
        get_film.encoding = get_film.apparent_encoding#换编码
    except:
        print("connection timeout!check your network! please try again!")
    return get_film.text #传出函数
demo = get_info() #调用并赋值
def fill_info(): #定义调整信息函数
    get_file_soup = BeautifulSoup(demo,"html.parser") #将网页信息转为soup类
    fill_film = get_file_soup.find_all('a',class_="ulink")#以标签a，属性为ulink 过滤出信息
    return fill_film #传出函数
demo_fill = fill_info() #调用并赋值
def son_info(): #定义获取最新网页中的子网页信息
    try:
        for i in demo_fill:  #定义i在demo_fill中进行for循环
            moive_url = 'http://www.dy2018.com' +i['href']#将遍历到的href接到url后面
            son_film = requests.get(moive_url) #爬取网页
            son_film.encoding = son_film.apparent_encoding#编码
            son_moive_info = son_film.text#以文本形式赋值
            son_soup = BeautifulSoup(son_moive_info,"html.parser")#转换为soup类
            son_fill_film = son_soup.find_all('a') #过滤出a标签并赋值
            for j in son_fill_film: #在sff中遍历
                pa = re.compile(r'^ftp://.*.(mkv|rmvb)')#正则表达式匹配出下载链接
                string = j['href']#当匹配到href就赋值
                match = pa.match(string)#匹配字符串
                if match:
                    moive_url_list.append(string) #增加字符串到列表中
                    moive_url_list.append('\n')#添加换行符，方便输出时不乱
    except:
        print("connection error please agine")
    return (moive_url_list)  # 传出列表
main = son_info()#调用函数
def outp():#定义输出函数
    for var in main:
        t.insert('insert',var )
root = Tk() #实例化变量名，方便调用
root.title('www.dy2018.com爬虫器')
root.geometry('1000x600')
t = Text(root,bg = 'green',width=1000)#创建文本框
t_Scrollbar = Scrollbar(root) #创建文本滚动条
t_Scrollbar.pack(side=RIGHT,fill=Y) #滚动条格式为靠右，竖式
t.pack(side=LEFT,fill=Y) #文本框为靠左，竖式
t_Scrollbar.config(command=t.yview)
t.config(yscrollcommand=t_Scrollbar.set) #文本框与滚动条绑定
button = Button(root,text = "GO",command=outp) #创建按钮，并赋予文本GO
button.pack(side=BOTTOM,before=t) #设定按钮位置为底部，文本框之后
label1=Label(root,text="developer：stone  QQ：515540070",fg='red'    )
label1.pack(side=BOTTOM,before=button)
root.mainloop() #创建一个基本窗口
time.sleep(150)