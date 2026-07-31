from lib import *

#方控相关

def Left_left_cli():   #左侧左
    os.system('adb shell input keyevent 1002')
def Left_right_cli():  #左侧右
    os.system('adb shell input keyevent 1003')
def Left_long_cli():   #左长按
    os.system('adb shell input keyevent 1024')
    command = 'adb shell vdt rp HOST_ICM_SYNC_SIGNAL "{\"SyncMode\":\"LeftSwitchMode\",\"msgId\":\"\",\"SyncProgress\":1}"'
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
def Left_short_cli():  #左短按
    os.system('adb shell input keyevent 1004')
    # os.system('adb shell vdt rp HOST_ICM_SYNC_SIGNAL "{\"SyncMode\":\"LeftSwitchMode\",\"msgId\":\"\",\"SyncProgress\":0}"')
def Left_up_cli(): #左上
    os.system('adb shell input keyevent 1081')
def Left_down_cli():   #左下
    os.system('adb shell input keyevent 1082')


def Right_right_cli(): #右侧右
    os.system('adb shell input keyevent 1014')
def Right_left_cli():  #右侧左
    os.system('adb shell input keyevent 1013')
def Right_long_cli():  #右长按
    os.system('adb shell input keyevent 1035')
def Right_short_cli(): #右短按
    os.system('adb shell input keyevent 1015')
def Right_up_cli():    #右上
    os.system('adb shell input keyevent 1083')
def Right_down_cli():  #右下
    os.system('adb shell input keyevent 1084')

def Return_cli():  #返回
    os.system('adb shell input keyevent 1036')
def Custom_cli():  #自定义
    os.system('adb shell input keyevent 1006')
def Voice_cli():   #语音
    os.system('adb shell input keyevent 1005')
def Mute_cli():    #静音
    os.system('adb shell input keyevent 164')


#雨刮灵敏度
button_RaindDetec = ButtonClicks()
def RainDetec_cli():
    i = 1 + button_RaindDetec.clicks % 5
    if i == 5:
        vdts({
            'HOST_ICM_RAIN_DETEC_SENCFG': 1,
        })
    else:

        vdts({
        'HOST_ICM_RAIN_DETEC_SENCFG': i,
        })
    button_RaindDetec.clicks += 1

