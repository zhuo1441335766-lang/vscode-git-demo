import os
import time

from lib import *

#充电选择列表
def Charge_type_cli(cli):
    List = ['未充电','充电准备', '充电中', '充电完成', '充电故障', '充枪连接', '预约充电', '电池加热',
            '电池冷却', '供电准备', '供电中', '供电故障', '供电停止', '未知状态']
    vdts({
        'HOST_MCU_CHARGING_STATE': List.index(cli),
    })
    charge = {'未充电':0,'充电准备':0,'充电中':2,'充电完成':4,'充电故障':3, '充枪连接':0, '预约充电':1, '电池加热':0,
            '电池冷却':0, '供电准备':0, '供电中':5, '供电故障':7, '供电停止':6, '未知状态':0}
    out_charge = ['供电准备', '供电中', '供电故障', '供电停止']
    if cli == '未充电':   #如果检测为非供电，大屏设置插充电枪
        vdts({
            'VCU_CHARGE_GUN_STATUS': 0,
        })
    elif cli not in out_charge:    #如果检测为非供电，大屏设置插充电枪
        vdts({
            'VCU_CHARGE_GUN_STATUS': 2,
        })
    else:           #如果检测为供电，大屏设置插供电枪
        vdts({
            'VCU_CHARGE_GUN_STATUS': 4,
        })
    time.sleep(0.5)
    vdts({      #将获取到的充电状态映射到大屏，使仪表与大屏的充电态一致
        'VCU_CHARGE_STATUS': charge.get(cli),
    })

#超级充电
def Super_Charge_cli(cli):

    if cli == '快速充电中':
        vdts({
        'HOST_FAST_CHARGE_STATUS': 2
    })
    elif cli == '极速充电中':
        vdts({
        'HOST_VCU_SUPER_CHRG_FLG': 1,
        'HOST_FAST_CHARGE_STATUS': 3
    })
    else:
        vdts({
            'HOST_VCU_SUPER_CHRG_FLG': 0,
            'HOST_FAST_CHARGE_STATUS': 0
        })


    #电流电压功率
def Charge_cli(current,voltage,power):
    vdts({
        'HOST_ECHARGE_CUR': [2,2,current,0,0],  #电流
        'VCU_OBC_DCCUR':current,    #大屏慢充电流
        'VCU_DCCCS_CURR':current,  #大屏快充电流
        'HOST_ECHARGE_VOLTAGE':[2,2,voltage],   #电压
        'VCU_OBC_DCVOLT': voltage,  # 大屏慢充电压
        'VCU_DCCCS_SUMU': voltage,  # 大屏快充电压
        'HOST_VCU_CHRG_PWR':power,  #功率
        'VCU_CHRG_PWR':power        #大屏功率

    })

#随机发送充电数值
def Charge_random_cli():
    current = round(random.uniform(100, 220),1)
    voltage = round(random.uniform(360, 600),1)
    power = round(random.uniform(50, 120),1)
    vdts({
        'HOST_ECHARGE_CUR': [2,2,current,0,0],  #电流
        'VCU_OBC_DCCUR':current,    #大屏慢充电流
        'VCU_DCCCS_CURR':current,  #大屏快充电流
        'HOST_ECHARGE_VOLTAGE':[2,2,voltage],   #电压
        'VCU_OBC_DCVOLT': voltage,  # 大屏慢充电压
        'VCU_DCCCS_SUMU': voltage,  # 大屏快充电压
        'HOST_VCU_CHRG_PWR':power,  #功率
        'VCU_CHRG_PWR':power        #大屏功率

    })

#其他信息
def ChargeOther_cli(time,chargtime,time_sh,time_sm,powersupply,time_eh,time_em):
    if powersupply == '':
        powersupply = 0
    # else:
    #     powersupply = 10* float(powersupply)
    if time_eh =='':
        time_eh = 0
    if time_em == '':
        time_em = 0
    if time_sh =='':
        time_sh = 0
    if time_sm == '':
        time_sm = 0
    vdts({
        'HOST_ECHARGE_LIMIT_TIME':time,     #剩余时间
        'VCU_CHARGE_COMPLETE_TIME':time,    #大屏剩余时间
        'HOST_ICM_CHARGING_DURATION ':chargtime,     #充电时长
        'HOST_VCU_DISCHARGE_BATTCAP_FLOAT': 10* float(powersupply),    #供电量
        'VCU_DISCHARGE_BATTCAP_FLOAT': float(powersupply),  # 大屏供电量
        'HOST_TBOX_APPOINT_CHG_SET_HOUR':time_sh,    #预约小时
        'HOST_TBOX_APPOINT_CHG_SET_MIN':time_sm,     #预约分钟
        'HOST_TBOX_APPOINT_CHG_TIME':[21,34,time_eh,time_em],    #预约结束时间
        'TBOX_APPOINT_CHG_SET':[2,time_sh,time_sm,time_eh,time_em]


    })

    #随机发其他信息
