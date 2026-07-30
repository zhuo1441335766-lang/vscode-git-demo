import os

from lib import *

    #车况卡片相关

    #左前门
button_clicksLFdoor = ButtonClicks()
button_clicksRFdoor = ButtonClicks()
button_clicksLRdoor = ButtonClicks()
button_clicksRRdoor = ButtonClicks()
def Cars_LFdoor_cli():
    #判断当前是否为无仪表屏车型，如果是无仪表车型，则需要发送车门异常文言，否则不出现卡片
    if JudgeScreen() == False:
        os.system('adb shell vdt rp HOST_EALARM_ID 51')
    LF =1+ button_clicksLFdoor.clicks % 2
    RF = button_clicksRFdoor.clicks % 2
    LR = button_clicksLRdoor.clicks % 2
    RR = button_clicksRRdoor.clicks % 2
    if LF == 2:
        LF = 0
        os.system('adb shell vdt rp HOST_EALARM_ID 999')
    vdts({
        'HOST_BCM_DOOR':[LF,RF,LR,RR],
        'BCM_DOOR': [LF, RF, LR, RR]
        })

    button_clicksLFdoor.clicks += 1


    #右前门

def Cars_RFdoor_cli():
    #判断当前是否为无仪表屏车型，如果是无仪表车型，则需要发送车门异常文言，否则不出现卡片
    if JudgeScreen() == False:
        os.system('adb shell vdt rp HOST_EALARM_ID 52')
    LF = button_clicksLFdoor.clicks % 2
    RF = 1+button_clicksRFdoor.clicks % 2
    LR = button_clicksLRdoor.clicks % 2
    RR = button_clicksRRdoor.clicks % 2
    if RF == 2:
        RF = 0
        os.system('adb shell vdt rp HOST_EALARM_ID 999')
    vdts({
        'HOST_BCM_DOOR': [LF, RF, LR, RR],
        'BCM_DOOR': [LF, RF, LR, RR]
    })
    button_clicksRFdoor.clicks += 1


    #左后门

def Cars_LRdoor_cli():
    #判断当前是否为无仪表屏车型，如果是无仪表车型，则需要发送车门异常文言，否则不出现卡片
    if JudgeScreen() == False:
        os.system('adb shell vdt rp HOST_EALARM_ID 53')
    LF = button_clicksLFdoor.clicks % 2
    RF = button_clicksRFdoor.clicks % 2
    LR = 1+button_clicksLRdoor.clicks % 2
    RR = button_clicksRRdoor.clicks % 2
    if LR == 2:
        LR = 0
        os.system('adb shell vdt rp HOST_EALARM_ID 999')
    vdts({
        'HOST_BCM_DOOR': [LF, RF, LR, RR],
        'BCM_DOOR': [LF, RF, LR, RR]
    })
    button_clicksLRdoor.clicks += 1

    # 右后门

def Cars_RRdoor_cli():
    #判断当前是否为无仪表屏车型，如果是无仪表车型，则需要发送车门异常文言，否则不出现卡片
    if JudgeScreen() == False:
        os.system('adb shell vdt rp HOST_EALARM_ID 54')
    LF = button_clicksLFdoor.clicks % 2
    RF = button_clicksRFdoor.clicks % 2
    LR = button_clicksLRdoor.clicks % 2
    RR =1+ button_clicksRRdoor.clicks % 2
    if RR == 2:
        RR = 0
        os.system('adb shell vdt rp HOST_EALARM_ID 999')
    vdts({
        'HOST_BCM_DOOR': [LF, RF, LR, RR],
        'BCM_DOOR': [LF, RF, LR, RR]
    })
    button_clicksRRdoor.clicks += 1


    #后备箱
button_clicksTrunk = ButtonClicks()
def Cars_Trunk_cli():
    TwoStates(button_clicksTrunk,'HOST_BCM_TRUNKAJAR')

    #前舱盖
button_clicksBonnet = ButtonClicks()
def Cars_Bonnet_cli():
    TwoStates(button_clicksBonnet,'HOST_BCM_BONNET')

    #左充电盖
button_clicksLChargCover = ButtonClicks()
def LCharg_Cover_cli():
    # TwoStates(button_clicksLChargCover,'HOST_BCM_L_CHARGER_PORT')
    i = 1 + button_clicksLChargCover.clicks % 3
    if i == 1:
        vdts({
            'HOST_BCM_L_CHARGER_PORT': 1,
            })
    elif i == 2:
        vdts({
            'HOST_BCM_CHARGEPORT_LEFT_FAULT': 1,
            })
    else:
        vdts({
            'HOST_BCM_L_CHARGER_PORT': 0,
            'HOST_BCM_CHARGEPORT_LEFT_FAULT': 0,

        })
    button_clicksLChargCover.clicks += 1

    #右充电盖
button_clicksRChargCover = ButtonClicks()
def RCharg_Cover_cli():
    i = 1 + button_clicksRChargCover.clicks % 3
    if i == 1:
        vdts({
            'HOST_BCM_R_CHARGER_PORT': 1,
            })
    elif i == 2:
        vdts({
            'HOST_BCM_ECHARGEPORT_RIGHT_FAULT': 1,
            })
    else:
        vdts({
            'HOST_BCM_R_CHARGER_PORT': 0,
            'HOST_BCM_ECHARGEPORT_RIGHT_FAULT': 0,

        })
    button_clicksRChargCover.clicks += 1


    #胎压相关

def LF_Tire_cli(LF):
    if LF =='':
        pass
    else:
        vdts({
        'HOST_ETPMS_PRESSURE_LF':float(LF),
    })

def RF_Tire_cli(RF):
    if RF == '':
        pass
    else:
        vdts({
        'HOST_ETPMS_PRESSURE_RF':float(RF),
    })

