from lib import *

    #雷达故障
button_RadarFault= ButtonClicks()

def RadarFault_cli():
    i = 1 + button_RadarFault.clicks % 2
    if i == 1:
        vdts({
            'HOST_ESENSOR_ERROR_INFO': 3,   #雷达卡片
            # 'HOST_MCU_EMRADAR_CALIBRATION_STATE':1  #标定文言
        })
    else:
        vdts({
            'HOST_ESENSOR_ERROR_INFO': 0,
            # 'HOST_MCU_EMRADAR_CALIBRATION_STATE': 0
        })
    button_RadarFault.clicks += 1

    #标定文言
button_AlignFault = ButtonClicks()
def AlignFault_cli():
    TwoStates(button_AlignFault, 'HOST_MCU_EMRADAR_CALIBRATION_STATE')

button_radarLF = ButtonClicks()
button_radarRF = ButtonClicks()
button_radarLR = ButtonClicks()
button_radarRR = ButtonClicks()

def RadarLf_cli():
    TwoStates(button_radarLF,'HOST_MCU_EURADAR_CAL_FL')

def RadarRF_cli():
    TwoStates(button_radarRF,'HOST_MCU_EURADAR_CAL_FR')

def RadarLR_cli():
    TwoStates(button_radarLR,'HOST_MCU_EURADAR_CAL_RL')

def RadarRR_cli():
    TwoStates(button_radarRR,'HOST_MCU_EURADAR_CAL_RR')

    #车手模式数值
def FG_cli(Value):
    if Value == '':
        Value = 0
    InputBox('HOST_ESP_VEH_LONG_ACCEL',float(Value))

def RG_cli(Value):
    if Value == '':
        Value = 0
    InputBox('HOST_ESP_VEH_LATERAL_ACCEL',float(Value))

def Torque_cli(Value):
    InputBox('HOST_IPU_MOTOR_TORQUE',Value)