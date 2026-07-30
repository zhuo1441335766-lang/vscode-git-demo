from lib import *

    #车速
def CarSpeed_cli(key):
    if key == '':
        pass
    else:
        vdts({
        'HOST_VCU_RAW_CAR_SPEED': key,
        'VCU_RAW_CAR_SPEED': key,
         })

    #限速相关
def Selected_cli(speed_type):      #限速类型
    if speed_type == '无限速':
        vdts({
            'HOST_EIND_TRS_SPEED': 0,
            'HOST_XPU_SPD_LMT_TYPE':0,
        })
    elif speed_type == '导航限速':
        vdts({
            'HOST_XPU_SPD_LMT_TYPE': 0,
            'HOST_EIND_TRS_SPEED': 1,
        })
    elif speed_type == '导航超速1':
        vdts({
            'HOST_EIND_TRS_SPEED': 4,
            'HOST_XPU_SPD_LMT_TYPE': 0,
        })
    elif speed_type == '导航超速2':
        vdts({
            'HOST_EIND_TRS_SPEED': 5,
            'HOST_XPU_SPD_LMT_TYPE': 0,
        })
    elif speed_type == '电子限速':
        vdts({
            'HOST_EIND_TRS_SPEED': 1,
            'HOST_XPU_SPD_LMT_TYPE': 2,
        })
    elif speed_type == '电子超速1':
        vdts({
            'HOST_EIND_TRS_SPEED': 4,
            'HOST_XPU_SPD_LMT_TYPE': 2,
        })
    elif speed_type == '电子超速2':
        vdts({
            'HOST_EIND_TRS_SPEED': 5,
            'HOST_XPU_SPD_LMT_TYPE': 2,
        })
    else:
        vdts({
            'HOST_EIND_TRS_SPEED': 0,
            'HOST_XPU_SPD_LMT_TYPE': 0,
        })

def SelectedSpeed_value_cli(speed_value):      #限速值
    vdts({
        'HOST_ESPEED_LIMIT': speed_value,
    })


#ACC速度
def Acc_Speed_cli(cli):
    vdts({
        'HOST_ESPEED_XCC': cli,

    })

    #TSR相关
def Tsr_cli(cli):
    List = ['无TSR', '禁止超车', '解除超车','禁止进入','禁止通行','禁止临停','禁止泊车','禁止长停','禁机动车',
        '停车让行','减速让行','道路入口','道路出口','禁止左转','禁止右转','禁止直行','禁止掉头']
    vdts({
        'HOST_EIND_TRS_FORB': List.index(cli),
    })


    #红绿灯相关

    #红绿灯类型
def Lights_cli(cli):
    List = ['无红绿灯', '左转绿灯', '左转黄灯','左转红灯','左转黑灯','直行绿灯','直行黄灯',
                          '直行红灯','直行黑灯','右转绿灯','右转黄灯','右转红灯','右转黑灯','掉头绿灯','掉头黄灯','掉头红灯','掉头黑灯']
    vdts({
        'HOST_ICM_FUSION_TRAFFIC_LIGHTS_COLOR': List.index(cli),
    })

    #红绿灯读秒
def LightsTime_cli(Value):
    vdts({
        'HOST_ICM_FUSION_TRAFFIC_LIGHTS_COUNTER':Value
    })

    #左右转向灯
button_LeftSignal= ButtonClicks()
button_RightSignal= ButtonClicks()
def LeftSignal_cli():
    L = 1 + button_LeftSignal.clicks % 2
    R = button_RightSignal.clicks % 2
    vdts({
        'HOST_LTURNLAMP_RTURNLAMP_ST': [L,R],
        'HOST_MODEL_TURNLIGHT_FRONT': [L, R],
    })
    button_LeftSignal.clicks += 1

def RightSignal_cli():
    L = button_LeftSignal.clicks % 2
    R = 1 + button_RightSignal.clicks % 2
    vdts({
        'HOST_LTURNLAMP_RTURNLAMP_ST': [L,R],
        'HOST_MODEL_TURNLIGHT_FRONT': [L, R],
    })
    button_RightSignal.clicks += 1