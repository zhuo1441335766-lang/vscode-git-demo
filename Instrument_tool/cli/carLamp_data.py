import os

from lib import *

# NGP
button_clicksNGP = ButtonClicks()
button_clicksMaxNGP = ButtonClicks()
button_clicksMaxLCC = ButtonClicks()
button_clicksMaxAPA = ButtonClicks()
def Button_NGP():
    if JudgeMaxCar() == True:
        NGP = 1 + button_clicksMaxNGP.clicks % 7
        LCC = button_clicksMaxLCC.clicks % 4
        APA = button_clicksMaxAPA.clicks % 3
        #因为LCC和NGP的Value值并不是按顺序排列的，，故用字典来进行匹配
        LccMaxValue = {0:0, 1:2, 2:4, 3:9}
        NgpMaxValue = {0:0, 1:1, 2:2, 3:4, 4:5, 5:6, 6:7}
        vdts({
                'HOST_AUTO_PILOT_STATE': [LccMaxValue.get(LCC),APA,NgpMaxValue.get(NGP)],
            })
        button_clicksMaxNGP.clicks += 1
    else:
        os.system('adb shell vdt rp HOST_XPU_RD_PK_HMI_MODE 1')
        # ThreeStates(button_clicksNGP, 'HOST_MCU_ENGP_IND')
        i = 1 + button_clicksNGP.clicks % 7
        ngpvalue = {1:1, 2:2, 3:4, 4:5, 5:6, 6:7}
        vdts({
                'HOST_MCU_ENGP_IND': ngpvalue.get(i),
            })
        button_clicksNGP.clicks += 1


    # ACC
button_clicksACC = ButtonClicks()

def Button_ACC():
    os.system('adb shell vdt rp HOST_XPU_RD_PK_HMI_MODE 1')
    i = 1 + button_clicksACC.clicks % 6
    accvalue = {1:6, 2:4, 3:7, 4:8, 5:9}
    vdts({
            'HOST_MCU_EACC_CC_LIGHT': accvalue.get(i),
        })
    button_clicksACC.clicks += 1

    # LCC


button_clicksLCC = ButtonClicks()


def Button_LCC():
    if JudgeMaxCar() == True:
        NGP = button_clicksMaxNGP.clicks % 7
        LCC = 1 + button_clicksMaxLCC.clicks % 4
        APA = button_clicksMaxAPA.clicks % 3
        #因为LCC和NGP的Value值并不是按顺序排列的，，故用字典来进行匹配
        LccMaxValue = {0:0, 1:2, 2:4, 3:9}
        NgpMaxValue = {0:0, 1:1, 2:2, 3:4, 4:5, 5:6, 6:7}
        vdts({
                'HOST_AUTO_PILOT_STATE': [LccMaxValue.get(LCC),APA,NgpMaxValue.get(NGP)],
            })
        button_clicksMaxLCC.clicks += 1
    else:
        os.system('adb shell vdt rp HOST_XPU_RD_PK_HMI_MODE 1')
        # ThreeStates(button_clicksLCC, 'HOST_XPU_AUTO_PILOT_ST')
        i = 1 + button_clicksLCC.clicks % 4
        if i == 4:
                vdts({
                    'HOST_XPU_AUTO_PILOT_ST': 0,
                })
                QNXcmd('HOST_XPU_AUTO_PILOT_ST', 0)
        elif i == 3:
                vdts({
                    'HOST_XPU_AUTO_PILOT_ST': 8,
                })
                QNXcmd('HOST_XPU_AUTO_PILOT_ST', 8)
        else:
            vdts({
                    'HOST_XPU_AUTO_PILOT_ST': i,
                })
            QNXcmd('HOST_XPU_AUTO_PILOT_ST', str(i))
        button_clicksLCC.clicks += 1
    # APA


button_clicksAPA = ButtonClicks()

