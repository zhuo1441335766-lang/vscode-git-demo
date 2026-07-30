from lib import *

#左侧滑门状态
def LSlideDoor_type_cli(LSlideDoorStatus_type):
    List = {'未知状态': 0, '左门故障': 7, '左门全开': 1, '左门全关': 2, '打开中': 3, '关闭中': 4, '停止': 5}
    vdts({
        'BCM_LSLIDEDOOR_CTRL': List.get(LSlideDoorStatus_type),
    })

#左门热保护
button_PsdlTHERMAL = ButtonClicks()
def PsdlTHERMAL_cli():
    TwoStates(button_PsdlTHERMAL,'PSDL_MOTOR_THERMAL_PROTECT')



# 左门故障
button_PsdlFault = ButtonClicks()
def PsdlFault_cli():
    TwoStates(button_PsdlFault, 'PSDL_SYSTEM_FAULT')

#左侧滑门状态
def RSlideDoor_type_cli(LSlideDoorStatus_type):
    List = {'未知状态': 0, '左门故障': 7, '左门全开': 1, '左门全关': 2, '打开中': 3, '关闭中': 4, '停止': 5}
    vdts({
        'BCM_RSLIDEDOOR_CTRL': List.get(LSlideDoorStatus_type),
    })

#左门热保护
button_PsdrTHERMAL = ButtonClicks()
def PsdrTHERMAL_cli():
    TwoStates(button_PsdrTHERMAL,'PSDR_MOTOR_THERMAL_PROTECT')



# 左门故障
button_PsdrFault = ButtonClicks()
def PsdrFault_cli():
    TwoStates(button_PsdrFault, 'PSDR_SYSTEM_FAULT')


#左鹏翼门
def LSdclDoor_type_cli(status_type):
    List = {'初始态': 0,  '左翼关闭': 1, '左翼打开中': 2, '左翼关闭中': 3, '暂停中': 4, '打开失败': 5,'左翼过热': 6,'左翼故障': 7,}
    vdts({
        'BCM_SDCL_SYS_RUNING_ST': List.get(status_type),
    })

#右鹏翼门
def RSdclDoor_type_cli(status_type):
    List = {'初始态': 0,  '右翼关闭': 1, '右翼打开中': 2, '右翼关闭中': 3, '暂停中': 4, '打开失败': 5,'右翼过热': 6,'右翼故障': 7,}
    vdts({
        'BCM_SDCR_SYS_RUNING_ST': List.get(status_type),
    })