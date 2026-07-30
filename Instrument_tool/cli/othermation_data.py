from lib import *


    #通用文言
def OrdinaryNote_cli(Value):
    if Value == '':
        pass
    else:
        vdts({
            'HOST_EALARM_ID': Value,
        })

    #自驾文言
def AutoNote_cli(Value):
    if Value == '':
        pass
    else:
        vdts({
            'HOST_MCU_EAUTOPILOT_TIPS_ID': Value,
        })

#右侧卡片弹窗
def Popup_cli(Value):
    if Value == 'N挡防误触':
        vdts({
            'HOST_EGEAR_N_REMIND':1
        })
    else:
        List = {'无右侧弹窗':0, '强制下电':1,'P挡保护1':2, 'P挡保护2':3}
        vdts({
        'HOST_MCU_LEFT_POPUP_WINDOW': List.get(Value),
        'HOST_EGEAR_N_REMIND': 0
        })

#ACC车距
def AccRange_cli(Value):
    List = {'不设置弹窗':0,'1挡':1, '2挡':2,'3挡':3, '4挡':4,'5挡':5,'NGP自动':7}
    vdts({
        'HOST_XPU_EACC_LEVEL': List.get(Value)
        })

    #模拟进出天文台
button_Oty= ButtonClicks()
def Observatory_cli():
    i = 1 + button_Oty.clicks % 2
    if i == 1:
        os.system('adb shell vdt sp ICM_GEOFENCE 1')
        button_Oty.clicks += 1
        return True
    else:
        os.system('adb shell vdt sp ICM_GEOFENCE 0')
        button_Oty.clicks += 1
        return False

    #模拟仪表下电
def InstrumentIGOff_cli():
    vdts({
        'HOST_MCU_IG_DATA ': 0
    })

    #模拟进出FNGP
button_fngp= ButtonClicks()
def Intofngp_cli():
    i = 1 + button_fngp.clicks % 2
    if i == 1:
        os.system('adb shell vdt rp XPU_DRIVING_STATE_REMIND 11')
        os.system('adb shell vdt rp HOST_XPU_FNGP_DRIVE_STATE_REMIND 11')
        button_fngp.clicks += 1
        return True
    else:
        os.system('adb shell vdt rp HOST_XPU_FNGP_DRIVE_STATE_REMIND 0')
        os.system('adb shell vdt rp XPU_DRIVING_STATE_REMIND 0')
        button_fngp.clicks += 1
        return False


#模拟DD上电
button_DDig= ButtonClicks()
def DiDiIgOn_cli():
    i = 1 + button_DDig.clicks % 2
    if i == 1:
        os.system('adb shell vdt MCU_IG_DATA 1')
        os.system('adb shell vdt rp HOST_VDP_CLOWVPWRMOD 3')
        button_DDig.clicks += 1
        return True
    else:
        os.system('adb shell vdt MCU_IG_DATA 0')
        os.system('adb shell vdt rp HOST_VDP_CLOWVPWRMOD 0')
        button_DDig.clicks += 1
        return False