def Button_APA():
    if JudgeMaxCar() == True:
        NGP = button_clicksMaxNGP.clicks % 7
        LCC = button_clicksMaxLCC.clicks % 4
        APA = 1 + button_clicksMaxAPA.clicks % 3
        #因为LCC和NGP的Value值并不是按顺序排列的，，故用字典来进行匹配
        LccMaxValue = {0:0, 1:2, 2:4, 3:9}
        NgpMaxValue = {0:0, 1:1, 2:2, 3:4, 4:5, 5:6, 6:7}
        vdts({
                'HOST_AUTO_PILOT_STATE': [LccMaxValue.get(LCC),APA,NgpMaxValue.get(NGP)],
            })
        button_clicksMaxAPA.clicks += 1
    else:
        os.system('adb shell vdt rp HOST_XPU_RD_PK_HMI_MODE 2')
        os.system('adb shell vdt rp XPU_RD_PK_HMI_MODE 2')
        ThreeStates(button_clicksAPA, 'HOST_ICM_APA_STATUS')

    # VPA
button_clicksVPA = ButtonClicks()

def Button_VPA():
    os.system('adb shell vdt rp HOST_XPU_RD_PK_HMI_MODE 2')
    os.system('adb shell vdt rp XPU_RD_PK_HMI_MODE 2')
    ThreeStates(button_clicksVPA, 'HOST_ICM_VPA_STATUS')




    # 车门指示灯


button_clicksCarDoor = ButtonClicks()


def Button_CarDoor():
    i = 1 + button_clicksCarDoor.clicks % 12
    carbody = ['0 0 0 0', '1 0 0 0', '0 1 0 0', '0 0 1 0', '0 0 0 1', '1 1 0 0', '1 0 1 0', '1 0 0 1', '1 1 1 0',
               '0 1 1 1', '1 1 1 1']

    if i == 11:
        vdts({
            'HOST_BCM_BONNET': 1,
            'HOST_BCM_DOOR': [0, 0, 0, 0]
        })
    elif i == 12:
        vdts({
            'HOST_BCM_BONNET': 0,
        })
    else:
        vdts({
            'HOST_BCM_DOOR': carbody[i],
        })

    button_clicksCarDoor.clicks += 1

    # 手刹灯


button_clicksParking = ButtonClicks()


def Button_Parking():
    TwoStates(button_clicksParking, 'HOST_ESP_APB_FUNC_LAMP')

    # Auto自启停灯


button_clicksAuto = ButtonClicks()


def Button_Auto():
    ThreeStates(button_clicksAuto, 'HOST_ESP_IND_LIGHT_AVH')

    # 主驾安全带


button_clicksDriverSeatBelt = ButtonClicks()


def Button_clicksDriverSeatBelt():
    TwoStates(button_clicksDriverSeatBelt, 'HOST_BCM_EDRIVER_SEAT')

    # 后左安全带


button_clicksREARLEFTSeatBelt = ButtonClicks()


def Button_clicksREARLEFTSeatBelt():
    ThreeStates(button_clicksREARLEFTSeatBelt, 'HOST_BCM_2NDLEFTSEAT_BELTSBR_WARNING')

    # 后中安全带


button_clicksREARMidSeatBelt = ButtonClicks()


def Button_clicksREARMidSeatBelt():
    ThreeStates(button_clicksREARMidSeatBelt, 'HOST_BCM_2NDMIDSEAT_BELTSBR_WARNING')

    # 后右安全带


button_clicksREARRitSeatBelt = ButtonClicks()


def Button_clicksREARRitSeatBelt():
    ThreeStates(button_clicksREARRitSeatBelt, 'HOST_BCM_2NDRIGHTSEAT_BELTSBR_WARNING')

    # 12V蓄电池故障


button_clicksBatteryFail = ButtonClicks()


def Button_clicksBatteryFail():
    TwoStates(button_clicksBatteryFail, 'HOST_VCU_IND_12V_BAT')

    # 充电指示灯


