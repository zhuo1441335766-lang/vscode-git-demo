from cli.charge_data import *

    #这里是充电页的创建
charge = tk.Frame(root,width=400, height=455,)
charge.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(charge,width=400,height=455)
canvas2.pack()

# auto_line=canvas2.create_line(20,10,160,10,fill='grey')
# auto_text = canvas2.create_text(200, 10, text='充电相关', fill='grey', font=('微软雅黑', 10))
# Auto_line=canvas2.create_line(240,10,380,10,fill='grey')

def charge_cli(e):
    charge_type = combo_charge.get()
    Charge_type_cli(charge_type)

    #在这里获取当前选择的类型
combo_charge = Combobox(charge,state="readonly")
combo_charge['values'] = ('未充电','充电准备', '充电中', '充电完成', '充电故障', '预约充电', '电池加热',
            '电池冷却', '供电准备', '供电中', '供电故障', '供电停止')
combo_charge.set('未充电')
combo_charge.bind("<<ComboboxSelected>>", charge_cli)
combo_charge.place(x=80, y=10, width=90)



#充电速度状态

def ChargeSpeed_cli(e):
    charge_type = ChargeSpeed.get()
    Super_Charge_cli(charge_type)

    #在这里获取当前选择的类型
ChargeSpeed = Combobox(charge,state="readonly")
ChargeSpeed['values'] = ('选择充电速度','充电中', '快速充电中', '极速充电中')
ChargeSpeed.set('选择充电速度')
ChargeSpeed.bind("<<ComboboxSelected>>", ChargeSpeed_cli)
ChargeSpeed.place(x=280, y=10, width=100)




    #电流电压功率
def Entry_Charge():
    current = entry_current.get()
    voltage = entry_voltage.get()
    power = entry_power.get()
    Charge_cli(current,voltage,power)




#多线程执行
def Thread_Entry_Charge():
    thread = threading.Thread(target=Entry_Charge)
    thread.start()
def Thread_Charge_random():
    thread = threading.Thread(target=Charge_random_cli)
    thread.start()

    #其他信息封装齐发
def EntryOther_Charge():
    time = entry_chargetime.get()
    time_sh = entry_chargetimeh.get()
    time_sm = entry_chargetimem.get()
    powersupply = entry_powersupply.get()
    time_eh =entry_chargeendtimeh.get()
    time_em =entry_chargeendtimem.get()
    chargtime =entry_chargetime2.get()
    ChargeOther_cli(time,chargtime,time_sh,time_sm,powersupply,time_eh,time_em)

def Thread_Entry_ChargeOther():
    thread = threading.Thread(target=EntryOther_Charge)
    thread.start()

def Thread_ChargeOther_random():
    thread = threading.Thread(target=ChargeOther_random_cli)
    thread.start()




#电流电压相关信息
ChargingInformation_line=canvas2.create_line(30,45,165,45,fill='grey')
auto_text = canvas2.create_text(210, 45, text='电流电压信息', fill='grey', font=('微软雅黑', 10))
ChargingInformation_line2=canvas2.create_line(255,45,390,45,fill='grey')

entry_current = tk.Entry(charge, validate='key', validatecommand=vcmd, width=5, font=("Arial", 15))
entry_current.place(x=120, y=65)
entry_voltage = tk.Entry(charge, validate='key', validatecommand=vcmd, width=5, font=("Arial", 15))
entry_voltage.place(x=310, y=65)
entry_power = tk.Entry(charge, validate='key', validatecommand=vcmd, width=5, font=("Arial", 15))
entry_power.place(x=120, y=105)

charge_current = canvas2.create_text(80, 80, text='电流', fill='grey', font=('微软雅黑', 10))
charge_voltage = canvas2.create_text(260, 80, text='电压', fill='grey', font=('微软雅黑', 10))
charge_power = canvas2.create_text(80, 120, text='功率', fill='grey', font=('微软雅黑', 10))

charge_button = tk.Button(charge, text="发送", command=Thread_Entry_Charge, bd=1,width=34, height=20,image=pixel,compound="c")
charge_button.place(x=240, y=105)
charge_random = tk.Button(charge, text="随机发送", command=Thread_Charge_random, bd=1,width=50, height=20,image=pixel,compound="c")
charge_random.place(x=320, y=105)

#其他信息
ChargOtherInformation_line=canvas2.create_line(30,150,175,150,fill='grey')
ChargOther_text = canvas2.create_text(210, 150, text='其他信息', fill='grey', font=('微软雅黑', 10))
ChargOtherInformation_line2=canvas2.create_line(245,150,390,150,fill='grey')
entry_chargetime = tk.Entry(charge, validate='key', validatecommand=vcmd, width=5, font=("Arial", 15))
entry_chargetime.place(x=130, y=170)
charge_time = canvas2.create_text(60, 185, text='充电剩余时间', fill='grey', font=('微软雅黑', 10))
entry_powersupply = tk.Entry(charge, validate='key', validatecommand=vcmd, width=4, font=("Arial", 15))
entry_powersupply.place(x=310, y=170)
feed_cable = canvas2.create_text(260, 185, text='供电量', fill='grey', font=('微软雅黑', 10))

