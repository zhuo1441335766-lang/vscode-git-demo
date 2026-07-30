from cli.carLamp_data import *
from ApkLog import text_info
    #这里是指示灯页的创建
carlamp = tk.Frame(root,width=400, height=455,)
carlamp.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(carlamp,width=400,height=455)
canvas2.pack()

top_text = canvas2.create_text(50, 20, text='顶部指示灯', fill='grey', font=('微软雅黑', 10))
buttons = ['ACC', 'LCC', 'NGP', 'APA', 'VPA']
def VPA():
    if JudgeMaxCar() == True:
        text_info('当前为MAX车型，不支持VPA')
    else:
        Button_VPA()
commands = [Button_ACC, Button_LCC, Button_NGP, Button_APA, VPA]
for i in range(5):
    button = tk.Button(carlamp, text=buttons[i], command=commands[i],width=50, height=20,bd=1,image=pixel,compound="c")
    button.place(x=40 + i*70, y=43)

# button_RSignal = tk.Button(carlamp, text="READY", command=RangeReady,width=55, bd=1, height=20,image=pixel, compound="c")
# button_RSignal.place(x=105, y=10)
button_LSignal = tk.Button(carlamp, text="左转灯", command=LeftSignal_cli,width=55, bd=1, height=20,image=pixel, compound="c")
button_LSignal.place(x=140, y=10)
button_RSignal = tk.Button(carlamp, text="右转灯", command=RightSignal_cli,width=55, bd=1, height=20,image=pixel, compound="c")
button_RSignal.place(x=280, y=10)



"""
    逻辑为:在原有的画布中再额外创建四个画布，分别储存四种类型的指示灯
    当调用其中一个类型是，将此类型画布place展示，其他两个画布place_forget隐藏，即可实现指示灯分类选择显示
"""

#如上，额外创建一个固定指示灯画布，盖在总指示灯画布之上
Fixedlamp = tk.Frame(carlamp,width=400, height=325,)
Fixedlamp.place(x=0,y=140)

#动态指示灯画布创建
Trendslamp = tk.Frame(carlamp,width=400, height=325,)
# Trendslamp.place(x=0,y=110)

#海外指示灯画布创建
EUlamp = tk.Frame(carlamp,width=400, height=325,)
# EUlamp.place(x=0,y=110)

#燃油指示灯画布创建
Petrollamp = tk.Frame(carlamp,width=400, height=325,)
# EUlamp.place(x=0,y=110)

def ForGetAllFrame():
    Trendslamp.place_forget()
    EUlamp.place_forget()
    Fixedlamp.place_forget()
    Petrollamp.place_forget()

def FixedLamp_switch():
    ForGetAllFrame()
    Fixedlamp.place(x=0,y=140)
    button_Fixed.config(state="disabled")
    button_Trends.config(state='normal')
    button_Petrol.config(state="normal")
    button_EU.config(state='normal')



def TrendsLamp_switch():
    ForGetAllFrame()
    button_EU.config(state='normal')
    button_Fixed.config(state="normal")
    button_Petrol.config(state="normal")
    button_Trends.config(state="disabled")
    Trendslamp.place(x=0, y=140)
def EUlamp_switch():
    ForGetAllFrame()
    EUlamp.place(x=0, y=140)
    button_Trends.config(state='normal')
    button_Fixed.config(state="normal")
    button_Petrol.config(state="normal")
    button_EU.config(state="disabled")


def Petrollamp_switch():
    ForGetAllFrame()
    Petrollamp.place(x=0, y=140)
    button_Trends.config(state='normal')
    button_Fixed.config(state="normal")
    button_EU.config(state="normal")
    button_Petrol.config(state="disabled")


toptype_text = canvas2.create_text(85, 90, text='在下面选择指示灯类型', fill='grey', font=('微软雅黑', 10))
#指示灯切换按钮
button_Fixed = tk.Button(carlamp, text="固定指示灯", command=FixedLamp_switch,width=85, height=20,image=pixel, compound="c")
button_Fixed.place(x=20, y=110)
button_Trends = tk.Button(carlamp, text="动态指示灯", command=TrendsLamp_switch,width=85,height=20,image=pixel, compound="c")
button_Trends.place(x=115, y=110)
button_EU = tk.Button(carlamp, text="海外指示灯", command=EUlamp_switch,width=85,height=20,image=pixel, compound="c")
button_EU.place(x=210, y=110)
button_Petrol = tk.Button(carlamp, text="燃油指示灯", command=Petrollamp_switch,width=85,height=20,image=pixel, compound="c")
button_Petrol.place(x=305, y=110)



button_Fixed.config(state="disabled")

#固定指示灯
buttons_F1 = [ '驻车灯','示宽灯', '近光灯', '智能远光']
commands_F1 = [ Button_Parking, Button_clicksLED,Button_clicksLowBeam, Button_clicksIHB]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_F1[i]))
    Button = tk.Button(Fixedlamp, text=buttons_F1[i]+'  ',image=photo,
                           command=commands_F1[i], width=85,bd=1, height=20,compound="right")
    Button.place(x=20 + i*95, y=10)
    Button.image = photo

