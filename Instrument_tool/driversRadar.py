from cli.driversRadar_data import *

    #这里是车手雷达页的创建
driversradar = tk.Frame(root,width=400, height=455,)
driversradar.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(driversradar,width=400,height=455)
canvas2.pack()

# auto_line=canvas2.create_line(20,10,160,10,fill='grey')
# auto_text = canvas2.create_text(200, 10, text='充电相关', fill='grey', font=('微软雅黑', 10))
# Auto_line=canvas2.create_line(240,10,380,10,fill='grey')


button_AlignFault = tk.Button(driversradar, text='打开/关闭雷达校准', command=AlignFault_cli,bd=1, width=15, height=1)
button_AlignFault.place(x=230, y=20)
button_radarfault = tk.Button(driversradar, text='打开/关闭故障卡', command=RadarFault_cli,bd=1, width=15, height=1)
button_radarfault.place(x=50, y=20)



radarinspect_text = canvas2.create_text(50, 65, text='雷达校准', fill='grey', font=('微软雅黑', 10))
button_LFinspect = tk.Button(driversradar, text='左前雷达', command=RadarLf_cli,bd=1, width=8, height=1)
button_LFinspect.place(x=50, y=95)
button_RFinspect = tk.Button(driversradar, text='右前雷达', command=RadarRF_cli,bd=1, width=8, height=1)
button_RFinspect.place(x=130, y=95)
button_LRinspect = tk.Button(driversradar, text='左后雷达', command=RadarLR_cli,bd=1, width=8, height=1)
button_LRinspect.place(x=205, y=95)
button_RRinspect = tk.Button(driversradar, text='右后雷达', command=RadarRR_cli,bd=1, width=8, height=1)
button_RRinspect.place(x=280, y=95)


    #车手模式

drivermode_line=canvas2.create_line(20,150,150,150,fill='grey')
drivermode_text = canvas2.create_text(195, 150, text='车手模式数值', fill='grey', font=('微软雅黑', 10))
drivermode2_line=canvas2.create_line(240,150,360,150,fill='grey')


def DriverMode():
    FG = entry_GFR.get()
    RG = entry_GLR.get()
    Nm = entry_Torquealue.get()
    FG_cli(FG)
    RG_cli(RG)
    Torque_cli(Nm)

G_Value_text = canvas2.create_text(50, 190, text='G值', fill='grey', font=('微软雅黑', 10))
GFR_Value_text = canvas2.create_text(120, 190, text='前后', fill='grey', font=('微软雅黑', 10))
entry_GFR = tk.Entry(driversradar, validate='key', validatecommand=vcmd, width=4, font=("Arial", 13))
entry_GFR.place(x=160, y=180)

GLR_Value_text = canvas2.create_text(255, 190, text='左右', fill='grey', font=('微软雅黑', 10))
entry_GLR = tk.Entry(driversradar, validate='key', validatecommand=vcmd, width=4, font=("Arial", 13))
entry_GLR.place(x=295, y=180)

TorqueValue_text = canvas2.create_text(50, 230, text='扭矩', fill='grey', font=('微软雅黑', 10))
TorqueFValue_text = canvas2.create_text(120, 230, text='Nm', fill='grey', font=('微软雅黑', 10))
entry_Torquealue = tk.Entry(driversradar, validate='key', validatecommand=vcmd, width=4, font=("Arial", 13))
entry_Torquealue.place(x=160, y=220)


button_RRinspect = tk.Button(driversradar, text='发送', command=DriverMode,bd=1, width=8, height=1)
button_RRinspect.place(x=255, y=230)

