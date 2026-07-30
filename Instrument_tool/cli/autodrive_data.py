from lib import *

    #后碰撞预警

button_Rcw= ButtonClicks()
def Rcw_cli():
    TwoStates(button_Rcw,'HOST_EIND_RCW')

    # RAEB（海外）
button_RAEB = ButtonClicks()
def RAEB_cli():
    TwoStates(button_RAEB, 'HOST_RAEB_ACTIVE_ST')

#AEB
button_AEB = ButtonClicks()
def AEB_cli():
    TwoStates(button_RAEB, 'HOST_EIND_FCW_AEB')

    #DOW左
button_DowL= ButtonClicks()
def DowL_cli():
    TwoStates(button_DowL,'HOST_EIND_RCTA_LEFT')

    #DOW右
button_DowR= ButtonClicks()
def DowR_cli():
    TwoStates(button_DowR,'HOST_EIND_RCTA_RIGHT')

    #毫米波雷达相关

    #左侧前
def FSL_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_FSL':1
    })
    InputBox('HOST_ERADAR_FSL',Value)

    #左前
def FL_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_FL':1
    })
    InputBox('HOST_ERADAR_SPACING_FOL',Value)

    #左前中
def FCL_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_FCL':1
    })
    InputBox('HOST_ERADAR_SPACING_FCL',Value)

    #右前中
def FCR_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_FCR':1
    })
    InputBox('HOST_ERADAR_SPACING_FCR',Value)

    #右前
def FR_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_FR':1
    })
    InputBox('HOST_ERADAR_SPACING_FOR',Value)

    #右侧前
def FSR_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_FSR':1
    })
    InputBox('HOST_ERADAR_FSR',Value)

    #左侧后
def RSL_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_RSL':1
    })
    InputBox('HOST_ERADAR_RSL',Value)

    #左后
def RL_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_RL':1
    })
    InputBox('HOST_ERADAR_SPACING_ROL',Value)

    #左后中
def RCL_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_RCL':1
    })
    InputBox('HOST_ERADAR_SPACING_RCL',Value)

    #右后中
def RCR_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_RCR':1
    })
    InputBox('HOST_ERADAR_SPACING_RCR',Value)

    #右后
def RR_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_RR':1
    })
    InputBox('HOST_ERADAR_SPACING_ROR',Value)

    #右侧后
def RSR_cli(Value):
    vdts({
        'HOST_ERADAR_LEVEL_RSR':1
    })
    InputBox('HOST_ERADAR_RSR',Value)

    #前后预警距离
def AlarmFront_cli(Value1,Value2):
    InputBox('HOST_ERADAR_FDISTANCE', Value1)
    InputBox('HOST_ERADAR_RDISTANCE', Value2)