import os
import random
from tkinter.ttk import Combobox
import threading
from tkinter import messagebox
import tkinter as tk
from tkinter import *

from tkinter import filedialog
import subprocess
import re
import time
import serial
import serial.tools.list_ports


#调用本地的adb去使用
adb_path = "./resources/adb"
# subprocess.run([scrcpy_path])
subprocess.run([adb_path, 'devices'])

#在所在目录下寻找投屏应用
scrcpy_path = "./resources/scrcpy"



current_dir = os.getcwd()   #获取当前工程文件所在目录
new_path = os.path.join(current_dir, 'Log')     #定义文件夹以及路径

# 检查路径是否存在，如果不存在则创建
if not os.path.exists(new_path):
    os.makedirs(new_path)

pic_path = os.path.join(current_dir, 'pic')  # 定义文件夹以及路径

# 检查当前路径下有没有截图文件夹，没有则创建
if not os.path.exists(pic_path):
    os.makedirs(pic_path)

video_path = os.path.join(current_dir, 'Video')     #定义文件夹以及路径

# 检查路径是否存在，如果不存在则创建
if not os.path.exists(video_path):
    os.makedirs(video_path)

image_path = os.path.join(current_dir, 'image')     #定义文件夹以及路径


#设置主界面大小
root = tk.Tk()
root.geometry("1000x540")
root.title("仪表测试小工具")
pixel = tk.PhotoImage(width=1, height=1)
menubar = Menu(root)



# 将菜单放置在主窗口
root.config(menu=menubar)

#限制了输入框只能输入数字
def only_numeric_input(P):
    if P.startswith('-') and (P[1:].replace('.', '', 1).isdigit() or P[1:] == ''):
        return True
    elif P.replace('.', '', 1).isdigit():
        return True
    elif P == "":
        return True
    else:
        return False

vcmd = (root.register(only_numeric_input), '%P')

#计数器，记录按钮按下次数
class ButtonClicks:
    def __init__(self):
        self.clicks = 0

#简化ABD命令
def vdt(prop, value):
    if isinstance(value, list):
        valStr = ' '.join(str(i) for i in value)
    else:
        valStr = str(value)
    os.system('adb root')
    os.system('adb shell vdt rp %s %s' % (prop, valStr))


def vdts(dict):
    for key, val in dict.items():
        vdt(key, val)



#生成当前系统时间戳
def System_Time():
    i = time.strftime("%Y-%m-%d %H:%M:%S")
    return i

#检查当前设备是否正常连接
def Test():
    try:
        subprocess.check_output(f'adb root', shell=True,universal_newlines=True)
    except subprocess.CalledProcessError:
        return False

#识别当前串口端口号

def get_available_ports():
    """Lists serial port names

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of the serial port names available on the system
    """
    if os.name == 'posix':
        # POSIX (LINUX, MAC OS X, BSD, UNIX, etc.)
        # this excludes your current terminal "/dev/tty"
        default_list = ['/dev/ttyS%s' % i for i in range(0, 256)]
        default_list += ['/dev/ttyUSB%s' % i for i in range(0, 256)]
        default_list += ['/dev/ttyACM%s' % i for i in range(0, 256)]
        default_list += ['/dev/tty.usbserial%s' % i for i in range(0, 256)]
        default_list += ['/dev/ttyAMA%s' % i for i in range(0, 256)]
        default_list += ['/dev/tty.usbmodem%s' % i for i in range(0, 256)]
        default_list += ['/dev/tty.usb-serial%s' % i for i in range(0, 256)]
        # Raspberry Pi serial port
        default_list += ['/dev/ttyS0', '/dev/ttyAMA0']
        ports = [port for port in serial.tools.list_ports.comports()
                 if port.device in default_list]
    elif os.name == 'nt':
        # Windows
        ports = list(serial.tools.list_ports.comports())
    else:
        raise EnvironmentError('Unsupported platform')

    return [port.device for port in ports]


def QNX_PORT():
    available_ports = str(get_available_ports())
    return available_ports[2:-2]


# 打开串口，设置串口参数
def serial_data(com,value):
    if com =="":
        com = 'COM12'
    if value =="":
        value = 115200
    try:
        serials = serial.Serial(com, value, timeout=1)  # 串口名、波特率、超时设置
        return serials
    except serial.SerialException as e:
        print(f"串口打开失败:暂未正常连接台架")




ser = serial_data(QNX_PORT(), '')


# 检查串口是否被打开
# if ser.isOpen():
#     print(ser.name + ' is open...')

