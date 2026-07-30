from lib import *

#胎压相关
def LF_Tire_cli(LF):
    if LF =='':
        pass
    else:
        vdts({
        'TPMS_PRFL':float(LF)*100,
    })

def RF_Tire_cli(RF):
    if RF == '':
        pass
    else:
        vdts({
        'TPMS_PRFR':float(RF)*100,
    })

def LR_Tire_cli(LR):
    if LR == '':
        pass
    else:
        vdts({
        'TPMS_PRRL':float(LR)*100,
    })

def RR_Tire_cli(RR):
    if RR == '':
        pass
    else:
        vdts({
        'TPMS_PRRR':float(RR)*100,
    })

    #轮胎胎压状态
button_clicksLF_State = ButtonClicks()      #左前轮胎状态计数器
button_clicksRF_State = ButtonClicks()      #右前轮胎状态计数器
button_clicksLR_State = ButtonClicks()      #左后轮胎状态计数器
button_clicksRR_State = ButtonClicks()      #右后轮胎状态计数器
def LF_State_cli():
    LFCard = 1 + button_clicksLF_State.clicks % 4
    RFCard = button_clicksRF_State.clicks % 4
    LRCard = button_clicksLR_State.clicks % 4
    RRCard = button_clicksRR_State.clicks % 4
    if LFCard >= 3 :
        LFCard +=1
    if RFCard >= 3:
        RFCard +=1
    if LRCard >= 3:
        LRCard +=1
    if RRCard >= 3:
        RRCard +=1
    vdts({
        ' TPMS_WARNING_TIRE_PRESSURE_ALL':[LFCard,RFCard,LRCard,RRCard],
        ' TPMS_PRWARN_ALL': [LFCard, RFCard, LRCard, RRCard],
        })


    button_clicksLF_State.clicks += 1



def RF_State_cli():
    LFCard = button_clicksLF_State.clicks % 4
    RFCard = 1 +button_clicksRF_State.clicks % 4
    LRCard = button_clicksLR_State.clicks % 4
    RRCard = button_clicksRR_State.clicks % 4
    if LFCard >= 3:
        LFCard +=1
    if RFCard >= 3:
        RFCard +=1
    if LRCard >= 3:
        LRCard +=1
    if RRCard >= 3:
        RRCard +=1
    vdts({
        ' TPMS_WARNING_TIRE_PRESSURE_ALL':[LFCard,RFCard,LRCard,RRCard],
        ' TPMS_PRWARN_ALL': [LFCard, RFCard, LRCard, RRCard],
        })
    button_clicksRF_State.clicks += 1



def LR_State_cli():
    LFCard = button_clicksLF_State.clicks % 4
    RFCard = button_clicksRF_State.clicks % 4
    LRCard = 1 +button_clicksLR_State.clicks % 4
    RRCard = button_clicksRR_State.clicks % 4
    if LFCard >= 3:
        LFCard +=1
    if RFCard >= 3:
        RFCard +=1
    if LRCard >= 3:
        LRCard +=1
    if RRCard >= 3:
        RRCard +=1
    vdts({
        ' TPMS_WARNING_TIRE_PRESSURE_ALL':[LFCard,RFCard,LRCard,RRCard],
        ' TPMS_PRWARN_ALL': [LFCard, RFCard, LRCard, RRCard],
        })
    button_clicksLR_State.clicks += 1



def RR_State_cli():
    LFCard = button_clicksLF_State.clicks % 4
    RFCard = button_clicksRF_State.clicks % 4
    LRCard = button_clicksLR_State.clicks % 4
    RRCard = 1 +button_clicksRR_State.clicks % 4
    if LFCard >= 3:
        LFCard +=1
    if RFCard >= 3:
        RFCard +=1
    if LRCard >= 3:
        LRCard +=1
    if RRCard >= 3:
        RRCard +=1
    vdts({
        ' TPMS_WARNING_TIRE_PRESSURE_ALL':[LFCard,RFCard,LRCard,RRCard],
        ' TPMS_PRWARN_ALL': [LFCard, RFCard, LRCard, RRCard],
        })
    button_clicksRR_State.clicks += 1


    #轮胎胎温度状态
button_clicksLF_Temp = ButtonClicks()
button_clicksRF_Temp = ButtonClicks()
button_clicksLR_Temp = ButtonClicks()
button_clicksRR_Temp = ButtonClicks()
def LF_Temp_cli():
    LFCard = 1 + button_clicksLF_Temp.clicks % 2
    RFCard = button_clicksRF_Temp.clicks % 2
    LRCard = button_clicksLR_Temp.clicks % 2
    RRCard = button_clicksRR_Temp.clicks % 2
    vdts({
        ' TPMS_WARNING_TIRE_TEMPERATURE_ALL ':[LFCard,RFCard,LRCard,RRCard],
        ' TPMS_TEMPWARN_ALL ': [LFCard, RFCard, LRCard, RRCard],
        })
    button_clicksLF_Temp.clicks += 1

def RF_Temp_cli():
    LFCard = button_clicksLF_Temp.clicks % 2
    RFCard = 1 + button_clicksRF_Temp.clicks % 2
    LRCard = button_clicksLR_Temp.clicks % 2
    RRCard = button_clicksRR_Temp.clicks % 2
    vdts({
        ' TPMS_WARNING_TIRE_TEMPERATURE_ALL ':[LFCard,RFCard,LRCard,RRCard],
        ' TPMS_TEMPWARN_ALL ': [LFCard, RFCard, LRCard, RRCard],
        })
    button_clicksRF_Temp.clicks += 1