button_clicksCharge = ButtonClicks()


def Button_clicksCharge():
    TwoStates(button_clicksCharge, 'HOST_VCU_CHARGE_GUN_STATUS')

    # 后雾灯


button_clicksFogLamp = ButtonClicks()


def Button_clicksFogLamp():
    TwoStates(button_clicksFogLamp, 'HOST_FOG_LIGHTS_SWITCH_XP')

    # 示宽灯


button_clicksLED = ButtonClicks()


def Button_clicksLED():
    TwoStates(button_clicksLED, 'HOST_BCM_PARKING_LAMP')

    # 近光灯


button_clicksLowBeam = ButtonClicks()


def Button_clicksLowBeam():
    i = 1 + button_clicksLowBeam.clicks % 4
    if i == 4:
        vdts({
            'HOST_BCM_ELOW_BEAM': 0,
        })
    else:
        vdts({
            'HOST_BCM_ELOW_BEAM': i,
        })
    button_clicksLowBeam.clicks += 1

    # 智能远光


button_clicksIHB = ButtonClicks()


def Button_clicksIHB():
    i = 1 + button_clicksIHB.clicks % 4
    if i == 4:
        vdts({
            'HOST_BCM_SMART_HIGHBEAM_ST': 0,
        })
    else:
        vdts({
            'HOST_BCM_SMART_HIGHBEAM_ST': i,
        })
    button_clicksIHB.clicks += 1

    # 副驾安全带


button_clicksPaGeBelt = ButtonClicks()


def Button_clicksPaGeBelt():
    TwoStates(button_clicksPaGeBelt, 'HOST_BCM_EPSNGR_SEAT')

    # 电动系统故障


button_clicksDSP = ButtonClicks()


def Button_clicksDSP():
    TwoStates(button_clicksDSP, 'HOST_VCU_EVERRLAMP_DSP')

    # ESP指示灯


button_clicksESP = ButtonClicks()


def Button_clicksESP():
    TwoStates(button_clicksESP, 'HOST_ESP_ESP_FAULT')

    # ESPOFF指示灯


button_clicksESPOF = ButtonClicks()


def Button_clicksESPOF():
    TwoStates(button_clicksESPOF, 'HOST_ESC_ESP')

    # ABS指示灯


button_clicksABS = ButtonClicks()


def Button_clicksABS():
    TwoStates(button_clicksABS, 'HOST_ESP_ABS_FAULT')

    # 左2
    # 驻车故障


button_clicksREQ = ButtonClicks()


def Button_clicksREQ():
    TwoStates(button_clicksREQ, 'HOST_ESP_SYS_WARNIND_REQ')

    # 转向助力


button_clicksLAMP = ButtonClicks()


def Button_clicksLAMP():
    TwoStates(button_clicksLAMP, 'HOST_ESP_WARN_LAMP')

    # 胎压系统


button_clicksTPMS = ButtonClicks()


def Button_clicksTPMS():
    TwoStates(button_clicksTPMS, 'HOST_TPMS_SYSFAULTWARN')

    # 电机过热


button_clicksEMOTOR = ButtonClicks()


def Button_clicksEMOTOR():
    TwoStates(button_clicksEMOTOR, 'HOST_VCU_EMOTOR_SYS_HOT_DISP')

    # 电池过热


button_clicksBAT = ButtonClicks()


def Button_clicksBAT():
    TwoStates(button_clicksBAT, 'HOST_VCU_BAT_HOT_DISP')

    # 驱动功率限制


button_clicksBSP = ButtonClicks()


def Button_clicksBSP():
    TwoStates(button_clicksBSP, 'HOST_VCU_POWERLIMITATION_DSP')

    # 动力电池切断


button_clicksCUTOFF = ButtonClicks()


def Button_clicksCUTOFF():
    TwoStates(button_clicksCUTOFF, 'HOST_VCU_HV_CUTOFF_DISP')

    # 电池低压


