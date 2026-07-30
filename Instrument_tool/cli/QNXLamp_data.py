from lib import *

# NGP
button_clicksNGP = ButtonClicks()
def Button_NGP():
    # os.system('adb shell vdt rp HOST_XPU_RD_PK_HMI_MODE 1')
    QNXcmd('HOST_XPU_RD_PK_HMI_MODE', 1)
    ThreeStates(button_clicksNGP, 'HOST_MCU_ENGP_IND')


    # ACC
button_clicksACC = ButtonClicks()
def Button_ACC():
    # os.system('adb shell vdt rp HOST_XPU_RD_PK_HMI_MODE 1')
    QNXcmd('HOST_XPU_RD_PK_HMI_MODE',1)
    i = 1 + button_clicksACC.clicks % 6
    accvalue = {1:6, 2:4, 3:7, 4:8, 5:9}
    # vdts({
    #         'HOST_MCU_EACC_CC_LIGHT': accvalue.get(i),
    #     })
    QNXcmd('HOST_MCU_EACC_CC_LIGHT',accvalue.get(i))
    button_clicksACC.clicks += 1

    # LCC


button_clicksLCC = ButtonClicks()
def Button_LCC():
    # os.system('adb shell vdt rp HOST_XPU_RD_PK_HMI_MODE 1')
    QNXcmd('HOST_XPU_RD_PK_HMI_MODE',1)
    ThreeStates(button_clicksLCC, 'HOST_XPU_AUTO_PILOT_ST')

    # APA


button_clicksAPA = ButtonClicks()
def Button_APA():
    # os.system('adb shell vdt rp HOST_XPU_RD_PK_HMI_MODE 2')
    QNXcmd('HOST_XPU_RD_PK_HMI_MODE',2)
    ThreeStates(button_clicksAPA, 'HOST_ICM_APA_STATUS')

    # VPA


button_clicksVPA = ButtonClicks()


def Button_VPA():
    # os.system('adb shell vdt rp HOST_XPU_RD_PK_HMI_MODE 2')
    QNXcmd('HOST_XPU_RD_PK_HMI_MODE',2)
    ThreeStates(button_clicksVPA, 'HOST_ICM_VPA_STATUS')

    # 车门指示灯


button_clicksCarDoor = ButtonClicks()
def Button_CarDoor():
    i = 1 + button_clicksCarDoor.clicks % 12
    carbody = ['0 0 0 0', '1 0 0 0', '0 1 0 0', '0 0 1 0', '0 0 0 1', '1 1 0 0', '1 0 1 0', '1 0 0 1', '1 1 1 0',
               '0 1 1 1', '1 1 1 1']
    if i == 11:
        # vdts({
        #     'HOST_BCM_BONNET': 1,
        #     'HOST_BCM_DOOR': [0, 0, 0, 0]
        # })
        QNXcmd('HOST_BCM_BONNET',1)
        QNXcmd('HOST_BCM_DOOR', [0, 0, 0, 0])
    elif i == 12:
        # vdts({
        #     'HOST_BCM_BONNET': 0,
        # })
        QNXcmd('HOST_BCM_BONNET',0)
    else:
        # vdts({
        #     'HOST_BCM_DOOR': carbody[i],
        # })
        QNXcmd('HOST_BCM_DOOR',carbody[i])
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
        # vdts({
        #     'HOST_BCM_ELOW_BEAM': 0,
        # })
        QNXcmd('HOST_BCM_ELOW_BEAM',0)
    else:
        # vdts({
        #     'HOST_BCM_ELOW_BEAM': i,
        # })
        QNXcmd('HOST_BCM_ELOW_BEAM',i)
    button_clicksLowBeam.clicks += 1

    # 智能远光

button_clicksIHB = ButtonClicks()
def Button_clicksIHB():
    i = 1 + button_clicksIHB.clicks % 4
    if i == 4:
        # vdts({
        #     'HOST_BCM_SMART_HIGHBEAM_ST': 0,
        # })
        QNXcmd('HOST_BCM_SMART_HIGHBEAM_ST',0)
    else:
        # vdts({
        #     'HOST_BCM_SMART_HIGHBEAM_ST': i,
        # })
        QNXcmd('HOST_BCM_SMART_HIGHBEAM_ST',i)
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


    # 制动故障

button_clicksESPB = ButtonClicks()
def Button_clicksESPB():
    ThreeStates(button_clicksESPB, 'HOST_ESP_BOOST_FAULT_ST')


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



####车速相关


####
# 车速
def CarSpeed_Data(key):
    if key == '':
        pass
    else:
        # vdts({
        # 'HOST_VCU_RAW_CAR_SPEED': key,
        #  })
        QNXcmd('HOST_VCU_RAW_CAR_SPEED', key)


# ACC速度
def Acc_Speed_Data(cli):
    # vdts({
    #     'HOST_ESPEED_XCC': cli,
    #
    # })
    QNXcmd('HOST_ESPEED_XCC', cli)
