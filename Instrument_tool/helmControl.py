from cli.helmControl_data import *
    #这里是方控页的创建

helmcontrol = tk.Frame(root,width=400, height=455,)
helmcontrol.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(helmcontrol,width=400,height=455)
canvas2.pack()

# auto_line=canvas2.create_line(20,10,160,10,fill='grey')
# auto_text = canvas2.create_text(200, 10, text='方控相关', fill='grey', font=('微软雅黑', 10))
# Auto_line=canvas2.create_line(240,10,380,10,fill='grey')


def Lstart_count(event):
    global press_time
    press_time = time.time()

def Lstop_count(event):
    release_time = time.time()
    elapsed_time = release_time - press_time
    if elapsed_time > 0.3:
        Left_long_cli()
    else:
        Left_short_cli()

Lleft_button = tk.Button(helmcontrol, text="左 ⬅", command=Left_left_cli, bd=1,width=34, height=34,image=pixel,compound="c")
Lleft_button.place(x=127, y=75)

LLong_button = tk.Button(helmcontrol, text="左长/短按", bd=1, width=50, height=34,image=pixel,compound="c")
LLong_button.place(x=172, y=75)
LLong_button.bind('<Button-1>', Lstart_count)
LLong_button.bind('<ButtonRelease-1>', Lstop_count)



Lup_button = tk.Button(helmcontrol, text="左 ⬆", command=Left_up_cli, width=34,bd=1, height=34,image=pixel,compound="c")
Lup_button.place(x=180, y=30)

Ldown_button = tk.Button(helmcontrol, text="左 ⬇", command=Left_down_cli, width=34,bd=1, height=34,image=pixel,compound="c")
Ldown_button.place(x=180, y=120)

Lright_button = tk.Button(helmcontrol, text="左 ➡", command=Left_right_cli,bd=1, width=34, height=34,image=pixel,compound="c")
Lright_button.place(x=232, y=75)

Voice_button = tk.Button(helmcontrol, text="语音",command=Voice_cli,bd=1, width=34, height=34,image=pixel,compound="c")
Voice_button.place(x=127, y=120)

Custom_button = tk.Button(helmcontrol, text="自定义",command=Custom_cli,bd=1, width=34, height=34,image=pixel,compound="c")
Custom_button.place(x=232, y=120)



def Rstart_count(event):
    global press_time
    press_time = time.time()

def Rstop_count(event):
    release_time = time.time()
    elapsed_time = release_time - press_time
    if elapsed_time > 0.3:
        Right_long_cli()
    else:
        Right_short_cli()

Rleft_button = tk.Button(helmcontrol, text="右 ⬅", command=Right_left_cli,bd=1, width=34, height=34,image=pixel,compound="c")
Rleft_button.place(x=127, y=235)

RLong_button = tk.Button(helmcontrol, text="右长/短按", bd=1, width=50, height=34,image=pixel,compound="c")
RLong_button.place(x=172, y=235)
RLong_button.bind('<Button-1>', Rstart_count)
RLong_button.bind('<ButtonRelease-1>', Rstop_count)

Rup_button = tk.Button(helmcontrol, text="右 ⬆", command=Right_up_cli,bd=1, width=34, height=34,image=pixel,compound="c")
Rup_button.place(x=180, y=190)

Rdown_button = tk.Button(helmcontrol, text="右 ⬇", command=Right_down_cli,bd=1, width=34, height=34,image=pixel,compound="c")
Rdown_button.place(x=180, y=280)

Rright_button = tk.Button(helmcontrol, text="右 ➡",command=Right_right_cli,bd=1, width=34, height=34,image=pixel,compound="c")
Rright_button.place(x=232, y=235)

Rright_button = tk.Button(helmcontrol, text="返回",command=Return_cli,bd=1, width=34, height=34,image=pixel,compound="c")
Rright_button.place(x=127, y=280)

Rright_button = tk.Button(helmcontrol, text="静音",command=Mute_cli,bd=1, width=34, height=34,image=pixel,compound="c")
Rright_button.place(x=232, y=280)

disable = tk.Button(helmcontrol, text="雨刮灵敏速度调节", command=RainDetec_cli,bd=1,width=14,height=1)
disable.place(x=150, y=350)

text = canvas2.create_text(210, 420, text='长按滚轮按钮超过0.3秒后松开，即可进入编辑态', fill='grey', font=('微软雅黑', 10))