button_clicksSOCLOW = ButtonClicks()


def Button_clicksSOCLOW():
    TwoStates(button_clicksSOCLOW, 'HOST_VCU_BMS_SOCLOW_STATUS')

    # 电池故障


button_clicksBATT = ButtonClicks()


def Button_clicksBATT():
    TwoStates(button_clicksBATT, 'HOST_VCU_BATT_FAULT_DISP')

    # 右2
    # 悬挂故障
button_clicksAS = ButtonClicks()

def Button_clicksAS():
    ThreeStates(button_clicksAS, 'HOST_AS_FAULT_LAMP_IND')

    # 减震故障
button_clicksCDC = ButtonClicks()
def Button_clicksCDC():
    TwoStates(button_clicksCDC, 'HOST_CDC_FAULT_LAMP_IND')

    # 制动故障

button_clicksESPB = ButtonClicks()


def Button_clicksESPB():
    ThreeStates(button_clicksESPB, 'HOST_ESP_BOOST_FAULT_ST')

    # 陡坡缓降


button_clicksHDC = ButtonClicks()


def Button_clicksHDC():
    FourStates(button_clicksHDC, 'HOST_HDC_IND')

    # 碰撞预警


button_clicksSCU = ButtonClicks()


def Button_clicksSCU():
    ThreeStates(button_clicksSCU, 'HOST_SCU_MRR_FCW_WARNING_ST')

    # 电机故障
button_clicksIPU = ButtonClicks()

def Button_clicksIPU():
    TwoStates(button_clicksIPU, 'HOST_IPU_FAULT')


    # 安全气囊

button_clicksBCM = ButtonClicks()
def Button_clicksBCM():
    TwoStates(button_clicksBCM, 'HOST_BCM_AIRBAG_FAULT_ST')

    # 电池低温

button_clicksBATCOLD = ButtonClicks()
def Button_clicksBATCOLD():
    TwoStates(button_clicksBATCOLD, 'HOST_VCU_BATCOLD_DISP')


    # 碰撞关闭
button_clicksAEB = ButtonClicks()

def Button_clicksAEB():
    TwoStates(button_clicksAEB, 'HOST_FCW_AEB_CLOSE_STATUS')


    # 后轮转向
button_clicksVMC = ButtonClicks()

def Button_clicksVMC():
    ThreeStates(button_clicksVMC, 'HOST_VMC_FAULT_LAMP_IND')

    # 车道偏离

button_clicksLSS = ButtonClicks()
def Button_clicksLSS():
    TwoStates(button_clicksLSS, 'HOST_LSS_ELK_FAULT_IND')

    # 热管理

button_clicksCOOLANT = ButtonClicks()
def Button_clicksCOOLANT():
    TwoStates(button_clicksCOOLANT, 'HOST_VCU_COOLANT_OVERHEAT_ST')

    #副驾气囊
button_clicksPassengerAirbag = ButtonClicks()

def Button_clicksPassengerAirbag():
    TwoStates(button_clicksPassengerAirbag, 'HOST_MCU_EPSNGR_SRS_CLOSE')

    #洗涤不足
button_clicksInsufficientWash = ButtonClicks()

def Button_clicksInsufficientWash():
    TwoStates(button_clicksInsufficientWash, 'HOST_MCU_EWASHERFLUID_ST')

    # 限速故障
button_clicksSpeedFault = ButtonClicks()

def Button_clicksSpeedFault():
    TwoStates(button_clicksSpeedFault, 'HOST_SAS_FAIL_IND')

    # 居中故障
button_clicksELccFault = ButtonClicks()

def Button_clicksELccFault():
    TwoStates(button_clicksELccFault, 'HOST_MCU_ELCC_FAILURE')


    #自动变道
button_clicksALC = ButtonClicks()

