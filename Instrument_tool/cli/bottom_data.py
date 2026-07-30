from lib import *

    #车外温度

def Env(key):
    if key == '':
        pass
    else:
        vdts({
        'HOST_ENV_OUTSIDE_TEMPERATURE': key,
         })



    #系统时间
def SystemTime(hour,min):
    os.system('adb root')
    year = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")
    date = 'date '+month+day+hour+min+year+'.22 set'
    os.system("adb shell %s" % date)

    # 剩余里程
def DSTBAT(key):

    if key == '':
        pass
    else:
        i = 10 * float(key)
        vdts({
        'HOST_VCU_DSTBAT_DISP_CLTC': i,
        'HOST_VCU_DSTBAT_DISP_WLTP': i,
        'HOST_VCU_DSTBAT_DISP_NEDC':i,
        'HOST_VCU_DSTBAT_DISP ':key,
        'HOST_VCU_DSTBAT_DISP_DYNAMIC':i,
        'VCU_DSTBAT_DISP_CLTC_FLOAT':key,
        'VCU_DSTBAT_DISP_WLTP_FLOAT':key,
        'VCU_DSTBAT_DISP':key,
        'VCU_DSTBAT_DISP_DYNAMIC':key,
         })



    # 剩余电量
def BmsSoc(key):
    if key == '':
        pass
    else:
        vdts({
        'HOST_VCU_BMS_SOCDISP': key,
        'VCU_BMS_SOCDISP': key,
         })


    #驾驶模式

def DriveMode_cli(Value):
    orders = {'标准':0,'节能':1,'运动':2,'舒适':3,'自适应':4,'脱困':5,'弹射':6,'X—PEDAL':7,
              '极客':8,'车手':9,'个性化':10,'雪地':11,'湿地':12}

    main_rders = {'标准':10,'节能':1,'运动':2,'舒适':7,'自适应':4,'脱困':16,'弹射':17,
                  'X—PEDAL':7,'极客':15,'车手':13,'个性化':18,'雪地':19,'湿地':20}
    if Value == '选择驾驶模式':
        pass
    else:
        os.system(f'adb shell vdt rp HOST_VCU_DRIVE_MODE %s'% (orders.get(Value)))
        os.system(f'adb shell vdt rp VCU_DRIVE_MODE %s'% (main_rders.get(Value)))



    #续航模式

def MileageMode_cli(Value):
    orders = {'NEDC':0,'WLTP':1,'CLTC':2,'Dynamics':3}
    if Value == '续航模式':
        pass
    else:
        os.system(f'adb shell vdt rp VCU_RANDIS_MODE %s'% (orders.get(Value)))
        i = orders.get(Value) + 1
        os.system(f'adb shell vdt rp HOST_RANDIS_MODE %s' % (i))



#ready指示灯
button_clicksReady = ButtonClicks()
def RangeReady():
    TwoStates(button_clicksReady,'HOST_VCU_EVSYS_READYST')


    #挡位
def Gear_P():
    vdts({
        'HOST_VCU_CURRENT_GEARLEV': 4,
        'VCU_CURRENT_GEARLEV':4,
    })

def Gear_R():
    vdts({
        'HOST_VCU_CURRENT_GEARLEV': 3,
        'VCU_CURRENT_GEARLEV': 3,
    })

def Gear_N():
    vdts({
        'HOST_VCU_CURRENT_GEARLEV': 2,
        'VCU_CURRENT_GEARLEV': 2,
    })

def Gear_D():
    vdts({
        'HOST_VCU_CURRENT_GEARLEV': 1,
        'VCU_CURRENT_GEARLEV': 1,
    })