def LR_Temp_cli():
    LFCard = button_clicksLF_Temp.clicks % 2
    RFCard = button_clicksRF_Temp.clicks % 2
    LRCard = 1 + button_clicksLR_Temp.clicks % 2
    RRCard = button_clicksRR_Temp.clicks % 2
    vdts({
        ' TPMS_WARNING_TIRE_TEMPERATURE_ALL ':[LFCard,RFCard,LRCard,RRCard],
        ' TPMS_TEMPWARN_ALL ': [LFCard, RFCard, LRCard, RRCard],
        })
    button_clicksLR_Temp.clicks += 1

def RR_Temp_cli():
    LFCard = button_clicksLF_Temp.clicks % 2
    RFCard = button_clicksRF_Temp.clicks % 2
    LRCard = button_clicksLR_Temp.clicks % 2
    RRCard = 1 + button_clicksRR_Temp.clicks % 2
    vdts({
        ' TPMS_WARNING_TIRE_TEMPERATURE_ALL ':[LFCard,RFCard,LRCard,RRCard],
        ' TPMS_TEMPWARN_ALL ': [LFCard, RFCard, LRCard, RRCard],
        })
    button_clicksRR_Temp.clicks += 1


    #轮胎传感器状态
button_clicksLF_Sensor = ButtonClicks()
button_clicksRF_Sensor = ButtonClicks()
button_clicksLR_Sensor = ButtonClicks()
button_clicksRR_Sensor = ButtonClicks()
def LF_Sensor_cli():
    LFCard = 1 + button_clicksLF_Sensor.clicks % 2
    RFCard = button_clicksRF_Sensor.clicks % 2
    LRCard = button_clicksLR_Sensor.clicks % 2
    RRCard = button_clicksRR_Sensor.clicks % 2
    vdts({
        ' TPMS_ALL_SENSOR_ST ':[LFCard,RFCard,LRCard,RRCard],
        })
    button_clicksLF_Temp.clicks += 1

def RF_Sensor_cli():
    LFCard = button_clicksLF_Sensor.clicks % 2
    RFCard = 1 + button_clicksRF_Sensor.clicks % 2
    LRCard = button_clicksLR_Sensor.clicks % 2
    RRCard = button_clicksRR_Sensor.clicks % 2
    vdts({
        ' TPMS_ALL_SENSOR_ST ':[LFCard,RFCard,LRCard,RRCard],
        })
    button_clicksRF_Temp.clicks += 1

def LR_Sensor_cli():
    LFCard = button_clicksLF_Sensor.clicks % 2
    RFCard = button_clicksRF_Sensor.clicks % 2
    LRCard = 1 + button_clicksLR_Sensor.clicks % 2
    RRCard = button_clicksRR_Sensor.clicks % 2
    vdts({
        ' TPMS_ALL_SENSOR_ST ':[LFCard,RFCard,LRCard,RRCard],
        })
    button_clicksLR_State.clicks += 1

def RR_Sensor_cli():
    LFCard = button_clicksLF_Sensor.clicks % 2
    RFCard = button_clicksRF_Sensor.clicks % 2
    LRCard = button_clicksLR_Sensor.clicks % 2
    RRCard = 1 + button_clicksRR_Sensor.clicks % 2
    vdts({
        ' TPMS_ALL_SENSOR_ST ':[LFCard,RFCard,LRCard,RRCard],
        })
    button_clicksLR_Temp.clicks += 1

    #悬架维修模式
button_SuspensionMalfunction = ButtonClicks()
def SuspensionMalfunction_cli():
    TwoStates(button_SuspensionMalfunction, 'BCM_ENGINEERINGMODE')

    #前雨刮维修模式
button_WIPERSERVICE = ButtonClicks()
def WIPERSERVICE_cli():
    TwoStates(button_WIPERSERVICE, 'BCM_WIPERSERVICE_SW')

    #后雨刮维修模式
button_RWIPERSERVICE = ButtonClicks()
def RWIPERSERVICE_cli():
    TwoStates(button_RWIPERSERVICE, 'BCM_RWIPERSERVICE_SW')

    #拖车线束连接
button_HARNCONN = ButtonClicks()
def HARNCONN_cli():
    TwoStates(button_HARNCONN, 'TTM_LAMP_CONNECT_ST')

    #拖车钩故障
button_THFault = ButtonClicks()
def THFault_cli():
    TwoStates(button_THFault, 'TTM_SYS_ERR')

    # 拖车钩初始化
button_THInit  = ButtonClicks()
def THInit_cli():
    TwoStates(button_THInit, 'TTM_DENORMALIZE_ST')

    # 拖车钩状态
button_THStatus  = ButtonClicks()
def THStatus_cli():
    TwoStates(button_THStatus, 'TTM_SW')

    # 远程拖钩开关
button_RTHSwitch  = ButtonClicks()
def RTHSwitch_cli():
    FourStates(button_RTHSwitch, 'TBOX_CDU_TTMSW_REQUEST')

    # 远程拖钩重置
button_RTHReset  = ButtonClicks()
def RTHReset_cli():
    FourStates(button_RTHReset, 'TBOX_CDU_TTM_RESET_REQUEST')