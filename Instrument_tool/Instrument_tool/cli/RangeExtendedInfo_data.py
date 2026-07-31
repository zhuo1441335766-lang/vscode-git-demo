import os

from lib import *

    #发动机启动
button_EngineOpen = ButtonClicks()
def EngineOpen_cli():
    TwoStates(button_EngineOpen, 'HOST_ENGINE_STATUS')

    #发动机油量
def OilBox_cli(Value):
    vdts({
        'HOST_FUEL_VALUE': Value,
    })

    #发动机温度
def EngineHeat_cli(Value):
    vdts({
        'HOST_ENGINE_COOLANT_TEMP': Value,
    })

    #发动机转速
def EngineSpeed_cli(Value):
    vdts({
        'HOST_ENGINE_SPEED': Value,
    })

    #燃油里程
def OilMileage_cli(Value):
    Value = 10 * float(Value)
    vdts({
        'HOST_FUEL_RANGE': Value
    })

    #综合里程
def SyntheticalMileage_cli(Value):
    Value = 10 * float(Value)

    vdts({
        'HOST_VEHICLE_RANGE':Value
    })


    #切换纯电/增程
button_SwitchCarMode = ButtonClicks()
def SwitchCarMode_cli():
    os.system("adb root")
    i = 1 + button_SwitchCarMode.clicks % 2
    if i == 1:
        os.system('adb shell setprop persist.sys.xiaopeng.powertrainForm 1')
        subprocess.check_output(f'adb shell "pidof com.xiaopeng.instrument | xargs kill"', shell=True,
                                universal_newlines=True)
        button_SwitchCarMode.clicks += 1
        print(1)
        return True
    else:
        os.system('adb shell setprop persist.sys.xiaopeng.powertrainForm 0')
        subprocess.check_output(f'adb shell "pidof com.xiaopeng.instrument | xargs kill"', shell=True,
                                universal_newlines=True)
        button_SwitchCarMode.clicks += 1
        print(0)
        return False

button_EnergyMode = ButtonClicks()
def EnergyMode_cli():
    FourStates(button_EnergyMode,'HOST_VCU_ENERGY_MODE')