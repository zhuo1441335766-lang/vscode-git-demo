from cli.ApkLog_data import *
    #这里是控制页的创建
ApkLog = tk.Frame(root,width=600, height=500)
ApkLog.place(x=400,y=0)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(ApkLog,width=600,height=500)
canvas2.pack()

    #推包与拉日志

auto_line=canvas2.create_line(20,15,250,15,fill='grey')
auto_text = canvas2.create_text(1020-720, 15, text='推包与拉日志', fill='grey', font=('微软雅黑', 10))
Auto_line=canvas2.create_line(350,15,580,15,fill='grey')

frametext = tk.Frame(ApkLog,width=560, height=150,bd=1)
frametext.pack_propagate(False)
frametext.place(x=20, y=40)


    #在这里设置更新显示的文本

scrollbar = tk.Scrollbar(frametext)
scrollbar.pack(side='right', fill='y')

textIns = tk.Text(frametext, height=10, borderwidth=2, relief="groove",  yscrollcommand=scrollbar.set)
textIns.insert(0.0,'')
textIns.configure(state='disabled')  # 设置文本框为只读状态
textIns.pack(side='left', fill='y')

    #将繁杂的打印窗打印步骤封装起来
def text_In(Value):
    Value = Value.replace('\n', '').replace('\r', '')
    textIns.config(state='normal')
    textIns.insert('end','\n'+Value)
    test_optimize()
    textIns.yview_moveto(1)
    textIns.config(state='disabled')

def text_info(Value):
    text_In(System_Time())
    text_In(Value)



def equipment_error():
    text_info("出现异常，请检查设备连接")


#disable-verity
def Disable():
    if Test() == False:
        equipment_error()
    else:
        Disable_cli()
        text_info('disable-verity成功!系统正在重启')

def Thread_Disable():
    text_info('正在执行，请稍后')
    thread = threading.Thread(target=Disable)
    thread.start()

#设备信息


#优化获取的信息
def test_optimize():
    textIns.tag_remove('sel', '1.0', tk.END)
    textIns.mark_set('insert', '1.0')



def DeviceInfo():
    if Test() == False:
        equipment_error()
    else:
        text_info('大屏版本为:'+RomInfo())
        text_In('仪表版本为:' + InstrumentInfo())
        text_In('科技岛版本为:' + techislandInfo())
        text_In('mcu版本为:' + McuInfo())
        text_In('CFC为:' + CfcInfo())
        text_In('VIN码为:'+VinInfo())
def Thread_DeviceInfo():
    text_info('正在疯狂获取中，请稍后')
    thread = threading.Thread(target=DeviceInfo)
    thread.start()

#重启设备
def Reboot():
    if Test() == False:
        equipment_error()
    else:
        Reboot_cli()
        text_info('重启成功，等待设备启动')
def Thread_Reboot():
    thread = threading.Thread(target=Reboot)
    thread.start()



    #切换昼夜
def switch_DayNight():
    if Test() == False:
        equipment_error()
    else:
        Switch_DayNight_cli()
        text_info("切换昼夜成功")

def Thread_switch_DayNight():
    thread = threading.Thread(target=switch_DayNight)
    thread.start()

    #杀死仪表进程

def KillInstrument():
    if Test() == False:
        equipment_error()
    else:
        text_info("仪表进程号为:"+GetInsPid_cli())
        text_In('仪表进程已被kill')
        KillInstrument_cli()

    # 杀死SR进程
def KillSubreality():
    if Test() == False:
        equipment_error()
    else:
        text_info("SR进程号为:"+GetSubPid_cli())
        text_In('SR进程已被kill')
        KillSubreality_cli()

    # 杀死导航进程
def Killmontecarlo():
    if Test() == False:
        equipment_error()
    else:
        text_info("导航进程号为:"+GetMapPid_cli())
        text_In('导航进程已被kill')
        KillMontecarlo_cli()

def KillTechIsland():
    if Test() == False:
        equipment_error()
    else:
        text_info("科技岛进程号为:"+GetTechIsland_cli())
        text_In('科技岛进程已被kill')
        KillTechIsland_cli()


def KillsystemUI():
    if Test() == False:
        equipment_error()
    else:
        text_info("SystemUI进程号为:"+GetSystemUi_cli())
        text_In('SystemUI已被kill')
        KillSystemUi_cli()

