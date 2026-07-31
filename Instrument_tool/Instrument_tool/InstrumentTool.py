
from imports import *
# from toolUpdate import *
"""""
    小工具主程序
"""""


#左侧列表默认为左右侧方控
ForgetAllCard()
Control.helmcontrol.place(x=0,y=40)


    #仪表页面左侧的功能页映射列表
def selectCard_Data(Value):
    List = {'左右侧方控':Control.helmcontrol,'充电相关':Charge.charge, '里程相关':Mileage.mileage,'车况相关':CarState.carstate,
            '能耗相关':Energy.energy,'主动安全与预警':Auto.autodrive,'车手与雷达':DriverRadar.driversradar,
            '车速与TSR':SpeedTSR.carspeelig,'指示灯相关':Light.carlamp,'文言弹窗与其他':Tip.othermation,'增程相关信息':Extended.extended}

    #这里的逻辑很简单，先把上面所有的功能隐藏，再单独显示用户选择的页面，就不会出现重叠的现象
    ForgetAllCard()
    ApkLog.place(x=400, y=0)
    bottom.place(x=0, y=500)
    List.get(Value).place(x=0,y=40)

    #这里获取到用户的选择后，拿着选择调用上面的功能列表函数
def selectCard(e):
    card_type = combo_Listcardselect.get()
    selectCard_Data(card_type)       #在这里获取当前选择的类型


combo_Listcardselect = Combobox(root,state="readonly")
combo_Listcardselect['values'] = ('左右侧方控', '充电相关','里程相关','车况相关','能耗相关','主动安全与预警','车手与雷达',
                                 '车速与TSR','指示灯相关','文言弹窗与其他','增程相关信息')
combo_Listcardselect.set('左右侧方控')
combo_Listcardselect.bind("<<ComboboxSelected>>", selectCard)
combo_Listcardselect.place(x=160, y=10, width=120)
ApkLog.place(x=400,y=0)
bottom.place(x=0,y=500)



'''
这里是一个分割线，将仪表左侧功能页与车控左侧功能页分开
'''



    #这里是车控页的选择，原理同上
def CarselectCard_Data(Value):
    List = {'车辆信息': CarInfo.carinfo, '门窗设置': DWSet.dwset, '灯光设置': Mileage.mileage,
            '座椅设置': CarState.carstate,'驾驶设置': Energy.energy,
            '辅助驾驶': Auto.autodrive, '全域智驾': DriverRadar.driversradar,
            '智能影像': SpeedTSR.carspeelig, '空调香氛': Light.carlamp}

    ForgetAllCard()
    #底栏的主要信息为续航和驾驶模式，挡位，对车控也有强依赖，故进车控时保留此功能的显示
    bottom.place(x=0, y=500)
    #这里要进入车控页的专属调试面板
    ApkLog.place(x=400, y=0)
    List.get(Value).place(x=0, y=40)


    # 这里获取到用户的选择后，拿着选择调用上面的功能列表函数
def CarSelectCard(e):
    card_type = combo_CarListcardselect.get()
    CarselectCard_Data(card_type)  # 在这里获取当前选择的类型


combo_CarListcardselect = Combobox(root, state="readonly")
combo_CarListcardselect['values'] = ('车辆信息', '门窗设置', '灯光设置', '座椅设置', '驾驶设置', '辅助驾驶', '全域智驾',
                                    '智能影像', '空调香氛')
combo_CarListcardselect.set('车辆信息')
combo_CarListcardselect.bind("<<ComboboxSelected>>", CarSelectCard)
# combo_CarListcardselect.place(x=160, y=10, width=120)
ApkLog.place(x=400, y=0)
bottom.place(x=0, y=500)

#进入QNX侧
def Enter_QNX():
    result = messagebox.askokcancel("Hold on....",
                                    "工具会自动识别串口设备端口号\n使用QNX相关功能时，务必移除与台架安卓所连接的双公线，只保留QNX连接线"
                                    "\n否则会导致工具识别端口异常"
                                    "\nPS:该功能不稳定，目前仍在测试中")
    if result == True:
        root.geometry("1000x540")
        ForgetAllCard()
        combo_Listcardselect.place_forget()     #隐藏仪表页左侧的多功能页模块
        combo_CarListcardselect.place_forget()        #隐藏车控页左侧的多功能页模块
        Qnxbottom.place(x=0, y=500)
        QNXLamp.QnxLamp.place(x=0, y=0)
        QnxControl.place(x=400, y=0)
        text.config(state='normal')
        text.insert('end', '\n' + System_Time() + "\n当前连接设备端口为:" + QNX_PORT())
        text.config(state='disabled')
        text.yview_moveto(1)

    else:
        return False





def Enter_XGPT():
    root.geometry("600x540")
    combo_CarListcardselect.place_forget()
    combo_Listcardselect.place_forget()
    ForgetAllCard()
    XGPT.SmartAI.place(x=0,y=0)

def Enter_Android():
    root.geometry("1000x540")
    ForgetAllCard()
    combo_CarListcardselect.place_forget()
    Control.helmcontrol.place(x=0, y=40)
    bottom.place(x=0, y=500)
    ApkLog.place(x=400,y=0)
    combo_Listcardselect.place(x=160, y=10, width=120)
    combo_Listcardselect.set('左右侧方控')

def Enter_CarControl():
    root.geometry("1000x540")
    combo_Listcardselect.forget()
    ForgetAllCard()
    bottom.place(x=0, y=500)
    ApkLog.place(x=400,y=0)
    combo_CarListcardselect.place(x=160, y=10, width=120)
    combo_CarListcardselect.set('车辆信息')
    CarInfo.carinfo.place(x=0,y=40)     #车控页优先显示车辆信息



#每次启动小工具，就进行版本检查
# thread = threading.Thread(target=PingGit)
# thread.start()



#读取更新信息

# def show_custom_message():
#     simpledialog.askstring()
#     if CheckUpdate() ==3:
#         messagebox.askokcancel("版本信息",
#                                         "当前版本最后更新日期为:%s\n"
#                                         "\n当前正在检测更新版本中,请稍后"
#                                         %(toolVersion))
#     elif CheckUpdate() ==1:
#         UpdateInformation = r'./path/UpdateInformation'
#         with open(UpdateInformation, 'r', encoding='UTF-8') as file:
#             content = file.read()
#         UpdataTool = messagebox.askokcancel("发现最新版本",
#                                         "当前版本最后更新日期为:%s\n"
#                                         "更新内容如下:\n%s\n"
#                                         "\n按下确定后，将进行更新版本"%(toolVersion,content))
#         if UpdataTool == True:
#             messagebox.showinfo("版本更新",
#                                                 "正在后台更新版本，可继续使用该工具")
#             text.yview_moveto(1)
#             thread = threading.Thread(target=PullTool)
#             thread.start()
#         else:1
#             return False
#     elif CheckUpdate() ==2:
#         messagebox.askokcancel("版本信息",
#                                         "当前版本最后更新日期为:%s\n"
#                                         "\n当前已是最新版本，无需更新"
#                                         %(toolVersion))


menubar.add_cascade(label="仪表侧", command=Enter_Android)
menubar.add_cascade(label="QNX侧", command=Enter_QNX)
menubar.add_cascade(label="其他模块", command=Enter_XGPT)
menubar.add_cascade(label="车控", command=Enter_CarControl)
# menubar.add_cascade(label="信息", command=show_custom_message)


#运行主程序
root.mainloop()


