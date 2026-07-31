from cli.autodrive_data import *

    #这里是主动安全与预警页的创建
autodrive = tk.Frame(root,width=400, height=455,)
autodrive.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(autodrive,width=400,height=455)
canvas2.pack()

# auto_line=canvas2.create_line(20,10,160,10,fill='grey')
# auto_text = canvas2.create_text(200, 10, text='充电相关', fill='grey', font=('微软雅黑', 10))
# Auto_line=canvas2.create_line(240,10,380,10,fill='grey')


Auto_List = ['RAEB(EU)','AEB','后碰撞预警','DOW左','DOW右']
Auto_cli = [RAEB_cli,AEB_cli,Rcw_cli,DowL_cli,DowR_cli]

for i in range(5):
    button = tk.Button(autodrive, text=Auto_List[i], command=Auto_cli[i], width=60, bd=1, height=20,image=pixel, compound="c")
    button.place(x=25 + i * 75, y=30)


    #雷达预警方位

Radar_List =['左侧前','左前','左前中','右前中','右前','右侧前',
             '左侧后','左后','左后中','右后中','右后','右侧后']
Radar_cli =[FSL_cli,FL_cli,FCL_cli,FCR_cli,FR_cli,FSR_cli,
             RSL_cli,RL_cli,RCL_cli,RCR_cli,RR_cli,RSR_cli]
Radar_name = ['FSL','FL','FCL','FCR','FR','FSR',
              'RSL','RL','RCL','RCR','RR','RSR']
Radar_name2 = ['fsl','fl','fcl','fcr','fr','fsr',
              'rsl','rl','rcl','rcr','rr','rsr']
def Radar_information():
    for i in range(12):
        Radar_name2[i] = (Radar_name[i]).get()
        Radar_cli[i](Radar_name2[i])

#多线程处理，防止卡顿
def Thread_Radar():
    thread = threading.Thread(target=Radar_information)
    thread.start()

for i in range(0,12):
    if i > 5:
        Radar_name[i] = tk.Entry(autodrive, validate='key', validatecommand=vcmd, width=3, font=("Arial", 13))
        Radar_name[i].place(x=35 + (i -6) * 60, y=200)
        Radar_name2[i] = canvas2.create_text(45 + (i-6) * 60, 185, text=Radar_List[i], fill='grey', font=('微软雅黑', 10))

    else:
        Radar_name[i] = tk.Entry(autodrive, validate='key', validatecommand=vcmd, width=3, font=("Arial", 13))
        Radar_name[i].place(x=35 + i * 60, y=140)
        Radar_name2[i] = canvas2.create_text(45 + i * 60, 125, text=Radar_List[i], fill='grey', font=('微软雅黑', 10))

radar_text = canvas2.create_text(85 , 90, text='雷达方位预警距离', fill='grey', font=('微软雅黑', 10))
button_radar = tk.Button(autodrive, text='发送', command=Thread_Radar,bd=1, width=8, height=1)
button_radar.place(x=300, y=250)

#     #雷达预警距离   OS5.0之前适用，现在已废弃
# def Radar_Gap():
#     FGap = RadarFGap.get()
#     RGap = RadarRGap.get()
#     AlarmFront_cli(FGap,RGap)


# RadarGap_text = canvas2.create_text(155 , 300, text='雷达预警距离(适用于OS5.0之前的版本)', fill='grey', font=('微软雅黑', 10))
# RadarFGap_text = canvas2.create_text(65 , 340, text='前向距离', fill='grey', font=('微软雅黑', 10))
# RadarRGap_text = canvas2.create_text(245 , 340, text='后向距离', fill='grey', font=('微软雅黑', 10))
# RadarFGap = tk.Entry(autodrive, validate='key', validatecommand=vcmd, width=4, font=("Arial", 13))
# RadarFGap.place(x=105, y=330)
# RadarRGap = tk.Entry(autodrive, validate='key', validatecommand=vcmd, width=4, font=("Arial", 13))
# RadarRGap.place(x=285, y=330)
# RadarFGapCm_text = canvas2.create_text(165 , 340, text='cm', fill='grey', font=('微软雅黑', 10))
# RadarRGapCm_text = canvas2.create_text(345 , 340, text='cm', fill='grey', font=('微软雅黑', 10))
# button_radargap = tk.Button(autodrive, text='发送', command=Radar_Gap,bd=1, width=8, height=1)
# button_radargap.place(x=295, y=375)