def LR_Tire_cli(LR):
    if LR == '':
        pass
    else:
        vdts({
        'HOST_ETPMS_PRESSURE_LB':float(LR),
    })

def RR_Tire_cli(RR):
    if RR == '':
        pass
    else:
        vdts({
        'HOST_ETPMS_PRESSURE_RB':float(RR),
    })


    #胎温相关

def LF_Tyre_cli(LF):
    if LF =='':
        vdts({
            'HOST_TIRE_TEMPWARN_LF':0,
        })

    else:
        vdts({
        'HOST_TIRE_TEMPWARN_LF':1,
        'HOST_ETPMS_TEMPERATURE_LF':[0,LF],
    })

def RF_Tyre_cli(RF):
    if RF == '':
        vdts({
            'HOST_TIRE_TEMPWARN_RF': 0,
        })

    else:
        vdts({
        'HOST_TIRE_TEMPWARN_RF':1,
        'HOST_ETPMS_TEMPERATURE_RF':[0,RF],
    })

def LR_Tyre_cli(LR):
    if LR == '':
        vdts({
            'HOST_TIRE_TEMPWARN_LB': 0,
        })

    else:
        vdts({
        'HOST_TIRE_TEMPWARN_LB':1,
        'HOST_ETPMS_TEMPERATURE_LB':[0,LR],
    })

def RR_Tyre_cli(RR):
    if RR == '':
        vdts({
            'HOST_TIRE_TEMPWARN_RB': 0,
        })
    else:
        vdts({
        'HOST_TIRE_TEMPWARN_RB':1,
        'HOST_ETPMS_TEMPERATURE_RB':[0,RR],
    })





    #建议补充的胎压值
def SuggestedPressure_cli(FValue,RValue):
    if FValue == '':
        FValue = 0
    if RValue == '':
        RValue = 0
    vdts({
        'HOST_ETPMS_PRESSURE_STANDARD ':[FValue,RValue],
        'HOST_EALARM_ID':544
    })

    #轮胎状态
button_clicksLF_State = ButtonClicks()      #左前轮胎状态计数器
button_clicksRF_State = ButtonClicks()      #右前轮胎状态计数器
button_clicksLR_State = ButtonClicks()      #左后轮胎状态计数器
button_clicksRR_State = ButtonClicks()      #右后轮胎状态计数器


def FalseScreenCard(LFCard,RFCard,LRCard,RRCard):
    #判断当前是否为无仪表屏车型，如果是无仪表车型，则需要发送胎压异常文言，否则不出现卡片
    if JudgeScreen() == False:
        #这里是判断当前的所有轮胎状态，来决定下面该弹什么卡片
        # 判断前轮状态
        Front = [LFCard, RFCard]
        Rear = [LRCard, RRCard]
        if max(Front) ==1 and max(Rear) == 1:
            os.system('adb shell vdt rp HOST_EALARM_ID 544')
            return
        if max(Front) !=0 and max(Rear) != 0 and max(Rear) != 3 and max(Front) != 3:
            if max(Front) + max(Rear) >2:
                os.system('adb shell vdt rp HOST_EALARM_ID 547')
                return
        if max(Front) == 1:
            os.system('adb shell vdt rp HOST_EALARM_ID 542')
            return
        if max(Front) == 2:
            os.system('adb shell vdt rp HOST_EALARM_ID 545')
            return
        # 判断后轮状态
        if max(Rear) == 1:
            os.system('adb shell vdt rp HOST_EALARM_ID 543')
            return
        if max(Rear) == 2:
            os.system('adb shell vdt rp HOST_EALARM_ID 546')
            return
        if max(Front) == 0 + max(Rear) ==0 or max(Front) or max(Rear) == 3:
            os.system('adb shell vdt rp HOST_EALARM_ID 999')


def LF_State_cli():
    LFCard = 1 + button_clicksLF_State.clicks % 4
    RFCard = button_clicksRF_State.clicks % 4
    LRCard = button_clicksLR_State.clicks % 4
    RRCard = button_clicksRR_State.clicks % 4
    FourStates(button_clicksLF_State, 'HOST_ETPMS_STATUS_LF')
    FalseScreenCard(LFCard, RFCard, LRCard, RRCard)


def RF_State_cli():
    LFCard = button_clicksLF_State.clicks % 4
    RFCard = 1 + button_clicksRF_State.clicks % 4
    LRCard = button_clicksLR_State.clicks % 4
    RRCard = button_clicksRR_State.clicks % 4
    FourStates(button_clicksRF_State, 'HOST_ETPMS_STATUS_RF')
    FalseScreenCard(LFCard, RFCard, LRCard, RRCard)


def LR_State_cli():
    LFCard = button_clicksLF_State.clicks % 4
    RFCard = button_clicksRF_State.clicks % 4
    LRCard = 1 +button_clicksLR_State.clicks % 4
    RRCard = button_clicksRR_State.clicks % 4
    FourStates(button_clicksLR_State, 'HOST_ETPMS_STATUS_LB')
    FalseScreenCard(LFCard, RFCard, LRCard, RRCard)


def RR_State_cli():
    LFCard = button_clicksLF_State.clicks % 4
    RFCard = button_clicksRF_State.clicks % 4
    LRCard = button_clicksLR_State.clicks % 4
    RRCard = 1 +button_clicksRR_State.clicks % 4
    FourStates(button_clicksRR_State, 'HOST_ETPMS_STATUS_RB')
    FalseScreenCard(LFCard, RFCard, LRCard, RRCard)

#油箱盖开关
button_FuelCap = ButtonClicks()
def FuelCap_cli():
    TwoStates(button_FuelCap,'HOST_FUEL_PORT_POS_IND')