from cli.XGPT_data import *

    #这里是AI小P的创建
SmartAI = tk.Frame(root,width=600, height=500)


#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(SmartAI,width=600,height=500)
canvas2.pack()

frametext = tk.Frame(SmartAI,width=560, height=150,bd=1)
frametext.pack_propagate(False)
frametext.place(x=20, y=40)

auto_line=canvas2.create_line(20,15,250,15,fill='grey')
auto_text = canvas2.create_text(1020-720, 15, text='XGPT相关页', fill='grey', font=('微软雅黑', 10))
Auto_line=canvas2.create_line(350,15,580,15,fill='grey')


    #在这里设置更新显示的文本

scrollbar = tk.Scrollbar(frametext)
scrollbar.pack(side='right', fill='y')

text = tk.Text(frametext, height=10, borderwidth=2, relief="groove",  yscrollcommand=scrollbar.set)
text.insert(0.0,'')
text.configure(state='disabled')  # 设置文本框为只读状态
text.pack(side='left', fill='y')

    #将繁杂的打印窗打印步骤封装起来
def text_In(Value):
    Value = Value.replace('\n', '').replace('\r', '')
    text.config(state='normal')
    text.insert('end','\n'+Value)
    test_optimize()
    text.yview_moveto(1)
    text.config(state='disabled')

def text_info(Value):
    text_In(System_Time())
    text_In(Value)


def equipment_error():
    text_info('出现异常，请检查设备连接')

#版本信息

#优化获取的信息
def test_optimize():
    text.tag_remove('sel', '1.0', tk.END)
    text.mark_set('insert', '1.0')

def VersionInfo():
    if Test() == False:
        equipment_error()
    else:
        text_info('大屏版本为:'+ RomInfo())
        text_In('语音版本为:'+ CarSpeechInfo())
        text_In('小P助手版本为:'+ AiassistantInfo())
        text_In('XGPT版本为:'+ XgptInfo())


def Thread_VersionInfo():
    text_info('正在疯狂获取中，请稍后')
    thread = threading.Thread(target=VersionInfo)
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
        text_info('切换昼夜成功')

def Thread_switch_DayNight():
    thread = threading.Thread(target=switch_DayNight)
    thread.start()

    #投屏大屏
def OpenBigScrcpy():
    try:
        subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
        text_info('已根据车型投屏大屏')
        thread = threading.Thread(target=DisScrcpy_cli)
        thread.start()

    except subprocess.CalledProcessError:
        text_info('出现异常，请检查设备连接')
        text.yview_moveto(1)

        #大屏录像
def VideoScrcpy():
    try:
        subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
        text_info('已根据车型录屏,文件将存放在对应文件夹')
        text_In('如需停止录像，直接关闭投屏窗口即可')
        thread = threading.Thread(target=VideoScrcpy_cli)
        thread.start()

    except subprocess.CalledProcessError:
        text_info('出现异常，请检查设备连接')

        #抓LOG0
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


    #抓All Log
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


#推APK
def inspect():
    apk = RadarinstallApk.get()
    if deciderom(apk)==False:
        result = messagebox.askokcancel("Wait..",
                                        "检测到你正在用专5的包推DEV的rom(或者专1包推Release的rom)，请确认是否继续")
        if result == True:
            pass
        else:
            return False
    # elif decideway(apk)==False:
    #     result = messagebox.askokcancel("Wait..",
    #                                     "检测到所推包名与车型不匹配，请确认是否继续")
    #     if result == True:
    #         pass
    #     else:
    #         return False
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
    elif inspect() == False:
        text_info('已选择取消推包')
    else:
        Intallxgpt_cli(apk)
        text_info('APK已推，请重启设备！')

def ApkPrompt():
    if Test() == False:             #这里会执行推APK的操作
        equipment_error()
    text_info('正在推APK，请耐心等待')
    text_In('识别到当前设备车型为:'+GetCarType())
    thread = threading.Thread(target=InstallAapk)
    thread.start()

    #截图大屏
def Screen():
    if Test() == False:
        equipment_error()
    else:
        Screen_cli()
        text_info('截图成功！')
def Thread_Screen():
    thread = threading.Thread(target=Screen)
    thread.start()

#杀进程
def Killxgpt():
    if Test() == False:
        equipment_error()
    else:
        text_info('AI小P进程号为:'+GetxgptPid_cli())
        text_In('进程已被kill')
        Killxgpttrument_cli()

    # 杀死语音
