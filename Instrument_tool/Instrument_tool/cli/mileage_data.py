from lib import *

    #自启动距离
def MileageDis_cli(Value,time):
    if Value == '':
        Value = 0
    if time == '':
        time = 0
    vdts({
        'HOST_ICM_TRIP_SINC_IGON_TIME': [float(Value),time],
     })

    # 自启动时间
def MileageTime_cli(Value, time):
    if Value == '':
        Value = 0
    if time == '':
        time = 0
    vdts({
        'HOST_ICM_TRIP_SINC_IGON_TIME': [float(Value), time],
        })


    #启动后百公里能耗
def Distance_cli(energy):
    InputBox('HOST_EAVG_VEHELCCONSP',float(energy))


    #充电后行驶的里程
def AfterChargingDis_cli(Dis,Time):
    if Dis == '':
        Dis = 0
    if Time == '':
        Time = 0
    vdts({
        'HOST_ICM_TRIP_SINC_CHRG_TIME': [float(Dis),Time]
        })

    # 充电后行驶的时间
def AfterChargingTime_cli(Dis,Time):
    if Time == '':
        Time = 0
    if Dis == '':
        Dis = 0
    vdts({
        'HOST_ICM_TRIP_SINC_CHRG_TIME': [float(Dis),Time]
        })

    #总里程
def SumMileage_cli(Value):
    InputBox('HOST_ICM_TOTAL_ODOMETER',float(Value))