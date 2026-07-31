from cli.CarInfo_data import *
    #这里是车空信息页的创建
carinfo = tk.Frame(root,width=400, height=455,)
carinfo.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(carinfo,width=400,height=455)
canvas2.pack()


    #胎压设置
def LFT_System_cli():
    Value = entry_LFTP.get()
    LF_Tire_cli(Value)


def RFT_System_cli():
    Value = entry_RFTP.get()
    RF_Tire_cli(Value)


def LRT_System_cli():
    Value = entry_LRTP.get()
    LR_Tire_cli(Value)


def RRT_System_cli():
    Value = entry_RRTP.get()
    RR_Tire_cli(Value)


entry_LFTP = tk.Entry(carinfo, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_LFTP.place(x=45, y=20)
entry_RFTP = tk.Entry(carinfo, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_RFTP.place(x=225, y=20)
entry_LRTP = tk.Entry(carinfo, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_LRTP.place(x=45, y=70)
entry_RRTP = tk.Entry(carinfo, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_RRTP.place(x=225, y=70)

tire_buttons = ['左前胎压','右前胎压','左后胎压','右后胎压']
tire_commands = [LFT_System_cli,RFT_System_cli,LRT_System_cli,RRT_System_cli]
for i in range(4):
    if i > 1:
        button = tk.Button(carinfo, text=tire_buttons[i], command=tire_commands[i], width=55, bd=1, height=20,
                           image=pixel, compound="c")
        button.place(x=135 + (i - 2) * 180, y=70)
    else:
        button = tk.Button(carinfo, text=tire_buttons[i], command=tire_commands[i], width=55, bd=1, height=20,
                           image=pixel, compound="c")
        button.place(x=135 + i * 180, y=20)


    #轮胎胎压状态
tyre_buttons = ['左前胎压告警','右前胎压告警','左后胎压告警','右后胎压告警']
tyre_commands = [LF_State_cli,RF_State_cli,LR_State_cli,RR_State_cli]
for i in range(4):

    button = tk.Button(carinfo, text=tyre_buttons[i], command=tyre_commands[i], width=70, bd=1, height=20,
                           image=pixel, compound="c")
    button.place(x=35 + i * 95, y=120)

    #轮胎胎温状态
tyre_buttons = ['左前胎温告警','右前胎温告警','左后胎温告警','右后胎温告警']
tyre_commands = [LF_Temp_cli,RF_Temp_cli,LR_Temp_cli,RR_Temp_cli]
for i in range(4):

    button = tk.Button(carinfo, text=tyre_buttons[i], command=tyre_commands[i], width=70, bd=1, height=20,
                           image=pixel, compound="c")
    button.place(x=35 + i * 95, y=160)

    #轮胎传感器状态
tyre_buttons = ['左前传感器','右前传感器','左后传感器','右后传感器']
tyre_commands = [LF_Sensor_cli,RF_Sensor_cli,LR_Sensor_cli,RR_Sensor_cli]
for i in range(4):

    button = tk.Button(carinfo, text=tyre_buttons[i], command=tyre_commands[i], width=70, bd=1, height=20,
                           image=pixel, compound="c")
    button.place(x=35 + i * 95, y=200)

Maintenance_Mode=canvas2.create_line(20,250,140,250,fill='grey')
MaintenanceMode_text = canvas2.create_text(210, 250, text='维修模式相关', fill='grey', font=('微软雅黑', 10))
Maintenance_Mode2=canvas2.create_line(270,250,390,250,fill='grey')


#悬架维修模式
button_SuspensionMalfunction = tk.Button(carinfo, text='悬架维修', command=SuspensionMalfunction_cli,bd=1, width=12, height=1)
button_SuspensionMalfunction.place(x=50, y=270)

#前雨刮维修
button_WIPERSERVICE = tk.Button(carinfo, text='前雨刮维修', command=WIPERSERVICE_cli,bd=1, width=12, height=1)
button_WIPERSERVICE.place(x=170, y=270)

#后雨刮维修
button_RWIPERSERVICE = tk.Button(carinfo, text='后雨刮维修', command=RWIPERSERVICE_cli,bd=1, width=12, height=1)
button_RWIPERSERVICE.place(x=290, y=270)


        #拖车钩相关
TrailerHook=canvas2.create_line(20,320,140,320,fill='grey')
TrailerHook_text = canvas2.create_text(210, 320, text='拖车钩相关', fill='grey', font=('微软雅黑', 10))
TrailerHook2=canvas2.create_line(270,320,390,320,fill='grey')

#拖车钩线束连接
button_HARNCONN = tk.Button(carinfo, text='拖车线束连接', command=HARNCONN_cli,bd=1, width=12, height=1)
button_HARNCONN.place(x=50, y=340)

#拖车钩故障
button_THFault = tk.Button(carinfo, text='拖车钩故障', command=THFault_cli,bd=1, width=12, height=1)
button_THFault.place(x=170, y=340)

#拖车钩初始化
button_THInit = tk.Button(carinfo, text='拖车钩初始化', command=THInit_cli,bd=1, width=12, height=1)
button_THInit.place(x=290, y=340)

#拖车钩状态
button_THStatus = tk.Button(carinfo, text='拖车钩状态', command=THStatus_cli,bd=1, width=12, height=1)
button_THStatus.place(x=50, y=380)

#远程拖钩开关
button_RTHSwitch = tk.Button(carinfo, text='远程拖钩开关', command=RTHSwitch_cli,bd=1, width=12, height=1)
button_RTHSwitch.place(x=170, y=380)

#远程拖钩重置
button_RTHReset = tk.Button(carinfo, text='远程拖钩重置', command=RTHReset_cli,bd=1, width=12, height=1)
button_RTHReset.place(x=290, y=380)