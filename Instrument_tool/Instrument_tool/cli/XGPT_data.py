import os

from lib import *

#获取Rom版本号
def RomInfo():
    rom = subprocess.check_output(f'adb shell "getprop | grep xiaopeng.software"', shell=True,universal_newlines=True)
    return rom[25:-2]

#获取语音版本号
def CarSpeechInfo():
    carspeech = subprocess.check_output(f'adb shell "dumpsys package com.xiaopeng.carspeechservice  | grep versionName"', shell=True,
                                  universal_newlines=True)
    return carspeech[16:45]

#获取小P形象版本号
def AiassistantInfo():
    aiassistant = subprocess.check_output(f'adb shell "dumpsys package com.xiaopeng.aiassistant | grep versionName"', shell=True,
                                  universal_newlines=True)
    return aiassistant[16:45]

#获取AI小P版本号
def XgptInfo():
    xgpt = subprocess.check_output(f'adb shell "dumpsys package com.xiaopeng.xgpt | grep versionName"', shell=True,
                                  universal_newlines=True)
    return xgpt[16:45]

#获取hardwareId
def HardwareIdInfo():
    hardwareId = subprocess.check_output(f'adb shell "getprop | grep hardwareId"', shell=True, universal_newlines=True)
    match = re.search('hardwareId]:(.*)', hardwareId, re.DOTALL)
    if match:
        return match.group(1)

#获取Devices
def DevicesInfo():
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, text=True)
    output_lines = result.stdout.splitlines()
    # 获取第二行内容
    if len(output_lines) >= 2:
        second_line = output_lines[1]
        return second_line[0:8]

#获取vin
def VinInfo():
    vin = subprocess.check_output(f'adb shell "getprop | grep persist.sys.xiaopeng.vin"', shell=True, universal_newlines=True)
    match = re.search('eng.vin]:(.*)', vin, re.DOTALL)
    if match:
        vin = match.group(1)
        vin = vin[:-1]
        return vin

#截图大屏
def Screen_cli():
    os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png %s\%s_inspect.png' % (pic_path, time.strftime("%Y-%m-%d_%H-%M-%S")))

#大屏投屏
def DisScrcpy_cli():
    subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
    subprocess.run([scrcpy_path])

#大屏录屏
def VideoScrcpy_cli():
    subprocess.check_output(f'adb root', shell=True, universal_newlines=True)
    subprocess.run([scrcpy_path, '--record','%s\%s_video.mp4'%(video_path,time.strftime("%Y-%m-%d_%H-%M-%S"))])

#打开截图文件夹
def Open_pic():
    os.system('start explorer %s' % (pic_path))

#重启设备
def Reboot_cli():
    subprocess.check_output(f'adb reboot soc', shell=True, universal_newlines=True)

#切换昼夜模式
def Switch_DayNight_cli():

    subprocess.check_output(f'adb shell am broadcast -a com.xiaopeng.intent.action.SWITCH_DAYNIGHT', shell=True,
                            universal_newlines=True)

#打开录像文件夹
def Open_video():
    os.system('start explorer %s' % (video_path))

