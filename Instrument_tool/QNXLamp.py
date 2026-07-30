from cli.QNXLamp_data import *

    #这里是指示灯页的创建
QnxLamp = tk.Frame(root,width=400, height=495,)


#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(QnxLamp,width=400,height=495)
canvas2.pack()

top_text = canvas2.create_text(50, 10, text='顶部指示灯', fill='grey', font=('微软雅黑', 10))
buttons = ['ACC', 'LCC', 'NGP', 'APA', 'VPA']
commands = [Button_ACC, Button_LCC, Button_NGP, Button_APA, Button_VPA]
for i in range(5):
    button = tk.Button(QnxLamp, text=buttons[i], command=commands[i],width=50, height=20,bd=1,image=pixel,compound="c")
    button.place(x=40 + i*70, y=30)

fixation_text = canvas2.create_text(52, 90, text='固定指示灯', fill='grey', font=('微软雅黑', 10))
buttons_F1 = [ '四门两盖','驻车灯', 'AVH灯', '主驾安全']
commands_F1 = [ Button_CarDoor, Button_Parking,Button_Auto, Button_clicksDriverSeatBelt]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_F1[i]))
    button = tk.Button(QnxLamp, text=buttons_F1[i]+'  ',image=photo,
                       command=commands_F1[i], width=85,bd=1, height=20,compound="right")
    button.place(x=20 + i*95, y=110)
    button.image = photo
#
buttons_F2 = [ '后左安全','后中安全', '后右安全', '蓄电故障']
commands_F2 = [ Button_clicksREARLEFTSeatBelt, Button_clicksREARMidSeatBelt,Button_clicksREARRitSeatBelt,
                Button_clicksBatteryFail]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_F2[i]))
    button = tk.Button(QnxLamp, text=buttons_F2[i]+'  ',image=photo,
                       command=commands_F2[i], width=85,bd=1, height=20,compound="right")
    button.place(x=20 + i*95, y=145)
    button.image = photo


buttons_F3 = [ '充电枪灯','后雾灯', '示宽灯', '近光灯']
commands_F3 = [ Button_clicksCharge, Button_clicksFogLamp,Button_clicksLED,Button_clicksLowBeam]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_F3[i]))
    button = tk.Button(QnxLamp, text=buttons_F3[i]+'  ',image=photo,
                       command=commands_F3[i], width=85,bd=1, height=20,compound="right")
    button.place(x=20 + i*95, y=180)
    button.image = photo

buttons_F4 = [ '智能远光','副驾安全']
commands_F4 = [ Button_clicksIHB, Button_clicksPaGeBelt]

for i in range(2):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_F4[i]))
    button = tk.Button(QnxLamp, text=buttons_F4[i]+'  ',image=photo,
                       command=commands_F4[i], width=85,bd=1, height=20,compound="right")
    button.place(x=210 + i*95, y=80)
    button.image = photo

unfixation_text = canvas2.create_text(57, 220, text='非固定指示灯', fill='grey', font=('微软雅黑', 10))

buttons_UF1 = [ 'ESP故障','电动故障', 'ESPOFF', 'ABS灯']
commands_UF1 = [ Button_clicksESP, Button_clicksDSP,Button_clicksESPOF,Button_clicksABS]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_UF1[i]))
    button = tk.Button(QnxLamp, text=buttons_UF1[i]+'  ',image=photo,
                       command=commands_UF1[i], width=85,bd=1, height=20,compound="right")
    button.place(x=20 + i*95, y=235)
    button.image = photo

buttons_UF2 = [ '驻车故障','转向助力', '胎压系统', '电机过热']
commands_UF2 = [ Button_clicksREQ, Button_clicksLAMP,Button_clicksTPMS,Button_clicksEMOTOR]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_UF2[i]))
    button = tk.Button(QnxLamp, text=buttons_UF2[i]+'  ',image=photo,
                       command=commands_UF2[i], width=85,bd=1, height=20,compound="right")
    button.place(x=20 + i*95, y=270)
    button.image = photo

buttons_UF3 = [ '电池切断','电池故障', '电池过热', '电池低压']
commands_UF3 = [ Button_clicksCUTOFF, Button_clicksBATT,Button_clicksBAT,Button_clicksSOCLOW]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_UF3[i]))
    button = tk.Button(QnxLamp, text=buttons_UF3[i]+'  ',image=photo,
                       command=commands_UF3[i], width=85,bd=1, height=20,compound="right")
    button.place(x=20 + i*95, y=305)
    button.image = photo

# buttons_UF4 = [ '电池故障','xxxxxx', '制动故障', 'xxxxxx']
# commands_UF4 = [ Button_clicksBATT, Button_clicksAS,Button_clicksESPB,Button_clicksHDC]
#
# for i in range(4):
#     photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_UF4[i]))
#     button = tk.Button(QnxLamp, text=buttons_UF4[i]+'  ',image=photo,
#                        command=commands_UF4[i], width=85,bd=1, height=20,compound="right")
#     button.place(x=20 + i*95, y=340)
#     button.image = photo

buttons_UF5 = [ '制动故障','电机故障', '安全气囊', '电池低温']
commands_UF5 = [ Button_clicksESPB, Button_clicksIPU,Button_clicksBCM,Button_clicksBATCOLD]

for i in range(4):
    photo = PhotoImage(file='%s\\%s.gif'%(image_path,buttons_UF5[i]))
    button = tk.Button(QnxLamp, text=buttons_UF5[i]+'  ',image=photo,
                       command=commands_UF5[i], width=85,bd=1, height=20,compound="right")
    button.place(x=20 + i*95, y=340)
    button.image = photo


    #车速

def Entry_Speed():
    i = entry_speed.get()
    CarSpeed_Data(i)
entry_speed = tk.Entry(QnxLamp, validate='key', validatecommand=vcmd, width=5, font=("Arial", 18))
entry_speed.place(x=170, y=390)
button = tk.Button(QnxLamp, text="发送", command=Entry_Speed, width=8, height=1,bd=1)
button.place(x=280, y=392)
carspeed= canvas2.create_text(100, 405, text='车速', fill='grey', font=('微软雅黑', 10))


    #ACC速度设置

def Acc_Speed():
    i = acc_speed.get()
    Acc_Speed_Data(i)
acc_speed = tk.Entry(QnxLamp, validate='key', validatecommand=vcmd, width=5, font=("Arial", 18))
acc_speed.place(x=170, y=440)
acc_button = tk.Button(QnxLamp, text="发送", command=Acc_Speed, width=8, height=1,bd=1)
acc_button.place(x=280, y=442)
accspeed= canvas2.create_text(100, 455, text='ACC速度', fill='grey', font=('微软雅黑', 10))
