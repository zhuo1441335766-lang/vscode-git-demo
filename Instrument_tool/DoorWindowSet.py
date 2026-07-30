from cli.DoorWindowSet_data import *

    #这里是门窗设置页的创建
dwset = tk.Frame(root,width=400, height=455,)
dwset.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(dwset,width=400,height=455)
canvas2.pack()


    #左侧滑门状态
def LSlideDoorStatus_cli(e):
    LSlideDoorStatus_type = LSlideDoorStatus.get()
    LSlideDoor_type_cli(LSlideDoorStatus_type)

LSlideDoorStatus = Combobox(dwset,state="readonly")
LSlideDoorStatus['values'] = ( '未知状态','左门故障', '左门全开', '左门全关',
                               '打开中', '关闭中','停止')
LSlideDoorStatus.set('左门全关')
LSlideDoorStatus.bind("<<ComboboxSelected>>", LSlideDoorStatus_cli)
LSlideDoorStatus.place(x=30, y=15, width=90)


#左门热保护
button_PsdlTHERMAL = tk.Button(dwset, text='左门热保护', command=PsdlTHERMAL_cli,bd=1, width=12, height=1)
button_PsdlTHERMAL.place(x=150, y=10)


#左门故障
button_PsdlFault = tk.Button(dwset, text='左门故障', command=PsdlFault_cli,bd=1, width=12, height=1)
button_PsdlFault.place(x=280, y=10)



    #右侧滑门状态
def RSlideDoorStatus_cli(e):
    RSlideDoorStatus_type = RSlideDoorStatus.get()
    RSlideDoor_type_cli(RSlideDoorStatus_type)

RSlideDoorStatus = Combobox(dwset,state="readonly")
RSlideDoorStatus['values'] = ( '未知状态','右门故障', '右门全开', '右门全关',
                               '打开中', '关闭中','停止')
RSlideDoorStatus.set('右门全关')
RSlideDoorStatus.bind("<<ComboboxSelected>>", RSlideDoorStatus_cli)
RSlideDoorStatus.place(x=30, y=55, width=90)


#左门热保护
button_RTHReset = tk.Button(dwset, text='右门热保护', command=PsdrTHERMAL_cli,bd=1, width=12, height=1)
button_RTHReset.place(x=150, y=50)


#左门故障
button_RTHReset = tk.Button(dwset, text='右门故障', command=PsdrFault_cli,bd=1, width=12, height=1)
button_RTHReset.place(x=280, y=50)

#左剪刀门状态
def LSdclDoor_cli(e):
    LSdclDoor_type = LSdclDoor.get()
    LSdclDoor_type_cli(LSdclDoor_type)

LSdclDoor = Combobox(dwset,state="readonly")
LSdclDoor['values'] = ( '左翼门初始态','左翼关闭', '左翼打开中', '左翼关闭中','暂停中',
                               '打开失败', '左翼过热','左翼故障')
LSdclDoor.set('左翼门初始态')
LSdclDoor.bind("<<ComboboxSelected>>", LSdclDoor_cli)
LSdclDoor.place(x=30, y=100, width=110)


#左剪刀门状态
def RSdclDoor_cli(e):
    RSdclDoor_type = RSdclDoor.get()
    RSdclDoor_type_cli(RSdclDoor_type)

RSdclDoor = Combobox(dwset,state="readonly")
RSdclDoor['values'] = ( '右翼门初始态','右翼关闭', '右翼打开中', '右翼关闭中','暂停中',
                               '打开失败', '右翼过热','右翼故障')
RSdclDoor.set('右翼门初始态')
RSdclDoor.bind("<<ComboboxSelected>>", RSdclDoor_cli)
RSdclDoor.place(x=250, y=100, width=110)

Maintenance_Mode=canvas2.create_line(20,140,140,140,fill='grey')
MaintenanceMode_text = canvas2.create_text(210, 140, text='口盖相关设置', fill='grey', font=('微软雅黑', 10))
Maintenance_Mode2=canvas2.create_line(270,140,390,140,fill='grey')

#慢充口开关
button_LChargCover = tk.Button(dwset, text='慢充口开关', command=PsdrTHERMAL_cli,bd=1, width=12, height=1)
button_LChargCover.place(x=150, y=50)

#快充口开关
button_RChargCover = tk.Button(dwset, text='快充口开关', command=PsdrTHERMAL_cli,bd=1, width=12, height=1)
button_RChargCover.place(x=150, y=50)