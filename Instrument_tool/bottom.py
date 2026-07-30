from cli.bottom_data import *

bottom = tk.Frame(root,width=1000, height=40,bd=1)
bottom.place(x=0,y=500)
canvas=tk.Canvas(bottom,width=1000,height=40)
canvas.place(x=0,y=0)

bottom_line=canvas.create_line(0,2,1000,2,fill='grey')

#车外温度
def Entry_C():
    i = entry_c.get()
    Env(i)
entry_c = tk.Entry(bottom, validate='key', validatecommand=vcmd, width=3, font=("Arial", 16))
entry_c.place(x=20, y=8)

button = tk.Button(bottom, text='℃', command=Entry_C,bd=1, width=3, height=1)
button.place(x=75, y=8)


    #系统时间

def Entry_Time():
    h = entry_timeh.get()
    m = entry_timem.get()
    SystemTime(h,m)
entry_timeh = tk.Entry(bottom, validate='key', validatecommand=vcmd, width=2, font=("Arial", 16))
entry_timeh.place(x=128, y=8)

entry_timem = tk.Entry(bottom, validate='key', validatecommand=vcmd, width=2, font=("Arial", 16))
entry_timem.place(x=180, y=8)
button = tk.Button(bottom, text=':', command=Entry_Time, width=1,bd=1, height=1)
button.place(x=160, y=8)




    #剩余里程
def Entry_Mileage_smt():
    thread = threading.Thread(target=Entry_Mileage)
    thread.start()
def Entry_Mileage():
    i = entry_mileage.get()
    DSTBAT(i)
entry_mileage = tk.Entry(bottom, validate='key', validatecommand=vcmd, width=5, font=("Arial", 16))
entry_mileage.place(x=310, y=8)
button = tk.Button(bottom, text="km", command=Entry_Mileage_smt,bd=1, width=3, height=1)
button.place(x=380, y=8)


    #剩余电量
def Entry_BMSSOC():
    i = entry_bmssoc.get()
    BmsSoc(i)
entry_bmssoc = tk.Entry(bottom, validate='key', validatecommand=vcmd, width=3, font=("Arial", 16))
entry_bmssoc.place(x=420, y=8)
button = tk.Button(bottom, text="%", command=Entry_BMSSOC, width=2, height=1,bd=1)
button.place(x=470, y=8)


#READY指示灯
button = tk.Button(bottom, text="READY", command=RangeReady, width=6, height=1,bd=1)
button.place(x=700, y=8)

    #挡位
buttons_Gear = ['P','R','N','D']
commands_Gear =[Gear_P,Gear_R,Gear_N,Gear_D]
for i in range(4):
    button = tk.Button(bottom, text=buttons_Gear[i], command=commands_Gear[i], width=4, height=1,bd=1)
    button.place(x=800 + i * 50, y=8)




    #驾驶模式
def DriveMode_smt(e):
    thread = threading.Thread(target=DriveMode)
    thread.start()

def DriveMode():
    Instruction_type = combo_DrivingMode.get()
    DriveMode_cli(Instruction_type)


combo_DrivingMode = Combobox(bottom,state="readonly")
combo_DrivingMode['values'] = ('选择驾驶模式', '标准','节能','运动','舒适','自适应','脱困','弹射','X—PEDAL','极客','车手','个性化','雪地','湿地')
combo_DrivingMode.set('选择驾驶模式')
combo_DrivingMode.bind("<<ComboboxSelected>>", DriveMode_smt)
combo_DrivingMode.place(x=580, y=12, width=100)


    #续航模式
# button = tk.Button(bottom, text="续航模式", command=RangeMode,bd=1, width=8, height=1)
# button.place(x=230, y=8)

def MileageMode_smt(e):
    thread = threading.Thread(target=MileageMode)
    thread.start()

def MileageMode():
    Instruction_type = combo_MileageMode.get()
    MileageMode_cli(Instruction_type)


combo_MileageMode = Combobox(bottom,state="readonly")
combo_MileageMode['values'] = ('续航模式', 'WLTP','CLTC','NEDC','Dynamics')
combo_MileageMode.set('续航模式')
combo_MileageMode.bind("<<ComboboxSelected>>", MileageMode_smt)
combo_MileageMode.place(x=220, y=12, width=80)


