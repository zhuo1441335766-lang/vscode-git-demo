from cli.carState_data import *

    #这里是车况页的创建
carstate = tk.Frame(root,width=400, height=455,)
carstate.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(carstate,width=400,height=455)
canvas2.pack()

# auto_line=canvas2.create_line(20,10,160,10,fill='grey')
# auto_text = canvas2.create_text(200, 10, text='车况相关', fill='grey', font=('微软雅黑', 10))
# Auto_line=canvas2.create_line(240,10,380,10,fill='grey')
    #车况卡片相关


cars_buttons = ['左前门','右前门','前舱盖','左口盖',
                '左后门','右后门','后备箱','右口盖']
cars_commands = [Cars_LFdoor_cli,Cars_RFdoor_cli,Cars_Bonnet_cli,LCharg_Cover_cli,
                 Cars_LRdoor_cli,Cars_RRdoor_cli,Cars_Trunk_cli,RCharg_Cover_cli]

for i in range(8):
    if i > 3:
        button = tk.Button(carstate, text=cars_buttons[i], command=cars_commands[i], width=55, bd=1, height=20,
                           image=pixel, compound="c")
        button.place(x=45 + (i - 4 ) * 90, y=70)
    else:
        button = tk.Button(carstate, text=cars_buttons[i], command=cars_commands[i], width=55, bd=1, height=20,
                           image=pixel, compound="c")
        button.place(x=45 + i * 90, y=20)


    #胎压与胎温设置

def LFT_System_cli():
    Value = entry_LFTP.get()
    LF_Tire_cli(Value)


def RFT_System_cli():
    Value = entry_RFTP.get()
    RF_Tire_cli(Value)


def LRT_System_cli():
    Value = entry_LRTP.get()
    LR_Tire_cli(Value)


def RRT_System_cli():
    Value = entry_RRTP.get()
    RR_Tire_cli(Value)


entry_LFTP = tk.Entry(carstate, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_LFTP.place(x=45, y=120)
entry_RFTP = tk.Entry(carstate, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_RFTP.place(x=225, y=120)
entry_LRTP = tk.Entry(carstate, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_LRTP.place(x=45, y=170)
entry_RRTP = tk.Entry(carstate, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_RRTP.place(x=225, y=170)

tire_buttons = ['左前胎压','右前胎压','左后胎压','右后胎压']
tire_commands = [LFT_System_cli,RFT_System_cli,LRT_System_cli,RRT_System_cli]
for i in range(4):
    if i > 1:
        button = tk.Button(carstate, text=tire_buttons[i], command=tire_commands[i], width=55, bd=1, height=20,
                           image=pixel, compound="c")
        button.place(x=135 + (i - 2) * 180, y=170)
    else:
        button = tk.Button(carstate, text=tire_buttons[i], command=tire_commands[i], width=55, bd=1, height=20,
                           image=pixel, compound="c")
        button.place(x=135 + i * 180, y=120)


def LFTr_System_cli():
    Value = entry_LFTR.get()
    LF_Tyre_cli(Value)

def RFTr_System_cli():
    Value = entry_RFTR.get()
    RF_Tyre_cli(Value)

def LRTr_System_cli():
    Value = entry_LRTR.get()
    LR_Tyre_cli(Value)

def RRTr_System_cli():
    Value = entry_RRTR.get()
    RR_Tyre_cli(Value)

entry_LFTR = tk.Entry(carstate, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_LFTR.place(x=45, y=220)
entry_RFTR = tk.Entry(carstate, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_RFTR.place(x=225, y=220)
entry_LRTR = tk.Entry(carstate, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_LRTR.place(x=45, y=270)
entry_RRTR = tk.Entry(carstate, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_RRTR.place(x=225, y=270)

tyre_buttons = ['左前胎温','右前胎温','左后胎温','右后胎温']
tyre_commands = [LFTr_System_cli,RFTr_System_cli,LRTr_System_cli,RRTr_System_cli]
for i in range(4):
    if i > 1:
        button = tk.Button(carstate, text=tyre_buttons[i], command=tyre_commands[i], width=55, bd=1, height=20,
                           image=pixel, compound="c")
        button.place(x=135 + (i - 2) * 180, y=270)
    else:
        button = tk.Button(carstate, text=tyre_buttons[i], command=tyre_commands[i], width=55, bd=1, height=20,
                           image=pixel, compound="c")
        button.place(x=135 + i * 180, y=220)


    #轮胎状态
tyre_buttons = ['左前轮状态','右前轮状态','左后轮状态','右后轮状态']
tyre_commands = [LF_State_cli,RF_State_cli,LR_State_cli,RR_State_cli]
for i in range(4):

    button = tk.Button(carstate, text=tyre_buttons[i], command=tyre_commands[i], width=55, bd=1, height=20,
                           image=pixel, compound="c")
    button.place(x=45 + i * 90, y=320)

def SuggestedPressure():
    FValue = entry_LFproposal.get()
    RValue = entry_RFproposal.get()
    SuggestedPressure_cli(FValue,RValue)

TireTipLF_text = canvas2.create_text(80, 380, text='建议胎压值', fill='grey', font=('微软雅黑', 10))
entry_LFproposal = tk.Entry(carstate, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_LFproposal.place(x=135, y=370)
TireTip_text = canvas2.create_text(205, 380, text='前轮', fill='grey', font=('微软雅黑', 10))
entry_RFproposal = tk.Entry(carstate, validate='key', validatecommand=vcmd, width=5, font=("Arial", 13))
entry_RFproposal.place(x=225, y=370)
TireTipRF_text = canvas2.create_text(295, 380, text='后轮', fill='grey', font=('微软雅黑', 10))
button = tk.Button(carstate, text='发送', command=SuggestedPressure, width=46, bd=1, height=20,
                   image=pixel, compound="c")
button.place(x=320, y=367)


FuelCap = tk.Button(carstate, text='油箱盖开关', command=FuelCap_cli, width=70, bd=1, height=20,
                           image=pixel, compound="c")
FuelCap.place(x=45, y=417)