#拉LOG0
def Log0_cli():
    os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('adb pull /cli/Log/log0 %s\log0' % (new_path))
    os.system(
        'powershell Compress-Archive %s\log0 %s\log0_%s.zip' % (new_path, new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('rd/s/q %s\log0' % (new_path))



#拉All LOG
def AllLog_cli():
    os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png %s\%s_inspect.png' % (new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('adb pull /cli/Log %s\ALLlog' % (new_path))
    os.system('powershell Compress-Archive %s\ALLlog %s\ALLlog_%s.zip' % (
    new_path, new_path, time.strftime("%Y-%m-%d_%H-%M-%S")))
    os.system('rd/s/q %s\ALLlog' % (new_path))

def Open_Log():
    os.system('start explorer %s' % (new_path))

#推包
def Intall_cli(route):
    try:
        Return = subprocess.check_output(
            f'adb install -r -t -d %s' % (route), shell=True, universal_newlines=True)
        return Return
    except subprocess.CalledProcessError:
        return False

#获取AI小P进程号
def GetxgptPid_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.xgpt"', shell=True, universal_newlines=True)
    return pid

#killAI小P进程
def Killxgpttrument_cli():
    subprocess.check_output(f'adb shell "pidof com.xiaopeng.xgpt | xargs kill"', shell=True,
                            universal_newlines=True)

#获取语音进程号
def GetCSSPid_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.carspeechservice"', shell=True, universal_newlines=True)
    return pid

#kil语音进程
def KillCarSpeechService_cli():
    subprocess.check_output(f'adb shell "pidof com.xiaopeng.carspeechservice  | xargs kill"', shell=True,
                            universal_newlines=True)

#获取小P形象进程号
def GetAIAPid_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.aiassistant  ', shell=True, universal_newlines=True)
    return pid

#kill小P形象进程
def KillAiassistant_cli():
    subprocess.check_output(f'adb shell "pidof com.xiaopeng.aiassistant | xargs kill"', shell=True,
                            universal_newlines=True)

#获取爱卡宾进程号
def GetAicaPid_cli():
    pid = subprocess.check_output(f'adb shell "pidof com.xiaopeng.aicabinservice', shell=True, universal_newlines=True)
    return pid

#kill爱卡宾进程
def KillAicabin_cli():
    subprocess.check_output(f'adb shell "pidof com.xiaopeng.aicabinservice | xargs kill"', shell=True,
                            universal_newlines=True)

#唤醒小P
def CallXP_cli():
    subprocess.check_output(f'adb shell am broadcast -a xiaopeng.intent.action.UI_MIC_CLICK --es location "key_speech"',
                            shell=True, universal_newlines=True)

#发送小P指令
def DispatchOrders_cli(Value):
    subprocess.check_output(f'adb shell am broadcast -a carspeechservice.ACTION_SEND_TEXT --es text %s" --ei soundArea 0'%(Value),
                            shell=True, universal_newlines=True)

#执行Disable
def Disable_cli():
    subprocess.check_output(f'adb disable-verity"', shell=True, universal_newlines=True)
    subprocess.check_output(f'adb reboot"', shell=True, universal_newlines=True)

#打开语音环境调试开关
def DialogDebug_cli():
    os.system('adb shell am start -a carspeechservice.action.debug')

#打开工厂APK
def DFactoryApkOpen_cli():
    os.system('adb shell am start -n com.xiaopeng.factory/com.xiaopeng.factory.view.factorytest.AllTestActivity')

#推工厂APK

alpha_8155 = "./FactoryApk/8155alpha/8155_FactoryTest_nossh_alpha_release/push_factorytest.bat"
dev_8155 = "./FactoryApk/8155dev/push_factorytest"
alpha_8295 = "./FactoryApk/8295_XpFactoryTest_release_20230406/push_factorytest.bat"
dev_8295 = "./FactoryApk/8295_XpFactoryTest_dev_20230404/push_factorytest"

def PushFactoryApk_cli():
    #先判断当前是dev还是aipha
    rom = subprocess.check_output(f'adb shell "getprop | grep xiaopeng.software"', shell=True, universal_newlines=True)
    car = subprocess.check_output(f'adb shell "getprop | grep ro.product.odm.name"', shell=True, universal_newlines=True)
    if 'DEV' in rom[25:88]:
        # dev = True
        print('dev')
        # 再判断是否为8295平台
        if '8295' in car:
            i = '8295dev'
        else:
            i = '8155dev'
    else:
        print('非dev')
        # 再判断是否为8295平台
        if '8295' in car:
            i = '8295alpha'
        else:
            i = '8155alpha'
    print(i)
    if PushFactoryApk(i) == False:
        return False
    else:
        print('APK推成功')
        return True



#推XGPT包
def Intallxgpt_cli(route):
    os.system('adb remount')
    apk = subprocess.check_output(
        f'adb shell pm path com.xiaopeng.xgpt', shell=True,universal_newlines=True)
    match = re.search('package:(.*)', apk, re.DOTALL)
    car = match.group(1)
    Return = subprocess.check_output(f'adb push %s %s' % (route,car), shell=True,
        universal_newlines=True)
    print('推包路径位:'+car)
    return Return

#清理缓存
def ClearCache():
    os.system('adb root')
    os.system('adb shell pm clear com.xiaopeng.xgpt')

#调整AI小P环境
button_ChangeApk = ButtonClicks()
def ChangeApk_cli():
    i = 1 + button_ChangeApk.clicks % 2
    if i == 1:
        subprocess.check_output(f'adb shell am broadcast -a com.xp.xgpt.switch.cloud.envir --ez "switchPre" true',
                                shell=True, universal_newlines=True)
        print('应用已切换为预发')
        button_ChangeApk.clicks += 1
        return '预发'
    else:
        subprocess.check_output(f'adb shell am broadcast -a com.xp.xgpt.switch.cloud.envir --ez "switchPre" false',
                                shell=True, universal_newlines=True)
        print('应用已切换到正式')
        button_ChangeApk.clicks += 1
        return '正式'

#屏幕轨迹指针开关
button_ScreenPrint = ButtonClicks()
def ScreenPrint_cli():
    i = 1 + button_ScreenPrint.clicks % 2
    if i == 1:
        subprocess.check_output(f'adb shell settings put system show_touches 1',shell=True, universal_newlines=True)
        subprocess.check_output(f'adb shell settings put system pointer_location 1', shell=True, universal_newlines=True)
        print('屏幕轨迹打开')
        button_ScreenPrint.clicks += 1
        return True
    else:
        subprocess.check_output(f'adb shell settings put system show_touches 0',shell=True, universal_newlines=True)
        subprocess.check_output(f'adb shell settings put system pointer_location 0', shell=True, universal_newlines=True)
        print('屏幕轨迹关闭')
        button_ScreenPrint.clicks += 1
        return False

speechs_ViewOutsideCar = [
    #图生文感知车外世界
    '车辆前方是什么','左边的人有多高','后面的建筑是什么','右边的树是什么树',
]
speechs_Encyclopedia = [
    #小P百科
    '双缝实验','什么是万有引力','冰岛的首都在哪里','什么是琴生不等式',
]
speechs_CarQA = [
    #用车问答
    '怎么加玻璃水','怎么打开后备箱','怎么打开前舱盖','充电口盖该如何打开',
]
speechs_search = [
    #联网搜索
    '联网搜索成龙的成就','联网搜索路易十六','联网搜索广州的平均房价','联网搜索小鹏汽车的股价',
]
speechs_Chat = [
    #日常闲聊
    '香菇掉进厕所里还是香菇吗','等待交通灯为什么叫做等红灯而不是等绿灯','鸡你太美是什么意思','学法律的人为什么叫做律师而不是叫做法师',
]
speechs_OtherOrder = [
    #其他指令
    '打开座椅加热','我有点冷','帮我把车耳朵收起来吧','我有点闷想透透气'
]
speechs_Draw = [
    #小P绘画
    '画个孙悟空','画个太阳','画个诸葛亮','画个开飞船的小P',
]
speechs_StoryTell = [
    #故事创作
    '创作一个公主和王子的故事','创作一个灰姑娘的故事','创作一个冒险朵拉的故事','创作一个奥特曼决战小怪兽的故事',
]

def SendInstructions_cli(Value):

    orders = {'图生文':speechs_ViewOutsideCar,'小P百科':speechs_Encyclopedia,
              '用车问答':speechs_CarQA,'联网搜索':speechs_search,
              '日常闲聊':speechs_Chat,'其他指令':speechs_OtherOrder,
              '小P绘画':speechs_Draw,'故事创作':speechs_StoryTell}
    if Value == '选择指令类型':
        pass
    else:
        # subprocess.check_output(f'adb shell am broadcast -a xiaopeng.intent.action.UI_MIC_CLICK --es location "key_speech"',
        #                         shell=True, universal_newlines=True)
        os.system('adb shell am broadcast -a xiaopeng.intent.action.UI_MIC_CLICK --es location "rear_left"')
        time.sleep(1)
        # subprocess.check_output(f'adb shell am broadcast -a "carspeechservice.ACTION_SEND_TEXT" --es text %s' % (
        #     random.choice(orders.get(Value))),
        #                         shell=True, universal_newlines=True)
        os.system('adb shell am broadcast -a carspeechservice.ACTION_SEND_TEXT --es "text" "%s" --ei soundArea 2'%(random.choice(orders.get(Value))))
    # time.sleep(5)
    # subprocess.check_output(f'adb shell am broadcast -a xiaopeng.intent.action.UI_MIC_CLICK --es location "key_speech"',
    #                         shell=True, universal_newlines=True)


VinWriteIn={
            'XPENGE2840000D080360C644':'TESTDAVID1ET2-011',
            'XPENGE284000110F01C09321':'XPENGE284000110F0',
            'XPENGD5540000B0A1070FC15':'LMVHFEFZ8KA777832',
            'XPENGE2840800D120B000176':'LMVHFEFZ000000090',
            'XPENGE38000000000000000':'L1NSPGHB1LA018459',
            'XPENGE384000900FD35FF319':'L1NSPGHB6LA004111',
            'XPENGE284080070AD85FF319':'LMVHFEFZKEL007711',
            'XPENGE28A0000000000000000':'TESTXPENGE28a1103',
            'XPENGE380000000000000002':'L1NSPGHB8LA000078',
            'XPENGE380000000000000000':'TESTVIN1007004902',
            'XPENGE38100700344C570081':'test_vinwz0000001',
            'XPENGE38100700344C570291':'L1NNSGHB1NA093485',
            'XPENGF300700354253011036':'TESTXPENGF30x0622',
            'XPENGE28A074535453702101A':'TESTXPENGE28a0721',
            'XPENGF300000000000000000':'L1NNSGHA4NA991087',
            'XPENGE284000900FD35FF319':'LMVHFEFZ4KM668112',
            'XPENGE28A0745354536041006':'TESTXPENGE28A4106',
            'XPENGH930000000000000000':'L1NNSGHC5NB910014',
            'XPENGF304142431234567897':'TESTQQWERTESTCS02',
            'XPENGE28A0745354644011001':'TESTVINFLTCS19988',
            'XPENGE28A0745354B41071007':'TESTVINFLTCS00325',
            'XPENGF300701364352061013':'LMVHFEFZ4KM621748',
            'XPENGH9370036424D9100104':'TESTVINH93CS00104',
            'XPENGH930700354B50001018':'TESTDAPINGH93XF03',
            'XPENGH930700354A4E001005':'TESTQQWERTESTCS01',
            'XPENGH93070036424D00100A':'L1NNSGHB1NA093093',
            'XPENGE380700354559301003':'TESTXPENGE3822232',
            'XPENGF300700354B37061008':'F30TESTING3706100',
            'XPENGF570700364A4605100D':'TEST2023101100957',
            'XPENGH93070036445404100A':'L1NNSGHA9NB912393',
            'XPENGF300701364C310A1327':'L1NNSGHA5PB035647',
            'XPENGE387465737435663131':'LMVHFEFZ8KA703256',
            'XPENGE380745364D4A05102A':'TEST2728716272638',
            'XPENGE380745364D4A05106K':'L1NSPGHB0PA008973',
            'XPENGF570745364D4A05102A':'TEST2728716272638',
            'XPENGH930000020228203D1F':'TESTXPENGH93X0131',
            'XPENGH930700364B4A021028':'LTEST93HA12121432'
            }

def ReturnNormal_cli():
    os.system('adb root')
    os.system('adb remount')
    os.system('adb shell rm -rf /sdcard/pre_env.ini')
    os.system('adb reboot')
