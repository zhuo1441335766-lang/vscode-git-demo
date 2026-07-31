from cli.QNX_data import *

    #这里是QNX 控制台的页面创建
    #页面大小以及按钮的位置摆放与安卓侧一致，方便代码的平移
QnxControl = tk.Frame(root,width=600, height=495)


##以下代码均平移于安卓侧


#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(QnxControl,width=600,height=495)
canvas2.pack()


    #QNX控制台

auto_line=canvas2.create_line(20,15,250,15,fill='grey')
auto_text = canvas2.create_text(1020-720, 15, text='QNX控制台', fill='grey', font=('微软雅黑', 10))
Auto_line=canvas2.create_line(350,15,580,15,fill='grey')

frametext = tk.Frame(QnxControl,width=560, height=150,bd=1)
frametext.pack_propagate(False)
frametext.place(x=20, y=40)


    #在这里设置更新显示的文本

scrollbar = tk.Scrollbar(frametext)
scrollbar.pack(side='right', fill='y')

text = tk.Text(frametext, height=10, borderwidth=2, relief="groove",  yscrollcommand=scrollbar.set)
text.insert(0.0,'')
text.configure(state='disabled')  # 设置文本框为只读状态
text.pack(side='left', fill='y')

    #将文本更新封装起来，减少代码量
def TextUpdate(Value):
    text.config(state='normal')
    text.insert('end', '\n' + System_Time() + "\n%s"%(Value))
    text.config(state='disabled')
    text.yview_moveto(1)

def Enter_QNX():
    # text.config(state='normal')
    # text.insert('end', '\n' + System_Time() + "\n正在断开安卓侧心跳，请稍后")
    # text.config(state='disabled')
    # text.yview_moveto(1)
    TextUpdate('正在断开安卓侧心跳，请稍后')
    thread = threading.Thread(target=Enter_QNX_cli)
    thread.start()
    # text.config(state='normal')
    # text.insert('end', '\n' + System_Time() + "\n已关闭安卓侧心跳")
    # text.config(state='disabled')
    TextUpdate('已关闭安卓侧心跳\n删除旧截图数据')

def Screenshot():
    thread = threading.Thread(target=Screenshot_cli)
    thread.start()
    TextUpdate('截图成功')

def PullPic():
    TextUpdate('正在拉取QNX侧截图')
    thread = threading.Thread(target=PullQnxPic_cli)
    thread.start()
    TextUpdate('拉取成功')




disable = tk.Button(QnxControl, text="进入QNX系统", command=Enter_QNX,bd=1,width=12,height=1)
disable.place(x=25, y=200)
disable = tk.Button(QnxControl, text="截图仪表", command=Screenshot,bd=1,width=12,height=1)
disable.place(x=135, y=200)
disable = tk.Button(QnxControl, text="拉取截图", command=PullPic,bd=1,width=12,height=1)
disable.place(x=245, y=200)