# 发送串口指令，将指令封装起来
def QNXcmd(cmd,value):

    try:
        cmds = 'vdt rp '+cmd +' '+ str(value)
        bytes_data = cmds.encode()  # 默认使用UTF-8编码
        ser.write(bytes_data + b'\n')  # 发送字节数据

    except Exception as e:
        print(f"因为暂未连接串口设备或者有其他应用占用了端口，\n故QNX侧指令无法发送..")





  #判断输入的路径是否有效
def is_valid_path(path):
    return os.path.isdir(path) or os.path.isfile(path)

#检查当前路径是否有效
def TestRoute(route):
    if route == "":
        return False
    else:
        pass

#根据当前车型截图仪表
def GetCarType_Screencap():
    # rom = subprocess.check_output(f'adb shell "getprop | grep xiaopeng.software"', shell=True, universal_newlines=True)
    # CarMode = rom[34:37]
    # car = ['H93','F57',]
    # if CarMode in car:
    #     os.system('adb shell screencap -p -d 2  /sdcard/yibiaoscreenshot.png')
    # else:
    try:
        instrument_id = get_cluster_display_id()
        print('仪表应用所在displayid为%s'%(instrument_id) )
    except Exception as e:
        #get_cluster_display_id的方法get不到仪表的display ID 故将ID写死为1
        print('自动获取仪表display id失败，将使用display 1')
        instrument_id = 1
    os.system('adb shell /system/bin/screencap -p -d %s  /sdcard/yibiaoscreenshot.png'%(instrument_id))


#根据当前车型截图科技岛
def GetCarType_ScreencapLand():
    try:
        TechIsland_id = get_techIsland_display_id()
        print('科技岛应用所在displayid为%s'%(TechIsland_id) )
    except Exception as e:
        #get_cluster_display_id的方法get不到科技岛的display ID 故将ID写死为3
        print('自动获取仪表display id失败，将使用display 3')
        TechIsland_id = 3
    os.system('adb shell screencap -p -d %s  /sdcard/TechIsland.png'%(TechIsland_id))


#判断当前车型
def GetCarType():
    rom = subprocess.check_output(f'adb shell "getprop | grep xiaopeng.software"', shell=True, universal_newlines=True)
    if rom[34:37] =="E28":
        CarMode = rom[34:37]+'A'
    else:
        CarMode = rom[34:37]
    if rom[32:34] == 'EU':
        CarType = 'V'
    elif rom[32:34] == 'IA':
        CarType = 'R'
    else:
        CarType = ''
    Car = CarMode+CarType
    return Car

# 将只有两种状态的信号封装起来
def TwoStates(button_key, insvdt):
    i = 1 + button_key.clicks % 2
    if i == 1:
        vdts({
            insvdt: 1,
            })
        QNXcmd(insvdt,1)
    else:
        vdts({
            insvdt: 0,
            })
        QNXcmd(insvdt,0)
    button_key.clicks += 1

    # 将只有三种状态的指示灯封装起来
def ThreeStates(button_key, insvdt):
    i = 1 + button_key.clicks % 3
    if i == 3:
        vdts({
            insvdt: 0,
        })
        QNXcmd(insvdt,0)
    else:
        vdts({
            insvdt: i,
        })
        QNXcmd(insvdt,str(i))
    button_key.clicks += 1

    # 将只有四种状态的指示灯封装起来
def FourStates(button_key, insvdt):
    i = 1 + button_key.clicks % 4
    if i == 4:
        vdts({
            insvdt: 0,
        })
        QNXcmd(insvdt,0)
    else:
        vdts({
        insvdt: i,
        })
        QNXcmd(insvdt,str(i))
    button_key.clicks += 1


    #将输入框封装，如果输入为空则不进行发送信号
def InputBox(vdt,Value):
    if Value == '':
        pass
    else:
        vdts({
            vdt: Value,
        })

#判断输入的路径是否正确

# OS5.3.0做了统一APK，故无需再做车型判断

def decideway(ApkName,Value):
    if ApkName in Value:
        pass
    else:
        return False
    # carname=GetCarType()
    # if carname == 'F30R':
    #     carname = 'F30V'
    # strway = str(Value).lower()
    # carname =carname.lower()
    # if re.search(carname, strway):
    #     return True
    # else:
    #     print(carname, strway)
    #     return False



