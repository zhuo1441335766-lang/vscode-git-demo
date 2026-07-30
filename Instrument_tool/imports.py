##由于每个模块页面都单独做了一个py文件，为了防止主程序造成视觉上的混乱，特地创建了此文件来进行所有文件的导包
import CarInfo
#安卓侧
import helmControl as Control       #方控
import charge as Charge     #
import mileage as Mileage
import carState as CarState
import energy as Energy
import autodrive as Auto
import driversRadar as DriverRadar
import carSpeedLights as SpeedTSR
import carLamp as Light
import othermation as Tip
import RangeExtendedInfo as Extended
import DoorWindowSet as DWSet

#这两条是安卓侧的控制台与底栏
from ApkLog import *
from bottom import *

#AI小P
import XGPT

#QNX
from QnxBottom import *
from QNXsys import *
import QNXLamp




    #隐藏所有列表卡片的显示
def ForgetAllCard():
    #安卓侧
    Control.helmcontrol.place_forget()
    Charge.charge.place_forget()
    Mileage.mileage.place_forget()
    CarState.carstate.place_forget()
    Energy.energy.place_forget()
    Auto.autodrive.place_forget()
    DriverRadar.driversradar.place_forget()
    SpeedTSR.carspeelig.place_forget()
    Light.carlamp.place_forget()
    Tip.othermation.place_forget()
    Extended.extended.place_forget()



    #安卓控制台与底栏
    ApkLog.place_forget()
    bottom.place_forget()
    #AI小P
    XGPT.SmartAI.place_forget()
    #QNX
    Qnxbottom.place_forget()
    QNXLamp.QnxLamp.place_forget()
    QnxControl.place_forget()

    #车控
    CarInfo.carinfo.place_forget()
    DWSet.dwset.place_forget()
