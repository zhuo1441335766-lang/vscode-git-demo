import os

from  lib import *

#执行Disable
def Disable_cli():
    subprocess.check_output(f'adb disable-verity"', shell=True, universal_newlines=True)
    subprocess.check_output(f'adb reboot"', shell=True, universal_newlines=True)

#获取Rom版本号
def RomInfo():
    rom = subprocess.check_output(f'adb shell "getprop | grep xiaopeng.software"', shell=True,universal_newlines=True)
    return rom[25:-2]

#获取仪表版本号
def InstrumentInfo():
    try:
        ins = subprocess.check_output(f'adb shell "dumpsys package com.xiaopeng.instrument | grep versionName"', shell=True,
                                      universal_newlines=True)
        return ins[16:47]
    except Exception as e:
        return '无仪表设备\n'

#获取科技岛版本号
def techislandInfo():
    try:
        ins = subprocess.check_output(f'adb shell "dumpsys package com.xiaopeng.techisland | grep versionName"', shell=True,
                                      universal_newlines=True)
        return ins[16:47]
    except Exception as e:
        return '无科技岛设备\n'

#获取MCU版本号
def McuInfo():
    mcu = subprocess.check_output(f'adb shell "getprop | grep persist.sys.mcu"', shell=True, universal_newlines=True)
    match = re.search('sys.mcu.version]:(.*)', mcu, re.DOTALL)
    return match.group(1)

#获取当前设备CFC码
def CfcInfo():
    cfc = subprocess.check_output(f'adb shell "getprop | grep boot.vehicle_cfc]"', shell=True, universal_newlines=True)
    match = re.search('hicle_cfc]:(.*)', cfc, re.DOTALL)
    if match:
        # return match.group(1)
        cfc = match.group(1)
        cfc= cfc[:22] + ']\n'
        return cfc
def VinInfo():
    cfc = subprocess.check_output(f'adb shell "getprop | grep persist.sys.xiaopeng.vin"', shell=True, universal_newlines=True)
    match = re.search('eng.vin]:(.*)', cfc, re.DOTALL)
    if match:
        vin = match.group(1)
        vin = vin[:-1]
        return vin

#重启设备
def Reboot_cli():
    subprocess.check_output(f'adb reboot soc', shell=True, universal_newlines=True)

#切换昼夜模式
def Switch_DayNight_cli():

    subprocess.check_output(f'adb shell am broadcast -a com.xiaopeng.intent.action.SWITCH_DAYNIGHT', shell=True,
                            universal_newlines=True)

#获取仪表进程号
def GetInsPid_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.instrument"', shell=True, universal_newlines=True)
    return pid

#kill仪表进程
def KillInstrument_cli():
    subprocess.check_output(f'adb shell "pidof com.xiaopeng.instrument | xargs kill"', shell=True,
                            universal_newlines=True)

#获取SR进程号
def GetSubPid_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.subreality', shell=True, universal_newlines=True)
    return pid

#kill SR进程号
def KillSubreality_cli():
    subprocess.check_output(f'adb shell "pidof com.xiaopeng.subreality | xargs kill"', shell=True,
                            universal_newlines=True)

#获取地图进程号
def GetMapPid_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.montecarlo', shell=True, universal_newlines=True)
    return pid

#kill 地图进程号
def KillMontecarlo_cli():
    subprocess.check_output(f'adb shell "pidof com.xiaopeng.montecarlo | xargs kill"', shell=True,
                            universal_newlines=True)

#kill 科技岛进程号
def KillTechIsland_cli():
    subprocess.check_output(f'adb shell "pidof com.xiaopeng.techisland | xargs kill"', shell=True,
                            universal_newlines=True)

#kill 科技岛进程号
def GetTechIsland_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.techisland "', shell=True,
                            universal_newlines=True)
    return str(pid)


def KillSystemUi_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.systemui | xargs kill"', shell=True,
                            universal_newlines=True)
    return str(pid)
def GetSystemUi_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.systemui"', shell=True,
                            universal_newlines=True)
    return str(pid)

def Getsmartcontrol_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.smartcontrol"', shell=True,
                            universal_newlines=True)
    return str(pid)
def killsmartcontrol_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.smartcontrol | xargs kill"', shell=True,
                            universal_newlines=True)
    return str(pid)