def killsmartcontrol():
    if Test() == False:
        equipment_error()
    else:
        text_info("车控进程号为:"+Getsmartcontrol_cli())
        text_In('车控已被kill')
        killsmartcontrol_cli()
def KillPid(e):
    RPup_type = combo_KillPid.get()
    if RPup_type == 'kill仪表' :
        KillInstrument()
    elif RPup_type == 'kill人驾' :
        KillSubreality()
    elif RPup_type == 'kill导航' :
        Killmontecarlo()
    elif RPup_type == 'kill科技岛' :
        KillTechIsland()
    elif RPup_type == 'kill SystemUI' :
        KillsystemUI()
    elif RPup_type == 'kill车控' :
        killsmartcontrol_cli()
    else:
        pass


def log0():
    if Test() == False:
        equipment_error()
    else:
        Log0_cli()
        text_info('LOG0拉取成功')

def PullLog0():
    text_info('正在拉取日志，请耐心等待.....')
    thread = threading.Thread(target=log0)
    thread.start()

def Aog0():
    if Test() == False:
        equipment_error()
    else:
        AllLog_cli()
        text_info('All Log拉取成功！')
def PullAog0():
    text_info('正在拉取日志，请耐心等待.....')
    thread = threading.Thread(target=Aog0)
    thread.start()

def QNX():
    if Test() == False:
        equipment_error()
    else:
        QNXLog_cli()
        text_info('QNXLog拉取成功')
def PullQNX():
    text_info('正在拉取QNX日志，QNX日志拉取需要较长的时间，请耐心等待。。')
    thread = threading.Thread(target=QNX)
    thread.start()


#截图仪表
def ScreenIns():
    if Test() == False:
        equipment_error()
    else:
        ScreenIns_cli()
        text_info('截图成功')

def Thread_ScreenIns():
    thread = threading.Thread(target=ScreenIns)
    thread.start()

#科技岛截图
def ScreenLand():
    if Test() == False:
        equipment_error()
    else:
        ScreenLand_cli()
        text_info('截图成功')

def Thread_ScreenLand():
    thread = threading.Thread(target=ScreenLand)
    thread.start()


    #截图大屏
def Screen():
    if Test() == False:
        equipment_error()
    else:
        Screen_cli()
        text_info('截图成功')

def Thread_Screen():
    thread = threading.Thread(target=Screen)
    thread.start()

    #推包的多个兜底判断在这里执行
def inspect(ApkName):
    apk = RadarinstallApk.get()
    if DidiSigned(apk)==False :
        result = messagebox.askokcancel("Wait..",
                                        "检测到你正在用 DD 专5的包推DEV的rom(或者专1包推Release的rom)，请确认是否继续")
        if result == True:
            pass
        else:
            return False
    elif deciderom(apk)==False:
        result = messagebox.askokcancel("Wait..",
                                        "检测到你正在用专5的包推DEV的rom(或者专1包推Release的rom)，请确认是否继续")
        if result == True:
            pass
        else:
            return False
    elif decideway(ApkName,apk)==False:
        result = messagebox.askokcancel("Wait..",
                                        "检测到所推APK名称里没有包含安装的应用名称，请检查选择推包的文件\n\n"
                                        "APK路径为:"+apk+
                                        "\n当前所推应用为"+ApkName+
                                        '\n\n 点击确定无视风险，继续安装',)
        if result == True:
            pass
        else:
            return False
    elif JudegICM(apk) == False:
        # if GetCarType()=='E29':
        #     pass
        # else:
            result = messagebox.askokcancel("Wait..",
                                        "检测到当前有仪表屏与无仪表屏可能存在混淆推包，请确认\n\n"
                                        "APK路径为:"+apk+
                                        "\n当前车型为:"+GetCarType()+
                                        '\n\n 点击确定无视风险，继续安装', )
            if result == True:
                pass
            else:
                return False




def InstallAapk():
    apk = RadarinstallApk.get()          #获取文件路径
    apk = apk.replace("\"", "")
    if TestRoute(apk) == False:
        text_info('路径为空，请在下方输入APK路径')
    elif is_valid_path(apk) == False:             #这里会执行推APK的操作
        text_info('路径似乎不是一个有效路径，请检查')
    elif remount() == False:
        text_info('未disable-verity，请先执行disable-verity')
        text_In('再进行推包')
    elif inspect('Instrument') == False:
        text_info('已选择取消推包')
    else:
        Intall_cli(apk)
        text_info('APK已推，请重启设备！')