buttons_F2 = [ '后雾灯','主驾安全', '副驾安全', '后左安全']
commands_F2 = [ Button_clicksFogLamp, Button_clicksDriverSeatBelt,Button_clicksPaGeBelt, Button_clicksREARLEFTSeatBelt]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_F2[i]))
    Button = tk.Button(Fixedlamp, text=buttons_F2[i]+'  ',image=photo,
                           command=commands_F2[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=50)

buttons_F3 = [ '后中安全','后右安全','智能底盘']
commands_F3 = [ Button_clicksREARMidSeatBelt, Button_clicksREARRitSeatBelt,SmartChassis_cli]

for i in range(3):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_F3[i]))
    Button = tk.Button(Fixedlamp, text=buttons_F3[i]+'  ',image=photo,
                           command=commands_F3[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=90)

#动态指示灯

buttons_T1 = [ 'ABS灯','AVH灯', 'ESPOFF', 'ESP故障']
commands_T1 = [ Button_clicksABS, Button_Auto,Button_clicksESPOF, Button_clicksESP]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_T1[i]))
    Button = tk.Button(Trendslamp, text=buttons_T1[i]+'  ',image=photo,
                           command=commands_T1[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=10)

buttons_T2 = [ '安全气囊','充电枪灯', '电池低温', '电池低压']
commands_T2 = [ Button_clicksBCM, Button_clicksCharge,Button_clicksBATCOLD, Button_clicksSOCLOW]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_T2[i]))
    Button = tk.Button(Trendslamp, text=buttons_T2[i]+'  ',image=photo,
                           command=commands_T2[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=50)

buttons_T3 = [ '电池故障','电池过热', '电池切断', '电动故障']
commands_T3 = [ Button_clicksBATT, Button_clicksBAT,Button_clicksCUTOFF, Button_clicksDSP]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_T3[i]))
    Button = tk.Button(Trendslamp, text=buttons_T3[i]+'  ',image=photo,
                           command=commands_T3[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=90)

buttons_T4 = [ '电机故障','电机过热', '陡坡缓降', '功率限制']
commands_T4 = [ Button_clicksIPU, Button_clicksEMOTOR,Button_clicksHDC, Button_clicksBSP]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_T4[i]))
    Button = tk.Button(Trendslamp, text=buttons_T4[i]+'  ',image=photo,
                           command=commands_T4[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=130)

buttons_T5 = [ '后轮转向','碰撞关闭', '碰撞预警', '四门两盖']
commands_T5 = [ Button_clicksVMC, Button_clicksAEB,Button_clicksSCU, Button_CarDoor]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_T5[i]))
    Button = tk.Button(Trendslamp, text=buttons_T5[i]+'  ',image=photo,
                           command=commands_T5[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=170)

buttons_T6 = [ '胎压系统','蓄电故障', '悬挂故障', '制动故障']
commands_T6 = [ Button_clicksTPMS, Button_clicksBatteryFail,Button_clicksAS, Button_clicksESPB]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_T6[i]))
    Button = tk.Button(Trendslamp, text=buttons_T6[i]+'  ',image=photo,
                           command=commands_T6[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=210)

buttons_T6 = [ '驻车故障','转向助力', '自驾故障', '减震故障']
commands_T6 = [ Button_clicksREQ, Button_clicksLAMP,Button_clicksAutoDrivPilot, Button_clicksCDC]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_T6[i]))
    Button = tk.Button(Trendslamp, text=buttons_T6[i]+'  ',image=photo,
                           command=commands_T6[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=250)

buttons_E1 = [ '车道偏离','副驾气囊', '热管理', '居中故障']
commands_E1 = [ Button_clicksLSS, Button_clicksPassengerAirbag,Button_clicksCOOLANT, Button_clicksELccFault]
for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_E1[i]))
    Button = tk.Button(EUlamp, text=buttons_E1[i]+'  ',image=photo,
                           command=commands_E1[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=10)

buttons_E2 = [ '洗涤不足','自动变道', '限速故障','AEB重置']
commands_E2 = [ Button_clicksInsufficientWash, Button_clicksALC,Button_clicksSpeedFault,Button_clicksAEBInitialize]
for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_E2[i]))
    Button = tk.Button(EUlamp, text=buttons_E2[i]+'  ',image=photo,
                           command=commands_E2[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=50)

photo = PhotoImage(file='%s\\%s.gif'%(image_path,'拖挂房车'))
Button = tk.Button(EUlamp, text='拖挂房车'+'  ',image=photo,
                           command=Button_TrailerHook, width=85,bd=1, height=20,compound="right")
Button.image = photo
Button.place(x=20, y=90)

buttons_P1 = [ '机油警报','燃油不足', '水温警报', '排放故障']
commands_P1 = [ EngineOilAlarm_cli, FuelLow_cli,WaterHigh_cli, MilLamp_cli]
for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_P1[i]))
    Button = tk.Button(Petrollamp, text=buttons_P1[i]+'  ',image=photo,
                           command=commands_P1[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=10)

buttons_P2 = ['SVS故障']
commands_P2 = [ SVSalarm_cli]
for i in range(1):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_P2[i]))
    Button = tk.Button(Petrollamp, text=buttons_P2[i]+'  ',image=photo,
                           command=commands_P2[i], width=85,bd=1, height=20,compound="right")
    Button.image = photo
    Button.place(x=20 + i * 95, y=50)