#判断rom与apk类型
#判断当前的包是专1或者专5
def deciderom(Value):
    if 'D01' in str(GetCarType()):
        #如果为非DD车型，直接跳过此判断
        print('当前为DD车型')
        return True
    else:

        apktype = Value[-8:]
        if '5' in apktype:
            #包5
            print(apktype)
            apktype = "True"
        elif 'debug' in Value:
            #非包5
            print(apktype)
            apktype = "False"
        else:
            #非包5
            print(apktype)
            apktype = "False"

        rom = subprocess.check_output(f'adb shell "getprop | grep xiaopeng.software"', shell=True, universal_newlines=True)
        # romtype = rom[-5:-2]
        if 'DEV' in rom:
            #DEV的rom，不需要签名包

            romtype = "False"
        else:
            #非DEV，需要签名包
            romtype = "True"
        print(romtype)
        if apktype != romtype:
            #不匹配，需要返回警告
            print('APK Mismatch\n版本不匹配')
            return False
        elif apktype == romtype:
            print('版本匹配正确')
            return True

def remount():
    try:
        ins = subprocess.check_output(f'adb remount', shell=True,
                                      universal_newlines=True)
        if 'succeeded' not in ins or 'reboot' in ins:
            return False
    except Exception as e:
        return False

#判断当前仪表在哪位display id
def get_all_display_ids() -> dict:
    display_ids = {}
    tmp_id = -1
    display_name = ''
    output = subprocess.check_output(f'adb shell dumpsys display', shell=True, universal_newlines=True)
    # output = run_command_in_adb_shell("dumpsys display")
    output = output if output is not None else ''
    for line in output.split('\n'):
        output = re.search(r"Display ([0-9]{1,10})", line)
        display_type = re.search(r"type ([A-Za-z0-9]+)", line)
        if output:
            tmp_id = output.group(1)
            display_name = ''
        if tmp_id != -1 and display_type:
            display_name = display_type.group(1)
            display_ids[display_name] = tmp_id
            tmp_id = -1
            continue
        if "mPrimaryDisplayDevice" in line and 'virtual' in line.lower():
            try:
                display_ids.pop(display_name)
            except KeyError:
                pass
    return display_ids

def get_cluster_display_id(display_name='ICM'):
# def get_cluster_display_id():
#     icm_id = subprocess.check_output(f'adb shell "getprop | grep display.id.icm"', shell=True, universal_newlines=True)
    display_ids = get_all_display_ids()
    return display_ids.get(display_name, 0)
    # return icm_id[-3:-2]


#科技岛投屏
def get_techIsland_display_id(display_name='10'):
    display_ids = get_all_display_ids()
    return display_ids.get(display_name, 0)


"""
新立项的车型以及3屏及以上的车型，偶现display类型获取失败
目前的解决方法是遍历所有的display id以及屏幕分辨率并打印，并让用户手动选择
"""
def get_display_resolutions():
    output = subprocess.check_output(
            ["adb", "shell", "dumpsys", "display"],text=True,stderr=subprocess.STDOUT
        )
    pattern = re.compile(
        r'Display (\d+):.*?width=(\d+).*?height=(\d+)',
        re.DOTALL
    )
    matches = pattern.findall(output)
    return {id: f"{w}x{h}" for id, w, h in matches}

#结果匹配输出
def print_all_display():
    resolutions = get_display_resolutions()
    display_info = [f"Display {display_id}: {res}" for display_id, res in resolutions.items()]
    combined_output = "\n".join(display_info)
    return combined_output



#推工厂APK参数
def PushFactoryApk(cartype):
    os.system('adb wait-for-device')
    os.system('adb root')
    subprocess.check_output('adb remount',shell=True, universal_newlines=True)
    os.system('adb shell mkdir system/priv-app/XpFactoryTest')
    os.system('adb shell mkdir system/priv-app/XpFactoryTest/lib')
    os.system('adb shell mkdir system/priv-app/XpFactoryTest/lib/arm64')
    os.system('adb shell rm -rf /system/priv-app/XpFactoryTest/oat/')
    try:
        subprocess.check_output(f'adb push .\FactoryApk\%s\XpFactoryTest.apk /system/priv-app/XpFactoryTest/'%(cartype),
                                shell=True,universal_newlines=True)
        os.system(r'adb push .\FactoryApk\%s\lib\arm64\. /system/priv-app/XpFactoryTest/lib/arm64/'%(cartype))
        os.system(r'adb push .\FactoryApk\%s\pre_env.ini /sdcard/'%(cartype))
        os.system('adb shell rm -rf /data/app/com.xiaopeng.factory*')
        os.system('adb shell am force-stop com.xiaopeng.factory')
        os.system('adb shell sync')
    except subprocess.CalledProcessError:
        return False

#判断当前有没有仪表屏
def JudgeScreen():
    screen = subprocess.check_output(f'adb shell getprop persist.sys.xiaopeng.INSTRUMENT_SCREEN', shell=True, universal_newlines=True)
    if '1' in str(screen):
        return True
    else:
        return False