def Button_clicksALC():
    i = 1 + button_clicksALC.clicks % 5
    if i == 5:
        vdts({
            'HOST_MCU_EALC_IND': 0,
        })
    else:
        vdts({
            'HOST_MCU_EALC_IND': i,
        })
    button_clicksALC.clicks += 1

    #自驾故障
    #模拟LCC 4级故障
button_clicksAutoDrivPilot = ButtonClicks()
def Button_clicksAutoDrivPilot():
    i = 1 + button_clicksAutoDrivPilot.clicks % 2
    if i == 1:
        vdts({
            'HOST_XPU_AUTO_PILOT_ST': 4,
            })
        QNXcmd('HOST_XPU_AUTO_PILOT_ST',4)
    else:
        vdts({
            'HOST_XPU_AUTO_PILOT_ST': 0,
            })
        QNXcmd('HOST_XPU_AUTO_PILOT_ST',0)
    button_clicksAutoDrivPilot.clicks += 1

    #左右转向灯
button_LeftSignal= ButtonClicks()
button_RightSignal= ButtonClicks()
def LeftSignal_cli():
    L = 1 + button_LeftSignal.clicks % 2
    R = button_RightSignal.clicks % 2
    vdts({
        'HOST_LTURNLAMP_RTURNLAMP_ST': [L,R],
        'HOST_MODEL_TURNLIGHT_FRONT': [L, R],
        'BCM_LRTURNLAMP_ACTIVE_ST ': [L, R],
    })
    button_LeftSignal.clicks += 1

def RightSignal_cli():
    L = button_LeftSignal.clicks % 2
    R = 1 + button_RightSignal.clicks % 2
    vdts({
        'HOST_LTURNLAMP_RTURNLAMP_ST': [L,R],
        'HOST_MODEL_TURNLIGHT_FRONT': [L, R],
        'BCM_LRTURNLAMP_ACTIVE_ST ': [L, R],
    })
    button_RightSignal.clicks += 1

    #AEB重置
button_clicksAEBInitialize = ButtonClicks()
def Button_clicksAEBInitialize():
    i = 1 + button_clicksAEBInitialize.clicks % 2
    if i == 1:
        vdts({
            'HOST_SCU_MRR_FCW_WARNING_ST ': 3,
            })
    else:
        vdts({
            'HOST_SCU_MRR_FCW_WARNING_ST ': 0,
            })
    button_clicksAEBInitialize.clicks += 1

#拖车钩
button_TrailerHook = ButtonClicks()
def Button_TrailerHook():
    FourStates(button_TrailerHook, 'HOST_BCM_TRAILER_MODE_ST')


#智能底盘
button_SmartChassis = ButtonClicks()
def SmartChassis_cli():
    ThreeStates(button_SmartChassis, 'HOST_INTELLIGENT_CHASSIS_IND')

#发动机Mil灯
button_MilLamp = ButtonClicks()
def MilLamp_cli():
    TwoStates(button_MilLamp, 'HOST_MIL_IND')

#机油压力报警
button_EngineOilAlarm = ButtonClicks()
def EngineOilAlarm_cli():
    TwoStates(button_EngineOilAlarm, 'HOST_ENGINE_OIL_PRESSURE_ALERT')

#燃油不足
button_FuelLow = ButtonClicks()
def FuelLow_cli():
    TwoStates(button_FuelLow, 'HOST_FUEL_LOW_IND')

#水温警报
button_WaterHigh = ButtonClicks()
def WaterHigh_cli():
    TwoStates(button_WaterHigh, 'HOST_ENGINE_COOLANT_ALERT')

#SVS故障
button_SVSalarm = ButtonClicks()
def SVSalarm_cli():
    TwoStates(button_SVSalarm, 'HOST_SVS_IND')
# #ready指示灯
# button_clicksReady = ButtonClicks()
# def RangeReady():
#     TwoStates(button_clicksReady,'HOST_VCU_EVSYS_READYST')