import os

from lib import *


# 这里执行关闭安卓侧心跳，进入QNX系统的操作
def Enter_QNX_cli():
    text = "pidin | grep vmm"
    bytes_cli = text.encode()
    ser.write(bytes_cli + b'\n')
    # 等待接收返回信息
    time.sleep(2)  # 等待一秒，以便设备有时间响应
    # 读取返回信息
    lines = ser.read_all().decode().split('\n')  # 读取并打印返回信息
    print(lines)
    if lines:
        android=lines[1]
    android_pid = android[2:8]
    print('关闭心跳，pid为：'+android_pid)
    # QNXcmd('slay -9 %s'%(android_pid),'')

    cmds = 'slay -9 '+ str(android_pid)
    bytes_cli = cmds.encode()  # 默认使用UTF-8编码
    ser.write(bytes_cli + b'\n')  # 发送字节数据
    time.sleep(1)
    rmpic = "rm -r /cli/pic"
    bytes_cli = rmpic.encode()
    ser.write(bytes_cli + b'\n')
    return android_pid

def Screenshot_cli():
    mkdir = "mkdir /cli/pic"
    mkdir_cli = mkdir.encode()
    ser.write(mkdir_cli + b'\n')
    picture = "screenshot -display=1 -file=/cli/pic/%s.png"%(time.strftime("%Y-%m-%d_%H-%M-%S"))
    picture_cli = picture.encode()
    ser.write(picture_cli + b'\n')
    return True

#拉取QNX的截图
def PullQnxPic_cli():
    os.system('adb root')
    os.system('adb pull /qnx/cli/pic/.  %s\\' % (pic_path))




# 关闭串口
# try :
#     ser.close()
#     print('串口已关闭')
# except Exception as e:
#     print('当前没有连接到QNX台架，故没有可关闭的串口')