def ApkPrompt():
    if Test() == False:             #这里会执行推APK的操作
        equipment_error()
    text_info('正在推APK，请耐心等待,推包过程请不要关闭工具')
    text_In('识别到当前设备车型为:'+GetCarType())
    thread = threading.Thread(target=InstallAapk)
    thread.start()

#推科技岛APK
def InstallLandapk():
    apk = RadarinstallApk.get()          #获取文件路径
    apk = apk.replace("\"", "")
    if TestRoute(apk) == False:
        text_info('路径为空，请在下方输入APK路径')
    elif is_valid_path(apk) == False:             #这里会执行推APK的操作
        text_info('路径似乎不是一个有效路径，请检查')
    elif remount() == False:
        text_info('未disable-verity，请先执行disable-verity')
        text_In('再进行推包')
    elif inspect('techIsland') == False:
        text_info('已选择取消推包')
    else:
        IntallLand_cli(apk)
        text_info('APK已推，请重启设备！')

def LandApkPrompt():
    if Test() == False:             #这里会执行推APK的操作
        equipment_error()
    text_info('正在推APK，请耐心等待,推包过程请不要关闭工具')
    text_In('识别到当前设备车型为:'+GetCarType())
    thread = threading.Thread(target=InstallLandapk)
    thread.start()

    #禁止接收MCU信号
def MCUProhibit():
    result = messagebox.askokcancel("WARNING！！！！！", "此操作会禁止Carservice接收CAN信号\n如果是在实车环境，可能会导致严重问题，确认要开启此功能吗？")
    if result == True:
        if ProhibitMcu_cli() == True:
            text_info('已禁止接收MCU信号,再次点击或者重启设备可恢复接收')
            os.system('adb shell vdt disableMCU 1')

        else:
            text_info('已开始接收MCU信号')
            os.system('adb shell vdt disableMCU 0')

def McuUpcli():
    mcu = RadarinstallApk.get()

    if TestRoute(mcu) == False:
        text_info('没有输入MCU升级包的路径，请在下方填写路径')
    elif is_valid_path(mcu) == False:
        text_info('路径似乎不是一个有效路径，请检查')
    else:
        UpdateMcu_cli(mcu)
        text_info('MCU升级成功')

def McuPrompt():
    if Test() == False:
        equipment_error()
        return False
    text_info('正在升级MCU，需要较长的时间，请耐心等待....')
    text_In("可在工具的黑色命令窗口查看升级进度")
    thread = threading.Thread(target=McuUpcli)
    thread.start()


    #投屏仪表
def OpenScrcpy():
    if Test() == False:
        equipment_error()
    else:
        text_info('已根据车型投屏仪表')
        thread = threading.Thread(target=OpenScrcpy_cli)
        thread.start()

def OpenLandScrcpy():
    try:
        subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
        text_info('已根据车型投屏科技岛')
        thread = threading.Thread(target=OpenLandScrcpy_cli)
        thread.start()

    except subprocess.CalledProcessError:
        text_info('出现异常，请检查设备连接')
#投屏大屏
def OpenBigScrcpy():
    try:
        subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
        text_info('已根据车型投屏大屏')
        thread = threading.Thread(target=DisScrcpy_cli)
        thread.start()

    except subprocess.CalledProcessError:
        text_info('出现异常，请检查设备连接')

    #仪表录屏
def VideoScrcpy():
    try:
        subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
        text_info('已根据车型录屏仪表,文件将存放在对应文件夹')
        text_In('如需停止录像，直接关闭仪表投屏窗口即可')
        thread = threading.Thread(target=VideoScrcpy_cli)
        thread.start()

    except subprocess.CalledProcessError:
        text_info('出现异常，请检查设备连接')

#科技岛录像
def VideoLandScrcpy():
    try:
        subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
        text_info('已根据车型录屏科技岛,文件将存放在对应文件夹')
        text_In("如需停止录像，直接关闭科技岛投屏窗口即可")
        thread = threading.Thread(target=VideoLandScrcpy_cli)
        thread.start()

    except subprocess.CalledProcessError:
        text_info('出现异常，请检查设备连接')
#大屏录像
def VideoBigScrcpy():
    try:
        subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
        text_info('已根据车型录屏大屏,文件将存放在对应文件夹')
        text_In("如需停止录像，直接关闭大屏投屏窗口即可")
        thread = threading.Thread(target=VideoBigScrcpy_cli)
        thread.start()

    except subprocess.CalledProcessError:
        text_info('出现异常，请检查设备连接')

    #跳过OOBE