def KillSubreality():
    if Test() == False:
        equipment_error()
    else:
        text_info('语音服务进程号为:'+GetCSSPid_cli())
        text_In('进程已被kill')
        KillCarSpeechService_cli()

# 唤醒小P
def CallXP():
    if Test() == False:
        equipment_error()
    else:
        CallXP_cli()
        text_info('已唤醒小P，请在下方输入语音指令')

# 获取小P指令并发送

def DispatchOrders():
    i = RadarinstallApk.get()
    if TestRoute(i) == False:
        text_info('指令为空，请在下方输入指令')
    else:
        DispatchOrders_cli(i)

    # 杀死语音
def KillAiassistant():
    if Test() == False:
        equipment_error()
    else:
        text_info('小P形象进程号为:'+GetAIAPid_cli())
        text_In('进程已被kill')
        KillAiassistant_cli()

def KillAicabin():
    if Test() == False:
        equipment_error()
    else:
        text_info('爱卡宾进程号为:'+GetAicaPid_cli())
        text_In('进程已被kill')
        KillAicabin_cli()
def KillPid(e):
    RPup_type = combo_KillPid.get()
    KillList = {'killAI小P':Killxgpt,'kill语音':KillSubreality,'kill小P形象':KillAiassistant,'kill爱卡宾':KillAicabin}
    KillList.get(RPup_type)()

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

#获取vin码，大屏设备码等信息
def DeviceInfo():
    if Test() == False:
        equipment_error()
    else:
        text_info('Devices:'+DevicesInfo())
        text_In('hardwareId:'+ HardwareIdInfo())
        text_In('vin:'+ VinInfo())
def Thread_DeviceInfo():
    if Test() == False:
        equipment_error()
    else:
        text_info('正在疯狂获取中，请稍后')
        thread = threading.Thread(target=DeviceInfo)
        thread.start()

    #清理AI小P缓存
def ClearCache_XGPT():
    if Test() == False:
        equipment_error()
    else:
        text_info('已清理AI小P缓存,进程将重启')
        ClearCache()

#切换应用环境
def ChangeApk():
    if ChangeApk_cli() == '预发':
        text_info('已切换应用为预发环境')
    else:
        text_info('已切换应用为正式环境')

   #屏幕轨迹指针显示开关
def ScreenPrint():
    if Test() == False:
        equipment_error()
    elif ScreenPrint_cli() == True:
            text_info('屏幕轨迹指针已打开')
    else:
            text_info('屏幕轨迹指针已关闭')




#推工厂APK
def PushFactory():
    if Test() == False:
        equipment_error()
    elif remount() == False:
        text_info('未disable-verity，请先执行disable-verity')
        text_In('再进行推工厂APK')
    elif PushFactoryApk_cli() == True:
        text_info('APK已推，请重启设备')
    else:
        text_info('工厂APK Push失败，请检查')
def PushFactoryApk():
    if Test() == False:
        equipment_error()
    text_info('正在推APK，请耐心等待')
    thread = threading.Thread(target=PushFactory)
    thread.start()

#选择发送指令的类型，并随机发送

def SendInstructions_smt(e):
    if Test() == False:
        equipment_error()
    thread = threading.Thread(target=SendInstructions)
    thread.start()
def SendInstructions():
    Instruction_type = combo_Command.get()
    SendInstructions_cli(Instruction_type)




combo_KillPid = Combobox(SmartAI,state="readonly")
combo_KillPid['values'] = ('选择Kill进程', 'killAI小P','kill语音','kill小P形象','kill爱卡宾')
combo_KillPid.set('选择Kill进程')
combo_KillPid.bind("<<ComboboxSelected>>", KillPid)
combo_KillPid.place(x=465, y=200, width=90)



#恢复大屏为正式环境
def ReturnNormal():
    if Test() == False:             #这里会执行推APK的操作
        equipment_error()
    text_info('已恢复大屏为正式环境，设备即将重启')
    thread = threading.Thread(target=ReturnNormal_cli)
    thread.start()

