from cli.othermation_data import *
from ApkLog import textIns
    #这里是其他文言弹窗与其他页的创建
othermation = tk.Frame(root,width=400, height=455)
othermation.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(othermation,width=400,height=455)
canvas2.pack()

# auto_line=canvas2.create_line(20,10,160,10,fill='grey')
# auto_text = canvas2.create_text(200, 10, text='文言弹窗与其他', fill='grey', font=('微软雅黑', 10))
# Auto_line=canvas2.create_line(240,10,380,10,fill='grey')

def OrdinaryNote():
    Value = entry_ordinarynote.get()
    OrdinaryNote_cli(Value)

note_text = canvas2.create_text(100, 30, text='通用文言', fill='grey', font=('微软雅黑', 10))
entry_ordinarynote = tk.Entry(othermation, validate='key', validatecommand=vcmd, width=6, font=("Arial", 13))
entry_ordinarynote.place(x=180, y=20)
ordinarynote_button = tk.Button(othermation, text='发送', command=OrdinaryNote, width=70, bd=1, height=20,image=pixel, compound="c")
ordinarynote_button.place(x=280, y=20)

def AutoNote():
    Value = entry_autonote.get()
    AutoNote_cli(Value)

autonote_text = canvas2.create_text(100, 80, text='自驾文言', fill='grey', font=('微软雅黑', 10))
entry_autonote = tk.Entry(othermation, validate='key', validatecommand=vcmd, width=6, font=("Arial", 13))
entry_autonote.place(x=180, y=70)
autonotenote_button = tk.Button(othermation, text='发送', command=AutoNote, width=70, bd=1, height=20,image=pixel, compound="c")
autonotenote_button.place(x=280, y=70)

def RPup(e):
    RPup_type = combo_RPup.get()
    Popup_cli(RPup_type)       #在这里获取当前选择的类型

combo_RPup = Combobox(othermation,state="readonly")
combo_RPup['values'] = ('无仪表弹窗', '强制下电','P挡保护1', 'P挡保护2','N挡防误触')
combo_RPup.set('无仪表弹窗')
combo_RPup.bind("<<ComboboxSelected>>", RPup)
combo_RPup.place(x=260, y=120, width=100)


def AccRange(e):
    acc_type = combo_accrange.get()
    AccRange_cli(acc_type)       #在这里获取当前选择的类型



combo_accrange = Combobox(othermation,state="readonly")
combo_accrange['values'] = ('不设置车距', '1挡','2挡', '3挡','4挡','5挡','NGP自动')
combo_accrange.set('不设置车距')
combo_accrange.bind("<<ComboboxSelected>>", AccRange)
combo_accrange.place(x=70, y=120, width=100)


def Observatory():
    if Observatory_cli() == True:
        textIns.config(state='normal')
        textIns.insert('end', '\n'+System_Time()+"\n已模拟车辆进入地理围栏雷达限制区域")
        textIns.config(state='disabled')
        textIns.yview_moveto(1)
    else:
        textIns.config(state='normal')
        textIns.insert('end', '\n'+System_Time()+"\n已模拟车辆离开地理围栏雷达限制区域")
        textIns.config(state='disabled')
        textIns.yview_moveto(1)

button_Observatory = tk.Button(othermation, text='模拟进入雷达受限区', command=Observatory,bd=1, width=15, height=1)
button_Observatory.place(x=70, y=160)

button_IgOff = tk.Button(othermation, text='模拟仪表短暂IG 0FF', command=InstrumentIGOff_cli,bd=1, width=15, height=1)
button_IgOff.place(x=70, y=220)

def IntoFNGP():
    if Intofngp_cli() == True:
        textIns.config(state='normal')
        textIns.insert('end', '\n'+System_Time()+"\n仪表已进入FNGP，请在大屏选择路线")
        textIns.config(state='disabled')
        textIns.yview_moveto(1)
    else:
        textIns.config(state='normal')
        textIns.insert('end', '\n'+System_Time()+"\n仪表已退出FNGP")
        textIns.config(state='disabled')
        textIns.yview_moveto(1)
button_InFNGP = tk.Button(othermation, text='模拟FNGP状态', command=IntoFNGP,bd=1, width=15, height=1)
button_InFNGP.place(x=260, y=160)


def DiDiIgOn():
    if DiDiIgOn_cli() == True:
        textIns.config(state='normal')
        textIns.insert('end', '\n'+System_Time()+"\n已模拟台架上电")
        textIns.config(state='disabled')
        textIns.yview_moveto(1)
    else:
        textIns.config(state='normal')
        textIns.insert('end', '\n'+System_Time()+"\n已模拟台架下电")
        textIns.config(state='disabled')
        textIns.yview_moveto(1)
button_DiDiIgOn = tk.Button(othermation, text='模拟DD车型台架上电', command=IntoFNGP,bd=1, width=15, height=1)
button_DiDiIgOn.place(x=260, y=220)