def SkipOOBE():
    if Test() == False:
        equipment_error()
    else:
        SkipOOBE_cli()
        text_info('已跳过OOBE引导')

    #调整仪表日志等级
def SetLogDeBug():
    if Test() == False:
        equipment_error()
    else:
        SetLogDeBug_cli()
        text_info('已调整仪表日志等级')

    #海外版本切换语言
# def SwitchLanguage_smt(e):
#     if Test() == False:
#         equipment_error()
#     thread = threading.Thread(target=SwitchLanguage)
#     thread.start()
# def SwitchLanguage():
#     Instruction_type = combo_SwitchLanguage.get()
#     SwitchLanguage_cli(Instruction_type)

    #海外carplay等模拟应用的安装
def InstallPhoneMapApp():
    if Test() == False:
        equipment_error()
    else:
        text_info('成功安装CarPlay，AndroidAuto模拟应用')
        text_In('无需重启，请在大屏第三方应用列表里操作模拟数据')
        thread = threading.Thread(target=InstallPhoneMapApp_cli)
        thread.start()

#激活海外地图
def ActivationAbroadMap():
    if Test() == False:
        equipment_error()
    else:
        text_info('海外地图已激活，请耐心等待地图启动')
        thread = threading.Thread(target=ActivationMap_cli)
        thread.start()


#第一行按钮
disable = tk.Button(ApkLog, text="disable-verity", command=Thread_Disable,bd=1,width=12,height=1)
disable.place(x=25, y=200)
deviceinfo = tk.Button(ApkLog, text="查看版本信息", command=Thread_DeviceInfo,bd=1,height=1,width=12)
deviceinfo.place(x=135, y=200)
devicereboot = tk.Button(ApkLog, text="重启设备", command=Thread_Reboot,bd=1,height=1,width=12)
devicereboot.place(x=245, y=200)
switchDayNight = tk.Button(ApkLog, text="切换昼夜模式", command=Thread_switch_DayNight,bd=1,height=1,width=12)
switchDayNight.place(x=355, y=200)

combo_KillPid = Combobox(ApkLog,state="readonly")
combo_KillPid['values'] = ('选择Kill进程', 'kill仪表','kill人驾','kill导航','kill科技岛','kill SystemUI','kill车控')
combo_KillPid.set('选择Kill进程')
combo_KillPid.bind("<<ComboboxSelected>>", KillPid)
combo_KillPid.place(x=465, y=200, width=90)

#第二行按钮
disable = tk.Button(ApkLog, text="抓取LOG0", command=PullLog0,bd=1,width=12,height=1)
disable.place(x=25, y=240)
disable = tk.Button(ApkLog, text="抓取All Log", command=PullAog0,bd=1,width=12,height=1)
disable.place(x=135, y=240)
disable = tk.Button(ApkLog, text="抓取QNXLog", command=PullQNX,bd=1,width=12,height=1)
disable.place(x=245, y=240)
disable = tk.Button(ApkLog, text="打开Log文件夹", command=Open_Log,bd=1,width=12,height=1)
disable.place(x=355, y=240)
disable = tk.Button(ApkLog, text="禁收MCU信号", command=MCUProhibit,bd=1,width=12,height=1)
disable.place(x=465, y=240)

#第三行按钮
disable = tk.Button(ApkLog, text="仪表投屏", command=OpenScrcpy,bd=1,width=12,height=1)
disable.place(x=25, y=280)
disable = tk.Button(ApkLog, text="大屏投屏", command=OpenBigScrcpy,bd=1,width=12,height=1)
disable.place(x=135, y=280)
disable = tk.Button(ApkLog, text="科技岛投屏", command=OpenLandScrcpy,bd=1,width=12,height=1)
disable.place(x=245, y=280)

    #推APK相关
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # 更新Entry组件中的文本为文件路径
        RadarinstallApk.delete(0, tk.END)  # 清空Entry中的旧内容
        RadarinstallApk.insert(0, file_path)  # 插入新的文件路径

