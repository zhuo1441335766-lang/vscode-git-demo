from cli.carSpeedLights_data import *

    #这里是车速与TSR页的创建
carspeelig = tk.Frame(root,width=400, height=455,)
carspeelig.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(carspeelig,width=400,height=455)
canvas2.pack()

# auto_line=canvas2.create_line(20,10,160,10,fill='grey')
# auto_text = canvas2.create_text(200, 10, text='充电相关', fill='grey', font=('微软雅黑', 10))
# Auto_line=canvas2.create_line(240,10,380,10,fill='grey')


    #车速

def Entry_Speed():
    i = entry_speed.get()
    CarSpeed_cli(i)
entry_speed = tk.Entry(carspeelig, validate='key', validatecommand=vcmd, width=5, font=("Arial", 18))
entry_speed.place(x=170, y=20)
button = tk.Button(carspeelig, text="发送", command=Entry_Speed, width=8, height=1,bd=1)
button.place(x=280, y=22)
carspeed= canvas2.create_text(100, 35, text='车速', fill='grey', font=('微软雅黑', 10))


    #ACC速度设置

def Acc_Speed():
    i = acc_speed.get()
    Acc_Speed_cli(i)
acc_speed = tk.Entry(carspeelig, validate='key', validatecommand=vcmd, width=5, font=("Arial", 18))
acc_speed.place(x=170, y=70)
acc_button = tk.Button(carspeelig, text="发送", command=Acc_Speed, width=8, height=1,bd=1)
acc_button.place(x=280, y=72)
accspeed= canvas2.create_text(100, 85, text='ACC速度', fill='grey', font=('微软雅黑', 10))



speedlimit= canvas2.create_text(120, 135, text='限速类型与限速值', fill='grey', font=('微软雅黑', 10))

    ##限速相关
def Speed_Type(e):
    speed_type = combo.get()
    Selected_cli(speed_type)

def SpeedTime_Type():
    speed_value = speed_limit.get()
    SelectedSpeed_value_cli(speed_value)

    #在这里获取当前选择的类型
combo = Combobox(carspeelig,state="readonly")
combo['values'] = ('无限速', '导航限速', '导航超速1','导航超速2','电子限速','电子超速1','电子超速2')
combo.set('无限速')
combo.bind("<<ComboboxSelected>>",Speed_Type)
combo.place(x=60, y=165, width=80)
    #在这里获取速度值
speed_limit = tk.Entry(carspeelig, validate='key', validatecommand=vcmd, width=5, font=("Arial", 18))
speed_limit.place(x=170, y=160)
speedlimit_button = tk.Button(carspeelig, text="发送", command=SpeedTime_Type, width=8, height=1,bd=1)
speedlimit_button.place(x=280, y=160)

    #红绿灯相关

trafficlight= canvas2.create_text(105, 225, text='红绿灯与读秒', fill='grey', font=('微软雅黑', 10))
def Lights_Color(e):     #红绿灯类型
    lights_type = combo_lights.get()
    Lights_cli(lights_type)

def LightsTime_Color():  # 红绿灯读秒
    light_time = lights_time.get()
    LightsTime_cli(light_time)

    #在这里获取当前选择的类型
combo_lights = Combobox(carspeelig,state="readonly")
combo_lights['values'] = ('无红绿灯', '左转绿灯', '左转黄灯','左转红灯','左转黑灯','直行绿灯','直行黄灯',
                          '直行红灯','直行黑灯','右转绿灯','右转黄灯','右转红灯','右转黑灯','掉头绿灯','掉头黄灯','掉头红灯','掉头黑灯')
combo_lights.set('无红绿灯')
combo_lights.bind("<<ComboboxSelected>>",Lights_Color)
combo_lights.place(x=60, y=255, width=80)
    #在这里获取时间值
lights_time = tk.Entry(carspeelig, validate='key', validatecommand=vcmd, width=5, font=("Arial", 18))
lights_time.place(x=170, y=250)
speedlimit_button = tk.Button(carspeelig, text="发送", command=LightsTime_Color, width=8, height=1,bd=1)
speedlimit_button.place(x=280, y=250)



    #TSR类型
tsrlrlight= canvas2.create_text(115,315, text='TSR指示灯', fill='grey', font=('微软雅黑', 10))
def speed_cli(e):
    speed_type = combo_tsr.get()
    Tsr_cli(speed_type)

    #在这里获取当前选择的类型
combo_tsr = Combobox(carspeelig,state="readonly")
combo_tsr['values'] = ('无TSR', '禁止超车', '解除超车','禁止进入','禁止通行','禁止临停','禁止泊车','禁止长停','禁机动车',
        '停车让行','减速让行','道路入口','道路出口','禁止左转','禁止右转','禁止直行','禁止掉头')
combo_tsr.set('无TSR')
combo_tsr.bind("<<ComboboxSelected>>",speed_cli)
combo_tsr.place(x=210, y=305, width=80)




