from lib import *

# 续航模式
button_clicksRangeMode = ButtonClicks()
def RangeMode():
    i = 1 + button_clicksRangeMode.clicks % 2
    if i == 1:
        QNXcmd('HOST_RANDIS_MODE',2)
    else:
        QNXcmd('HOST_RANDIS_MODE',3)
    button_clicksRangeMode.clicks += 1


    #READY
button_clicksReady = ButtonClicks()
def RangeReady():
    TwoStates(button_clicksReady,'HOST_VCU_EVSYS_READYST')


    #挡位
def Gear_P():
    QNXcmd('HOST_VCU_CURRENT_GEARLEV', 4)

def Gear_R():
    QNXcmd('HOST_VCU_CURRENT_GEARLEV', 3)

def Gear_N():
    QNXcmd('HOST_VCU_CURRENT_GEARLEV', 2)

def Gear_D():
    QNXcmd('HOST_VCU_CURRENT_GEARLEV', 1)

    #续航数值
def DSTBAT(key):
    if key == '':
        pass
    else:
        i = 10 * float(key)
        QNXcmd('HOST_VCU_DSTBAT_DISP_CLTC', i)
        QNXcmd('HOST_VCU_DSTBAT_DISP_WLTP', i)

    #电池百分比
def BmsSoc(key):
    if key == '':
        pass
    else:
        QNXcmd('HOST_VCU_BMS_SOCDISP', key)


    #车外温度
def Env(key):
    if key == '':
        pass
    else:
        QNXcmd('HOST_ENV_OUTSIDE_TEMPERATURE', key)


    #驾驶模式
button_clicksDriveMode = ButtonClicks()
def DriveMode_cli(Value):
    orders = {'标准':0,'节能':1,'运动':2,'舒适':3,'自适应':4,'脱困':5,'弹射':6,'X—PEDAL':7,'极客':8,'车手':9}
    if Value == '选择驾驶模式':
        pass
    else:
        QNXcmd('HOST_VCU_DRIVE_MODE',orders.get(Value))

    #时间
def SystemTime(hour,min):
    year = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")
    date = 'date '+month+day+hour+min+year+'.22 set'
    os.system("adb shell %s" % date)