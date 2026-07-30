from cli.mileage_data import *
    #这里是里程页的创建
mileage = tk.Frame(root,width=400, height=455,)
mileage.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(mileage,width=400,height=455)
canvas2.pack()


# auto_line=canvas2.create_line(20,10,160,10,fill='grey')
# auto_text = canvas2.create_text(200, 10, text='里程相关', fill='grey', font=('微软雅黑', 10))
# Auto_line=canvas2.create_line(240,10,380,10,fill='grey')


#自启动后
SelfStart_line=canvas2.create_line(30,10,170,10,fill='grey')
auto_text = canvas2.create_text(210, 10, text='自启动后', fill='grey', font=('微软雅黑', 10))
SelfStart2_line=canvas2.create_line(250,10,390,10,fill='grey')


#启动后百公里能耗
def Distance():
    energy100km = entry_energy100km.get()
    Distance_cli(energy100km)

mileage_energy100km = canvas2.create_text(80, 50, text='百公里能耗', fill='grey', font=('微软雅黑', 10))
entry_energy100km = tk.Entry(mileage, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_energy100km.place(x=190, y=40)
mileage_energys100km = canvas2.create_text(265, 50, text='kWh', fill='grey', font=('微软雅黑', 10))
button_distance = tk.Button(mileage, text='发送', command=Distance,bd=1, width=7, height=1)
button_distance.place(x=310, y=40)



    #自启动距离与时间
def MileageDis():
    dis = entry_distance.get()
    time = entry_time.get()
    MileageDis_cli(dis,time)

def MileageTime():
    dis = entry_distance.get()
    time = entry_time.get()
    MileageTime_cli(dis,time)

mileage_distance = canvas2.create_text(80, 150, text='自启动距离', fill='grey', font=('微软雅黑', 10))
entry_distance = tk.Entry(mileage, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_distance.place(x=190, y=140)
mileage_dis = canvas2.create_text(265, 150, text='km', fill='grey', font=('微软雅黑', 10))
button_mileageDis = tk.Button(mileage, text='发送', command=MileageDis,bd=1, width=7, height=1)
button_mileageDis.place(x=310, y=140)

mileage_Time = canvas2.create_text(80, 100, text='自启动时间', fill='grey', font=('微软雅黑', 10))
entry_time = tk.Entry(mileage, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_time.place(x=190, y=90)
mileage_times = canvas2.create_text(265, 100, text='min', fill='grey', font=('微软雅黑', 10))
button_mileageTime = tk.Button(mileage, text='发送', command=MileageTime,bd=1, width=7, height=1)
button_mileageTime.place(x=310, y=90)


    #总里程
def MileagesSum():
    Value = entry_mileagesum.get()
    SumMileage_cli(Value)
mileage_sum = canvas2.create_text(80, 200, text='总里程', fill='grey', font=('微软雅黑', 10))
entry_mileagesum = tk.Entry(mileage, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_mileagesum.place(x=190, y=190)
mileage_mileagesum = canvas2.create_text(265, 200, text='km', fill='grey', font=('微软雅黑', 10))
button_mileagesum = tk.Button(mileage, text='发送', command=MileagesSum,bd=1, width=7, height=1)
button_mileagesum.place(x=310, y=190)


#自充电后
SelfCharg_line=canvas2.create_line(30,250,170,250,fill='grey')
Charg_text = canvas2.create_text(210, 250, text='自充电后', fill='grey', font=('微软雅黑', 10))
SelfCharg2_line=canvas2.create_line(250,250,390,250,fill='grey')


    #充电后里程与时间
def AfterChargingDis():
    ChargDis = entry_AfterChargDis.get()
    ChargTime = entry_AfterChargTime.get()
    AfterChargingDis_cli(ChargDis,ChargTime)

def AfterChargingTime():
    ChargTime = entry_AfterChargTime.get()
    ChargDis = entry_AfterChargDis.get()
    AfterChargingTime_cli(ChargDis,ChargTime)


mileage_AfterChargingDis = canvas2.create_text(80, 300, text='充电后里程', fill='grey', font=('微软雅黑', 10))
entry_AfterChargDis = tk.Entry(mileage, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_AfterChargDis.place(x=190, y=290)
mileage_AfterchargDis = canvas2.create_text(265, 300, text='km', fill='grey', font=('微软雅黑', 10))
button_AfterchargingDis = tk.Button(mileage, text='发送', command=AfterChargingDis,bd=1, width=7, height=1)
button_AfterchargingDis.place(x=310, y=290)

mileage_AfterChargingTime = canvas2.create_text(80, 350, text='充电后时间', fill='grey', font=('微软雅黑', 10))
entry_AfterChargTime = tk.Entry(mileage, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_AfterChargTime.place(x=190, y=340)
mileage_AfterchargTime = canvas2.create_text(265, 350, text='min', fill='grey', font=('微软雅黑', 10))
button_AfterchargingTime = tk.Button(mileage, text='发送', command=AfterChargingTime,bd=1, width=7, height=1)
button_AfterchargingTime.place(x=310, y=340)