def ChargeOther_random_cli():
    powersupply = round(random.uniform(1, 30),1)
    vdts({
        'HOST_ECHARGE_LIMIT_TIME': random.randint(0, 500),
        'HOST_ICM_CHARGING_DURATION ': random.randint(0, 500),
        'HOST_VCU_DISCHARGE_BATTCAP_FLOAT': powersupply * 10,
        'HOST_TBOX_APPOINT_CHG_SET_HOUR': random.randint(0, 23),
        'HOST_TBOX_APPOINT_CHG_SET_MIN': random.randint(0, 59),
        'HOST_TBOX_APPOINT_CHG_TIME': [21, 34, random.randint(0, 23), random.randint(0, 59)]
    })

#底部电池的加热冷却icon
button_batteryStyle = ButtonClicks()
def battery_style_cli():
    i = 1 + button_batteryStyle.clicks % 3
    if i == 1:
        vdts({
            'HOST_VCU_DC_PRE_WARM_ST ': 1,
            })
    elif i == 2:
        vdts({
            'HOST_VCU_DC_PRE_WARM_ST ': 17,
        })
    else:
        vdts({
            'HOST_VCU_DC_PRE_WARM_ST ': 0,
            })
    button_batteryStyle.clicks += 1



def ChargeLimit_cli(Charge,DisCharge,addcutdown):
    if Charge == '':
        Charge = 0
    if DisCharge == '':
        DisCharge = 0
    vdts({
        'HOST_ESOCMAXCHG_PWLIMIT 1': [Charge,DisCharge],    #充放电限值
        'TBOX_CHARGE_STOP_SOC':Charge,  #大屏充电限值
        'VCU_V2L_POWERLIMIT':DisCharge, #大屏放电限值
        'HOST_ESOCMAXCHG_PWLIMIT 0': [Charge,DisCharge],    #充放电限值
        'HOST_ICM_CHANGE_MILEAGE 1': addcutdown,
        'HOST_ICM_CHANGE_MILEAGE 0': addcutdown,
    })

    #充至充电限值
button_FullyCharged = ButtonClicks()
def FullyCharged(Value,time_eh,time_em,time_sh,time_sm):
    if time_eh =='':
        time_eh = 0
    if time_em == '':
        time_em = 0
    if time_sh =='':
        time_sh = 0
    if time_sm == '':
        time_sm = 0
    if Value == 1:
        vdts({
        'HOST_TBOX_APPOINT_CHG_TIME':[21,34,25,61],
        'TBOX_APPOINT_CHG_SET':[2,time_sh,time_sm,31,63]
    })
    else:
        vdts({
            'HOST_TBOX_APPOINT_CHG_TIME': [21, 34, time_eh, time_em],  # 预约结束时间
            'TBOX_APPOINT_CHG_SET':[2,time_sh,time_sm,time_eh,time_em]
        })

#电池状态/类型
def BatteryType_cli(Battery_type):
    os.system('adb root')
    if Battery_type == '电池加热':
        vdts({
            'HOST_VCU_DC_PRE_WARM_ST ': 1,
            })
    elif Battery_type == '电池预冷':
        vdts({
            'HOST_VCU_DC_PRE_WARM_ST ': 17,
            })
    elif Battery_type == '修改磷酸铁锂':
        os.system('adb shell setprop persist.sys.xiaopeng.batteryType 1')
        os.system('adb shell "pidof com.xiaopeng.instrument | xargs kill"')
        os.system('adb shell "pidof com.xiaopeng.chargecontrol | xargs kill"')
        os.system('adb shell "pidof com.xiaopeng.smartcontrol | xargs kill"')
        os.system('adb shell "pidof com.xiaopeng.subreality | xargs kill"')
    elif Battery_type == '修改三元锂':
        os.system('adb shell setprop persist.sys.xiaopeng.batteryType 0')
        os.system('adb shell "pidof com.xiaopeng.instrument | xargs kill"')
        os.system('adb shell "pidof com.xiaopeng.chargecontrol | xargs kill"')
        os.system('adb shell "pidof com.xiaopeng.smartcontrol | xargs kill"')
        os.system('adb shell "pidof com.xiaopeng.subreality | xargs kill"')
    else:
        vdts({
            'HOST_VCU_DC_PRE_WARM_ST ': 0,
            })