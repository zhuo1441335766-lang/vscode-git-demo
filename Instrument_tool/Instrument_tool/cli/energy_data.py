from lib import *

    #百公里能耗
def Energy100KM_cli(Value):
    if Value == '':
        pass
    else:
        vdts({
            'HOST_EAVG_VEHELCCONSP': float(Value),
        })

    #100m能耗
def Energy100M_cli(Value):
    if Value == '':
        pass
    else:
        vdts({
            'HOST_EENGCOST_P100M': float(Value),
        })

    #瞬时能耗
def EnergyPWR_cli(Value):
    if Value == '':
        pass
    else:
        vdts({
            'HOST_VCU_VEH_PWR_DISP': float(Value),
        })

    #可用功率
def EnergyAVAIL_cli(Value):
    if Value == '':
        pass
    else:
        vdts({
            'HOST_RES_AVAIL_POWER': float(Value),
        })

    #快速随机生成一组百米能耗

def Produce100mEnergy_cli():
    for i in range(25):
        energy100m = random.randint(-20,40)
        vdts({
            'HOST_EENGCOST_P100M': energy100m,
        })