deviceinfo = tk.Button(SmartAI, text="获取设备信息", command=Thread_DeviceInfo,bd=1,height=1,width=12)
deviceinfo.place(x=25, y=200)
deviceinfo = tk.Button(SmartAI, text="获取版本信息", command=Thread_VersionInfo,bd=1,height=1,width=12)
deviceinfo.place(x=135, y=200)
devicereboot = tk.Button(SmartAI, text="重启设备", command=Thread_Reboot,bd=1,height=1,width=12)
devicereboot.place(x=245, y=200)
switchDayNight = tk.Button(SmartAI, text="切换昼夜模式", command=Thread_switch_DayNight,bd=1,height=1,width=12)
switchDayNight.place(x=355, y=200)
disable = tk.Button(SmartAI, text="大屏录像", command=VideoScrcpy,bd=1,width=12,height=1)
disable.place(x=25, y=390)
disable = tk.Button(SmartAI, text="大屏投屏", command=OpenBigScrcpy,bd=1,width=12,height=1)
disable.place(x=135, y=390)
disable = tk.Button(SmartAI, text="打开录像文件夹", command=Open_video,bd=1,width=12,height=1)
disable.place(x=245, y=390)
disable = tk.Button(SmartAI, text="抓取LOG0", command=PullLog0,bd=1,width=12,height=1)
disable.place(x=25, y=240)
disable = tk.Button(SmartAI, text="抓取All Log", command=PullAog0,bd=1,width=12,height=1)
disable.place(x=135, y=240)
disable = tk.Button(SmartAI, text="截图大屏", command=Thread_Screen,bd=1,width=12,height=1)
disable.place(x=25, y=280)
disable = tk.Button(SmartAI, text="打开截图文件夹", command=Open_pic,bd=1,width=12,height=1)
disable.place(x=135, y=280)
disable = tk.Button(SmartAI, text="打开Log文件夹", command=Open_Log,bd=1,width=12,height=1)
disable.place(x=245, y=240)
disable = tk.Button(SmartAI, text="调试语音环境", command=DialogDebug_cli,bd=1,width=12,height=1)
disable.place(x=355, y=240)
disable = tk.Button(SmartAI, text="清理AI小P缓存", command=ClearCache_XGPT,bd=1,width=12,height=1)
disable.place(x=465, y=240)
disable = tk.Button(SmartAI, text="唤醒小P", command=CallXP,bd=1,width=12,height=1)
disable.place(x=245, y=440)
disable = tk.Button(SmartAI, text="输入语音指令", command=DispatchOrders,bd=1,width=12,height=1)
disable.place(x=355, y=440)
disable = tk.Button(SmartAI, text="disable-verity", command=Thread_Disable,bd=1,width=12,height=1)
disable.place(x=245, y=280)
disable = tk.Button(SmartAI, text="打开工厂调试", command=DFactoryApkOpen_cli,bd=1,width=12,height=1)
disable.place(x=135, y=440)
disable = tk.Button(SmartAI, text="推工厂APK", command=PushFactoryApk,bd=1,width=12,height=1)
disable.place(x=25, y=440)
disable = tk.Button(SmartAI, text="切换应用环境", command=ChangeApk,bd=1,width=12,height=1)
disable.place(x=465, y=280)
disable = tk.Button(SmartAI, text="屏幕轨迹开关", command=ScreenPrint,bd=1,width=12,height=1)
disable.place(x=355, y=390)


combo_Command = Combobox(SmartAI,state="readonly")
combo_Command['values'] = ('选择指令类型', '图生文','小P百科','用车问答','联网搜索','日常闲聊','其他指令','小P绘画','故事创作')
combo_Command.set('选择指令类型')
combo_Command.bind("<<ComboboxSelected>>", SendInstructions_smt)
combo_Command.place(x=465, y=390, width=100)


    #推APK相关
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # 更新Entry组件中的文本为文件路径
        RadarinstallApk.delete(0, tk.END)  # 清空Entry中的旧内容
        RadarinstallApk.insert(0, file_path)  # 插入新的文件路径


RadarinstallApk = tk.Entry(SmartAI, validate='key',width=60, font=("微软雅黑", 9))
RadarinstallApk.place(x=25, y=350)
open_button = tk.Button(SmartAI, text="选择推包文件", command=open_file,bd=1,width=12,height=1)
open_button.place(x=465, y=346)
push_text = canvas2.create_text(200, 330, text='在此处填写路径或者语音指令，工具会自动识别当前设备车型', fill='grey', font=('微软雅黑', 10))
disable = tk.Button(SmartAI, text="安装APK", command=ApkPrompt,bd=1,width=12,height=1)
disable.place(x=355, y=280)
disable = tk.Button(SmartAI, text="恢复大屏环境", command=ReturnNormal,bd=1,width=12,height=1)
disable.place(x=465, y=440)



scrollbar.config(command=text.yview)