#拉LOG0
def Log0_cli():
    GetCarType_Screencap()
    os.system(
        'adb pull /sdcard/yibiaoscreenshot.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('adb shell gsnap /cli/pic.jpg /dev/fb0')
    os.system(
        'adb pull /cli/pic.jpg %s\%s_inspect.png' % (pic_path,time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('adb pull /cli/Log/log0 %s\log0' % (new_path))
    os.system(
        'powershell Compress-Archive %s\log0 %s\log0_%s.zip' % (new_path, new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('rd/s/q %s\log0' % (new_path))


    #如果有仪表屏车型，则顺带把大屏也截图
    if JudgeScreen() == True:
        os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
        os.system('adb pull /sdcard/screenshot.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
        print('判断为有仪表屏车型，pull日志时会顺带截图')
    #如果有科技岛车型，则顺带截图
    if JudgeLand() == True:
        GetCarType_ScreencapLand()
        os.system(
            'adb pull /sdcard/TechIsland.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
        print('判断有科技岛应用，pul日志l时会顺带截图')


#拉All LOG
def AllLog_cli():
    GetCarType_Screencap()
    os.system(
        'adb pull /sdcard/yibiaoscreenshot.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('adb shell gsnap /cli/pic.jpg /dev/fb0')
    os.system(
        'adb pull /cli/pic.jpg %s\%s_inspect.png' % (pic_path,time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('adb pull /cli/Log %s\ALLlog' % (new_path))
    os.system('powershell Compress-Archive %s\ALLlog %s\ALLlog_%s.zip' % (
    new_path, new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('rd/s/q %s\ALLlog' % (new_path))
    #如果有仪表屏车型，则顺带把大屏也截图
    if JudgeScreen() == True:
        os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
        os.system('adb pull /sdcard/screenshot.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
        print('判断为有仪表屏车型，pull日志时会顺带截图')
    #如果有科技岛车型，则顺带截图
    if JudgeLand() == True:
        GetCarType_ScreencapLand()
        os.system(
            'adb pull /sdcard/TechIsland.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
        print('判断有科技岛应用，pull日志时会顺带截图')
#拉QNXLog
def QNXLog_cli():
    GetCarType_Screencap()
    os.system(
        'adb pull /sdcard/yibiaoscreenshot.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('adb pull /qnx/cli/Log %s\QNXlog' % (new_path))
    os.system('powershell Compress-Archive %s\QNXlog %s\QNXlog_%s.zip' % (
    new_path, new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('rd/s/q %s\QNXlog' % (new_path))
    #如果有仪表屏车型，则顺带把大屏也截图
    if JudgeScreen() == True:
        os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
        os.system('adb pull /sdcard/screenshot.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
        print('判断为有仪表屏车型，pull日志时会顺带截图')
    #如果有科技岛车型，则顺带截图
    if JudgeLand() == True:
        GetCarType_ScreencapLand()
        os.system(
            'adb pull /sdcard/TechIsland.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
        print('判断有科技岛应用，pull日志时会顺带截图')
#打开LOG文件夹
def Open_Log():
    os.system('start explorer %s' % (new_path))

#仪表截图
def ScreenIns_cli():
    GetCarType_Screencap()
    os.system(
        'adb pull /sdcard/yibiaoscreenshot.png %s\%s_inspect.png' % (pic_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('adb shell gsnap /cli/pic.jpg /dev/fb0')
    os.system(
        'adb pull /cli/pic.jpg %s\%s_inspect.png' % (pic_path,time.strftime("%Y-%m-%d_%H-%M-%S")))

#科技岛截图
def ScreenLand_cli():
    GetCarType_ScreencapLand()
    os.system(
        'adb pull /sdcard/TechIsland.png %s\%s_inspect.png' % (pic_path, time.strftime("%Y-%m-%d_%H-%M-%S")))

#截图大屏
def Screen_cli():
    os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png %s\%s_inspect.png' % (pic_path, time.strftime("%Y-%m-%d_%H-%M-%S")))


#推仪表包
def Intall_cli(route):
    apk = subprocess.check_output(f'adb shell pm path com.xiaopeng.instrument', shell=True, universal_newlines=True)
    match = re.search('package:(.*)', apk, re.DOTALL)
    car = match.group(1)
    Return = subprocess.check_output(f'adb push %s %s' % (route,car), shell=True,
        universal_newlines=True)
    print('推包路径为:'+car)
    return Return

#推科技岛包
def IntallLand_cli(route):
    apk = subprocess.check_output(f'adb shell pm path com.xiaopeng.techisland', shell=True, universal_newlines=True)
    match = re.search('package:(.*)', apk, re.DOTALL)
    car = match.group(1)
    Return = subprocess.check_output(f'adb push %s %s' % (route,car), shell=True,
        universal_newlines=True)
    print('推包路径为:'+car)
    return Return
#升级MCU
def UpdateMcu_cli(route):

    os.system('adb shell mkdir storage/mydisk')
    os.system('adb shell mkdir storage/mydisk/mcu')
    os.system('adb push  %s /storage/mydisk/mcu/' % (route))
    p = subprocess.Popen('adb shell vdt mcuUpdate', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(p.stdout.readline, b''):
        print(line)

#禁收CAN信号
button_ProhibitMcu = ButtonClicks()
def ProhibitMcu_cli():
    i = 1 + button_ProhibitMcu.clicks % 2
    if i == 1:
        button_ProhibitMcu.clicks += 1
        return True
    else:
        button_ProhibitMcu.clicks += 1
        return False

#仪表投屏
def OpenScrcpy_cli():
    try:
        instrument_id = get_cluster_display_id()
        print('仪表应用所在displayid为%s'%(instrument_id) )
    except Exception as e:
        #get_cluster_display_id的方法get不到仪表的display ID 故将ID写死为1
        print('自动获取仪表display id失败，让用户手动选择投屏ID')
        instrument_id = 1
    subprocess.run([scrcpy_path,'--display-id',str(instrument_id)])

#科技岛投屏
def OpenLandScrcpy_cli():
    subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
    try:
        TechIsland_id = get_techIsland_display_id()
    except Exception as e:
        #get_cluster_display_id的方法get不到仪表的display ID 故将ID写死为3
        print('自动获取仪表display id失败，将投屏display 3')
        TechIsland_id = 3
    subprocess.run([scrcpy_path,'--display-id',str(TechIsland_id)])
#仪表录屏
def VideoScrcpy_cli():
    subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
    instrument_id = get_cluster_display_id()
    print('仪表应用所在displayid为%s' % (instrument_id))
    subprocess.run([scrcpy_path, '--display-id', str(instrument_id),
                    '--record','%s\%s_video.mp4'%(video_path,time.strftime("%Y-%m-%d_%H-%M-%S"))])

#大屏录屏
def VideoBigScrcpy_cli():
    subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
    subprocess.run([scrcpy_path, '--record','%s\%s_video.mp4'%(video_path,time.strftime("%Y-%m-%d_%H-%M-%S"))])

#科技岛录屏
def VideoLandScrcpy_cli():
    subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
    TechIsland_id = get_techIsland_display_id()
    print('科技岛应用所在displayid为%s' % (TechIsland_id))
    subprocess.run([scrcpy_path, '--display-id', str(TechIsland_id),
                    '--record','%s\%s_video.mp4'%(video_path,time.strftime("%Y-%m-%d_%H-%M-%S"))])



#大屏投屏
def DisScrcpy_cli():
    subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
    subprocess.run([scrcpy_path])

#打开录像文件夹
def Open_video():
    os.system('start explorer %s' % (video_path))

#打开截图文件夹
def Open_pic():
    os.system('start explorer %s' % (pic_path))

#跳过OOBE
def SkipOOBE_cli():
    os.system('adb shell pm disable com.xiaopeng.oobe')

#调整日志等级
def SetLogDeBug_cli():
    os.system('adb shell setprop persist.hmi.log_level 5')

#海外切语言
def SwitchLanguage_cli(Value):
    orders = {'挪威':'nb','荷兰':'nl','瑞典':'sv','丹麦':'da','意大利':'it','西班牙':'es','英语（英国）':'en-GB',
'法语':'fr','德语':'de','泰语':'th','阿拉伯语':'ar','希伯来语':'iw','繁体':'zh-Hant','英语（美国）':'en-US','简体中文':'zh-Hans'}
    if Value == '海外切语言':
        pass
    else:
        subprocess.check_output(f'adb shell am broadcast -a NAPA_MOCK --es v1 "settings" --es v2 "DisplayUIManager" --es v3 "setLanguage" --es v4 "%s"'
                                % (orders.get(Value)),shell=True, universal_newlines=True)

#安装Carplay，AndroidAuto应用
def InstallPhoneMapApp_cli():
    os.system(f'adb install .\\resources\\client-debug.apk')
    print('安装成功')

#海外版本激活地图
def ActivationMap_cli():
    os.system('adb shell setprop persist.sys.xiaopeng.XPU 1')
    os.system('adb shell setprop sys.xiaopeng.vin F30MAPperfom00001')
    os.system('adb shell setprop persist.sys.xiaopeng.vin F30MAPperfom00001')
    os.system('adb shell "pidof com.xiaopeng.montecarlo | xargs kill"')
    time.sleep(5)
    os.system('adb shell am broadcast -a com.xiaopeng.montecarlo.BROADCAST_ONE_KEY_ACTIVATION -n com.xiaopeng.montecarlo/com.xiaopeng.montecarlo.app.test.broadcast.TestBroadCastReceiver')

def SetConfig_cli(getconfig):
    if getconfig == '最高配':
        os.system('adb root')
        os.system('adb shell setprop persist.sys.xiaopeng.debug.cfc 1')
        os.system('adb shell setprop persist.xiaopeng.cfcIndex 4')
        os.system('adb shell setprop persist.sys.xiaopeng.cfcVehicleLevel 4')
        os.system('adb shell setprop persist.sys.xiaopeng.RDM 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SRS 1')
        os.system('adb shell setprop persist.sys.xiaopeng.ESP 1')
        os.system('adb shell setprop persist.sys.xiaopeng.EPS 1')
        os.system('adb shell setprop persist.sys.xiaopeng.IBT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.IPUR 1')
        os.system('adb shell setprop persist.sys.xiaopeng.BMS 1')
        os.system('adb shell setprop persist.sys.xiaopeng.OBC_DCDC 1')
        os.system('adb shell setprop persist.sys.xiaopeng.ATLS 1')
        os.system('adb shell setprop persist.sys.xiaopeng.AQS 1')
        os.system('adb shell setprop persist.sys.xiaopeng.LLU 1')
        os.system('adb shell setprop persist.sys.xiaopeng.LSU 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSB 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MIRROR 1')
        os.system('adb shell setprop persist.sys.xiaopeng.ATL_NUMBER 17')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMD 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMP 1')
        os.system('adb shell setprop persist.sys.xiaopeng.LUMBAR_SUP 1')
        os.system('adb shell setprop persist.sys.xiaopeng.IMU 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMD_HEAT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMP_HEAT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMD_VENT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMP_VENT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.IPUF 1')
        os.system('adb shell setprop persist.sys.xiaopeng.XPU 1')
        os.system('adb shell setprop persist.sys.xiaopeng.AVM 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SRR_RL 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SRR_RR 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SRR_FL 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SRR_FR 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SECROW_RT_HEAT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SECROW_LT_HEAT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMD_LSU 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMP_LSU 1')
        os.system('adb shell setprop persist.sys.xiaopeng.AS_WELCOME 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMD_CUSHEXT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMP_CUSHEXT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SECROW_RT_CUSHEXT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SECROW_LT_CUSHEXT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMD_MASSG 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MSMP_MASSG 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SECROW_RT_MASSG 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SECROW_LT_MASSG 1')
        os.system('adb shell setprop persist.sys.xiaopeng.CWC 1')
        os.system('adb shell setprop persist.sys.xiaopeng.AS 1')
        os.system('adb shell setprop persist.sys.xiaopeng.driveway 1')
        os.system('adb shell setprop persist.sys.xiaopeng.Package1 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SPEAKER 20')
        os.system('adb shell setprop persist.sys.xiaopeng.SFS 1')
        os.system('adb shell setprop persist.sys.xiaopeng.AMP 1')
        os.system('adb shell setprop persist.sys.xiaopeng.ATL_18 1')
        os.system('adb shell setprop persist.sys.xiaopeng.ATL_19 1')
        os.system('adb shell setprop persist.sys.xiaopeng.TBOX_5G_A 1')
        os.system('adb shell setprop persist.sys.xiaopeng.TBOX_4G 0')
        os.system('adb shell setprop persist.sys.xiaopeng.SHC 1')
        os.system('adb shell setprop persist.sys.xiaopeng.LEG_SUP 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SWS_HEAT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SECROW_WELCOME 1')
        os.system('adb shell setprop persist.sys.xiaopeng.SEAT_MASS 1')
        os.system('adb shell setprop persist.sys.xiaopeng.MAKEUP_MIRROR 1')
        os.system('adb shell setprop persist.sys.xiaopeng.DOLBY 1')
        os.system('adb shell setprop persist.sys.xiaopeng.RSEAT_HEAT 1')
        os.system('adb shell setprop persist.sys.xiaopeng.Package2 1')
        os.system('adb shell setprop persist.sys.xiaopeng.Lidar_F 1')
        os.system('adb shell setprop persist.sys.xiaopeng.Lidar_R 1')
        os.system('adb shell setprop persist.sys.xiaopeng.ETC 1')
        os.system('adb shell setprop persist.sys.xiaopeng.TTM 1')
        os.system('adb shell setprop persist.sys.xtheme.support 1')
        os.system('adb shell setprop persist.sys.xiaopeng.XSPORT 1')
        os.system('adb reboot soc')
    elif getconfig == '最低配':
        os.system('adb root')
        os.system('adb shell setprop persist.sys.xiaopeng.debug.cfc 0')
        os.system('adb shell setprop persist.xiaopeng.cfcIndex 0')
        os.system('shell setprop persist.sys.xiaopeng.SFS 0')
        os.system('adb reboot soc')
    else:
        pass