entry_chargetimeh = tk.Entry(charge, validate='key', validatecommand=vcmd, width=3, font=("Arial", 15))
entry_chargetimeh.place(x=210, y=210)
entry_chargetimem = tk.Entry(charge, validate='key', validatecommand=vcmd, width=3, font=("Arial", 15))
entry_chargetimem.place(x=320, y=210)
charge_starttime = canvas2.create_text(65, 225, text='预约充电开始时间', fill='grey', font=('微软雅黑', 10))
charge_starttime_m= canvas2.create_text(290, 225, text='分钟', fill='grey', font=('微软雅黑', 10))
charge_starttime_h= canvas2.create_text(170, 225, text='小时', fill='grey', font=('微软雅黑', 10))


entry_chargeendtimeh = tk.Entry(charge, validate='key', validatecommand=vcmd, width=3, font=("Arial", 15))
entry_chargeendtimeh.place(x=210, y=250)
entry_chargeendtimem = tk.Entry(charge, validate='key', validatecommand=vcmd, width=3, font=("Arial", 15))
entry_chargeendtimem.place(x=320, y=250)
charge_endtime = canvas2.create_text(65, 265, text='预约充电结束时间', fill='grey', font=('微软雅黑', 10))
charge_endtime_m= canvas2.create_text(290, 265, text='分钟', fill='grey', font=('微软雅黑', 10))
charge_endtime_h= canvas2.create_text(170, 265, text='小时', fill='grey', font=('微软雅黑', 10))
entry_chargetime2 = tk.Entry(charge, validate='key', validatecommand=vcmd, width=5, font=("Arial", 15))
entry_chargetime2.place(x=130, y=290)
charge_time2 = canvas2.create_text(60, 305, text='充电时长', fill='grey', font=('微软雅黑', 10))

chargother_button = tk.Button(charge, text="发送", command=Thread_Entry_ChargeOther, bd=1,width=34, height=20,image=pixel,compound="c")
chargother_button.place(x=240, y=325)
chargeother_random = tk.Button(charge, text="随机发送", command=Thread_ChargeOther_random, bd=1,width=50, height=20,image=pixel,compound="c")
chargeother_random.place(x=320, y=325)

# battery_style = tk.Button(charge, text="底部电池加热\预冷", command=battery_style_cli, bd=1,width=100, height=20,image=pixel,compound="c")
# battery_style.place(x=60, y=325)

def BatteryType(e):
    Battery_type = battery_type.get()
    BatteryType_cli(Battery_type)

    #在这里获取当前选择的类型
battery_type = Combobox(charge,state="readonly")
battery_type['values'] = ('选择电池状态/类型','电池加热', '电池预冷', '修改磷酸铁锂', '修改三元锂')
battery_type.set('选择电池状态/类型')
battery_type.bind("<<ComboboxSelected>>", BatteryType)
battery_type.place(x=40, y=325, width=130)





super_var = tk.IntVar()
def Get_Suoer_state():
    i = super_var.get()
    #充电开始时间获取
    time_sh = entry_chargetimeh.get()
    time_sm = entry_chargetimem.get()
    #充电结束时间获取
    time_eh =entry_chargeendtimeh.get()
    time_em =entry_chargeendtimem.get()

    FullyCharged(i,time_eh,time_em,time_sh,time_sm)



super_charge = tk.Checkbutton(charge, text = "充至充电限值",font=('微软雅黑', 10),bd=1,variable=super_var,command=Get_Suoer_state)
super_charge.place(x=230, y=290)



    #充放电限值，老车型才有的
def ChargeLimit():
    chargelimit = entry_chargelimit.get()
    dischargelimit = entry_dischargelimit.get()
    addcutdown = entry_addcutdown.get()
    ChargeLimit_cli(chargelimit,dischargelimit,addcutdown)

def Thread_ChargeLimit():
    thread = threading.Thread(target=ChargeLimit)
    thread.start()



#其他信息
ChargOldInformation_line=canvas2.create_line(30,365,150,365,fill='grey')
ChargOld_text = canvas2.create_text(210, 365, text='旧车型/大屏特有', fill='grey', font=('微软雅黑', 10))
ChargOldInformation_line2=canvas2.create_line(270,365,390,365,fill='grey')
entry_addcutdown = tk.Entry(charge, validate='key', validatecommand=vcmd, width=4, font=("Arial", 15))
entry_addcutdown.place(x=140, y=420)
entry_chargelimit = tk.Entry(charge, validate='key', validatecommand=vcmd, width=4, font=("Arial", 15))
entry_chargelimit.place(x=140, y=380)
entry_dischargelimit = tk.Entry(charge, validate='key', validatecommand=vcmd, width=4, font=("Arial", 15))
entry_dischargelimit.place(x=320, y=380)

charge_addcutdown = canvas2.create_text(60, 435, text='增加\减少续航', fill='grey', font=('微软雅黑', 10))
charge_chargelimit = canvas2.create_text(60, 395, text='充电限值', fill='grey', font=('微软雅黑', 10))
charge_dischargelimit = canvas2.create_text(240, 395, text='放电限值', fill='grey', font=('微软雅黑', 10))

chargold_button = tk.Button(charge, text="发送", command=Thread_ChargeLimit, bd=1,width=34, height=20,image=pixel,compound="c")
chargold_button.place(x=240, y=420)