RadarinstallApk = tk.Entry(ApkLog, validate='key',width=60, font=("微软雅黑", 9))
RadarinstallApk.place(x=25, y=350)
open_button = tk.Button(ApkLog, text="选择推包文件", command=open_file,bd=1,width=12,height=1)
open_button.place(x=465, y=345)
push_text = canvas2.create_text(270, 330, text='在此处填写路径，工具会自动识别当前设备车型，也可在输入框右侧按钮中选择包的路径', fill='grey', font=('微软雅黑', 10))
disable = tk.Button(ApkLog, text="安装仪表APK", command=ApkPrompt,bd=1,width=12,height=1)
disable.place(x=355, y=280)
disable = tk.Button(ApkLog, text="安装科技岛APK", command=LandApkPrompt,bd=1,width=12,height=1)
disable.place(x=465, y=280)




    #第四行按钮
disable = tk.Button(ApkLog, text="截图仪表", command=Thread_ScreenIns,bd=1,width=12,height=1)
disable.place(x=25, y=385)
disable = tk.Button(ApkLog, text="截图大屏", command=Thread_Screen,bd=1,width=12,height=1)
disable.place(x=135, y=385)
disable = tk.Button(ApkLog, text="截图科技岛", command=Thread_ScreenLand,bd=1,width=12,height=1)
disable.place(x=245, y=385)
disable = tk.Button(ApkLog, text="打开截图文件夹", command=Open_pic,bd=1,width=12,height=1)
disable.place(x=355, y=385)
disable = tk.Button(ApkLog, text="升级mcu", command=McuPrompt,bd=1,width=12,height=1)
disable.place(x=465, y=385)


    #第五行按钮
disable = tk.Button(ApkLog, text="仪表录像", command=VideoScrcpy,bd=1,width=12,height=1)
disable.place(x=25, y=425)
disable = tk.Button(ApkLog, text="大屏录像", command=VideoBigScrcpy,bd=1,width=12,height=1)
disable.place(x=135, y=425)
disable = tk.Button(ApkLog, text="科技岛录像", command=VideoLandScrcpy,bd=1,width=12,height=1)
disable.place(x=245, y=425)
disable = tk.Button(ApkLog, text="打开录像文件夹", command=Open_video,bd=1,width=12,height=1)
disable.place(x=355, y=425)

# disable = tk.Button(ApkLog, text="安装CarPlay/Auto", command=InstallPhoneMapApp,bd=1,width=14,height=1)
# disable.place(x=465, y=425)
def SetConfig(e):
    RPup_type = combo_SetConfig.get()
    if RPup_type == '选择修改配置':
        pass
    else:
        text_info('正在修改配置，修改完成后将会自动重启')
        thread = threading.Thread(target=SetConfig_smt)
        thread.start()

def SetConfig_smt():
    RPup_type = combo_SetConfig.get()
    thread = threading.Thread(target=SetConfig_cli(RPup_type))
    thread.start()


combo_SetConfig = Combobox(ApkLog,state="readonly")
combo_SetConfig['values'] = ('选择修改配置', '最高配','最低配')
combo_SetConfig.set('选择修改配置')
combo_SetConfig.bind("<<ComboboxSelected>>", SetConfig)
combo_SetConfig.place(x=465, y=425, width=95)

def SwitchLanguage():
    if Test() == False:
        equipment_error()
    else:
        text_info('已调出切换语言弹窗，请在设备大屏操作')
        os.system('adb shell am broadcast -a com.xiaopeng.intent.action.LANGUAGE_CHANGE')

def Restore():
    if Test() == False:
        equipment_error()
    else:
        text_info('已恢复出厂设置')
        os.system('adb shell am broadcast -a android.intent.action.MASTER_CLEAR -f 0x01000000')

#第六行按钮
disable = tk.Button(ApkLog, text="跳过OOBE", command=SkipOOBE,bd=1,width=12,height=1)
disable.place(x=25, y=465)
disable = tk.Button(ApkLog, text="调整日志等级", command=SetLogDeBug,bd=1,width=12,height=1)
disable.place(x=135, y=465)
ActivationMap = tk.Button(ApkLog, text="海外地图激活", command=ActivationAbroadMap,bd=1,width=12,height=1)
ActivationMap.place(x=245, y=465)
ActivationMap = tk.Button(ApkLog, text="海外切换语言", command=SwitchLanguage,bd=1,width=12,height=1)
ActivationMap.place(x=355, y=465)
ActivationMap = tk.Button(ApkLog, text="恢复出厂设置", command=Restore,bd=1,width=12,height=1)
ActivationMap.place(x=465, y=465)

scrollbar.config(command=textIns.yview)