def JudegICM(APK):
    screen = subprocess.check_output(f'adb shell getprop persist.sys.xiaopeng.INSTRUMENT_SCREEN', shell=True,
                                     universal_newlines=True)
    #如果为有仪表车型，判断推的APK里是否包含“F01”字样
    if '1' in str(screen):
        if 'F01' not in str(APK):
            #没有F01字样，则为正确推了包
            return True
        else:
            return False
    else:
    #没有仪表车型，需要判断APK是否带有“F01”字样，否则为推错包
        if 'F01' not in str(APK):
            return False
        else:
            return True

#判断当前有没有科技岛
def JudgeLand():
    try:
        subprocess.check_output(f'adb shell "dumpsys package com.xiaopeng.techisland | grep versionName"', shell=True,
                                      universal_newlines=True)
        return True
    except Exception as e:
        return False

#判断当前是否为MAX配置车型
def JudgeMaxCar():
    Car = subprocess.check_output(f'adb shell getprop persist.sys.xiaopeng.ngpType', shell=True, universal_newlines=True)
    if '2' in str(Car):
        return True
    else:
        return False


def DidiSigned(apk):
    if 'D01' not in str(GetCarType()):
        #如果为非DD车型，直接跳过此判断
        print('当前为非DD车型')
        return True
    else:
        print('当前为DD车型')
        rom = subprocess.check_output(f'adb shell "getprop | grep xiaopeng.software"', shell=True,
                                      universal_newlines=True)
        if 'DEV' in rom:
            # DEV的rom，不需要签名包
            if 'signed' in str(apk):
                #如果APK包含签名，则返回错误
                return False
            else:
                return True
        else:
            print('当前不为DEV',apk)
            # 非DEV，需要签名包
            if 'signed' in str(apk):
                #如果APK没包含签名，则返回错误
                return True
            else:
                return False


toolVersion='11_03_25'


"""

打#号的内容为未完成的功能或者修复
-仪表区域
修复大屏充电供电量异常的问题
新增大屏预约充电开始结束时间的设置
修复切换电池类型时，没有kill对应的大屏应用的问题
新增DD车型模拟台架上电
新增一键恢复出厂设置功能(如遇设置不该设置的动西，或者推了异常的包，可用此功能恢复)
自动更新功能，安装CarPlay，AndroidAuto模拟应用功能下线


#其他模块
#新增车控相关业务的模拟
#多屏幕设备投屏时如遇工具无法正常识别投屏类型时，将所有屏幕分辨率以及ID例如并让用户手动进行选择

-仪表区域
修复偶尔仪表无法投屏的问题
修复极速充电标题不显示的问题
新增电池磷酸铁锂，三元锂类型的切换
新增雪地，湿地驾驶模式的设置
新版本E29已恢复大屏仪表区，加回E29车型推包时，对有无仪表屏APK推包的判断




-仪表区域
将毫米波雷达与传感器故障功能分离，并新增传感器故障第二行文言的显示
修复科技岛推包时出现的有无仪表屏的误判断
更新scrapy至V3.1
新增仪表充电时长的模拟
新增能源模式的模拟
修复E29无仪表应用车型，对科技岛信息无法读取的问题
新增推仪表APK时对DD车型的签名判断



-仪表区域
修复仪表区增程信息页燃油里程与综合里程发送异常的问题
新增对MAX车型LCC,NGP,APA指示灯的支持
修复科技岛进程无法kill的问题
新增推包时对APK与有无仪表车型的判断，防止推错包
新增kill systemUI的功能
-其他模块
新增一键恢复大屏为正式环境的功能
优化推工厂APK时没有disable的判断
修改推工厂APK时对设备8155与8295的判断逻辑


去掉每次打开工具时初始化git的步骤
新增无仪表屏车型大屏仪表区车况卡的显示
AI小P页修改为其他模块页，新增KILL爱卡宾应用
新增8155车型切换到泊车态时，大屏也跟随切换到泊车态
修复语音唤醒后无法发送指令的问题
新增切换驾驶模式时大屏也随之切换对应驾驶模式，以修复进车手时大屏仪表地图昼夜不一致的问题
优化所有信息框打印信息逻辑


22_11修改点
1.修复科技岛进程无法kill
2.新增push不同APK时的误操作提醒
3.新增切换纯电，增程模式时的提醒,修复切换时没有主动kill仪表进程的问题
4.抓取日志时会根据有无仪表屏以及科技岛车型来进行对应截图
5.修复nedc模式无法发送续航里程值的问题

20_11修改点
1.修复自动更新后出现解压失败的问题
2.修复发动机水温与指示灯混淆的问题
3.新增一键切换纯电\增程功能
4.修复推工厂APK时没有push ini文件的问题
5.新增SVS发动机故障指示灯按钮
"""
