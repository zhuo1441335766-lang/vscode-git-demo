from cli.energy_data import *
from ApkLog import textIns

    #这里是能耗页的创建
energy = tk.Frame(root,width=400, height=455,)
energy.place(x=0,y=40)

#创建画布用于制作线条以及编辑文字
canvas2=tk.Canvas(energy,width=400,height=455)
canvas2.pack()

# auto_line=canvas2.create_line(20,10,160,10,fill='grey')
# auto_text = canvas2.create_text(200, 10, text='能耗相关', fill='grey', font=('微软雅黑', 10))
# Auto_line=canvas2.create_line(240,10,380,10,fill='grey')

def HundredKM_Energy():
    Value = entry_energy100km.get()
    Energy100KM_cli(Value)

def HundredM_Energy():
    Value = entry_energy100m.get()
    Energy100M_cli(Value)

def PWREnergy():
    Value = entry_energypwr.get()
    EnergyPWR_cli(Value)

def AVAILEnergy():
    Value = entry_energavail.get()
    EnergyAVAIL_cli(Value)

entry_energy100km = tk.Entry(energy, validate='key', validatecommand=vcmd, width=6, font=("Arial", 13))
entry_energy100km.place(x=100, y=30)
entry_energy100m = tk.Entry(energy, validate='key', validatecommand=vcmd, width=6, font=("Arial", 13))
entry_energy100m.place(x=100, y=80)
entry_energypwr = tk.Entry(energy, validate='key', validatecommand=vcmd, width=6, font=("Arial", 13))
entry_energypwr.place(x=100, y=130)
entry_energavail = tk.Entry(energy, validate='key', validatecommand=vcmd, width=6, font=("Arial", 13))
entry_energavail.place(x=100, y=180)

tyre_buttons = ['百里能耗','百米能耗','瞬时能耗','可用功率']
tyre_commands = [HundredKM_Energy,HundredM_Energy,PWREnergy,AVAILEnergy]
for i in range(4):
    button = tk.Button(energy, text=tyre_buttons[i], command=tyre_commands[i], width=55, bd=1, height=20,image=pixel, compound="c")
    button.place(x=250, y=30 + i * 50)

def Thread_Energy_random():
    thread = threading.Thread(target=Produce100mEnergy_cli)
    thread.start()
    textIns.config(state='normal')
    textIns.insert('end', '\n' + System_Time() + "\n已随机发送25个百米能耗")
    textIns.config(state='disabled')
    textIns.yview_moveto(1)

button_Observatory = tk.Button(energy, text='随机模拟一组自启动能耗', command=Thread_Energy_random,bd=1, width=20, height=1)
button_Observatory.place(x=120, y=230)