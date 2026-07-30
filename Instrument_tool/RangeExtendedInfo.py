from cli.RangeExtendedInfo_data import *
from ApkLog import text_In

    #这里是增程页的创建
extended = tk.Frame(root,width=400, height=455,)
extended.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(extended,width=400,height=455)
canvas2.pack()

    #发动机油量
def OilBox():
    Value = entry_OilBox.get()
    OilBox_cli(Value)

OilBoxs = canvas2.create_text(80, 50, text='发动机油量', fill='grey', font=('微软雅黑', 10))
entry_OilBox = tk.Entry(extended, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_OilBox.place(x=190, y=40)
button_OilBox = tk.Button(extended, text='发送', command=OilBox,bd=1, width=7, height=1)
button_OilBox.place(x=310, y=40)

    #发动机温度

def EngineHeat():
    Value = entry_EngineHeat.get()
    EngineHeat_cli(Value)

Heat = canvas2.create_text(80, 100, text='发动机温度', fill='grey', font=('微软雅黑', 10))
entry_EngineHeat = tk.Entry(extended, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_EngineHeat.place(x=190, y=90)
button_EngineHeat = tk.Button(extended, text='发送', command=EngineHeat,bd=1, width=7, height=1)
button_EngineHeat.place(x=310, y=90)

    #发动机转速
def EngineSpeed():
    Value = entry_EngineSpeed.get()
    EngineSpeed_cli(Value)



Enginespeed = canvas2.create_text(80, 150, text='发动机转速', fill='grey', font=('微软雅黑', 10))
entry_EngineSpeed = tk.Entry(extended, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_EngineSpeed.place(x=190, y=140)
button_EngineSpeed = tk.Button(extended, text='发送', command=EngineSpeed,bd=1, width=7, height=1)
button_EngineSpeed.place(x=310, y=140)


    #燃油里程
def OilMileage():
    Value = entry_OilMileage.get()
    OilMileage_cli(Value)

Oilmileage = canvas2.create_text(80, 200, text='燃油里程', fill='grey', font=('微软雅黑', 10))
entry_OilMileage = tk.Entry(extended, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_OilMileage.place(x=190, y=190)
button_OilMileage = tk.Button(extended, text='发送', command=OilMileage,bd=1, width=7, height=1)
button_OilMileage.place(x=310, y=190)

    #综合里程
def SyntheticalMileage():
    Value = entry_SyntheticalMileage.get()
    SyntheticalMileage_cli(Value)

Syntheticalmileage = canvas2.create_text(80, 250, text='综合里程', fill='grey', font=('微软雅黑', 10))
entry_SyntheticalMileage = tk.Entry(extended, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_SyntheticalMileage.place(x=190, y=240)
button_SyntheticalMileage = tk.Button(extended, text='发送', command=SyntheticalMileage,bd=1, width=7, height=1)
button_SyntheticalMileage.place(x=310, y=240)

    #发动机启动
button_EngineOpen = tk.Button(extended, text='发动机启动', command=EngineOpen_cli,bd=1, width=12, height=1)
button_EngineOpen.place(x=50, y=300)


# 切换纯电/增程
def SwitchCarMode():
    if SwitchCarMode_cli()==1:
        text_In('已切换到增程模式，仪表将进行重启')
    else:
        text_In('已切换到纯电模式，仪表将进行重启')

button_EngineOpen = tk.Button(extended, text='切换纯电/增程', command=SwitchCarMode,bd=1, width=12, height=1)
button_EngineOpen.place(x=250, y=300)

button_EnergyMode = tk.Button(extended, text='切换能源模式', command=EnergyMode_cli,bd=1, width=12, height=1)
button_EnergyMode.place(x=50, y=350)