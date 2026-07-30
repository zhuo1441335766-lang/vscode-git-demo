from cli.QnxBottom_data import *


Qnxbottom = tk.Frame(root,width=1000, height=40,bd=1)
Qnxbottom.place(x=0,y=500)
canvas=tk.Canvas(Qnxbottom,width=1000,height=40)
canvas.place(x=0,y=0)

bottom_line=canvas.create_line(0,2,1000,2,fill='grey')

    #续航模式
button = tk.Button(Qnxbottom, text="续航模式", command=RangeMode,bd=1, width=8, height=1)
button.place(x=230, y=8)

    #READY
button = tk.Button(Qnxbottom, text="READY", command=RangeReady, width=6, height=1,bd=1)
button.place(x=700, y=8)

    #挡位
buttons_Gear = ['P','R','N','D']
commands_Gear =[Gear_P,Gear_R,Gear_N,Gear_D]
for i in range(4):
    button = tk.Button(Qnxbottom, text=buttons_Gear[i], command=commands_Gear[i], width=4, height=1,bd=1)
    button.place(x=800 + i * 50, y=8)

    #剩余里程
def Entry_Mileage():
    i = entry_mileage.get()
    DSTBAT(i)
entry_mileage = tk.Entry(Qnxbottom, validate='key', validatecommand=vcmd, width=5, font=("Arial", 16))
entry_mileage.place(x=310, y=8)
button = tk.Button(Qnxbottom, text="km", command=Entry_Mileage,bd=1, width=3, height=1)
button.place(x=380, y=8)

    #车外温度
def Entry_C():
    i = entry_c.get()
    Env(i)
entry_c = tk.Entry(Qnxbottom, validate='key', validatecommand=vcmd, width=3, font=("Arial", 16))
entry_c.place(x=20, y=8)

button = tk.Button(Qnxbottom, text='℃', command=Entry_C,bd=1, width=3, height=1)
button.place(x=75, y=8)

    #时间
def Entry_Time():
    h = entry_timeh.get()
    m = entry_timem.get()
    SystemTime(h,m)
entry_timeh = tk.Entry(Qnxbottom, validate='key', validatecommand=vcmd, width=2, font=("Arial", 16))
entry_timeh.place(x=130, y=8)
entry_timem = tk.Entry(Qnxbottom, validate='key', validatecommand=vcmd, width=2, font=("Arial", 16))
entry_timem.place(x=180, y=8)
button = tk.Button(Qnxbottom, text=':', command=Entry_Time, width=1,bd=1, height=1)
button.place(x=160, y=8)

    #电池百分比
def Entry_BMSSOC():
    i = entry_bmssoc.get()
    BmsSoc(i)
entry_bmssoc = tk.Entry(Qnxbottom, validate='key', validatecommand=vcmd, width=3, font=("Arial", 16))
entry_bmssoc.place(x=420, y=8)
button = tk.Button(Qnxbottom, text="%", command=Entry_BMSSOC, width=2, height=1,bd=1)
button.place(x=470, y=8)

#     #驾驶模式
# button = tk.Button(Qnxbottom, text="驾驶模式", command=DriveMode, width=8, height=1,bd=1)
# button.place(x=620, y=8)

    #驾驶模式
def DriveMode_smt(e):
    thread = threading.Thread(target=DriveMode)
    thread.start()

def DriveMode():
    Instruction_type = combo_SwitchLanguage.get()
    DriveMode_cli(Instruction_type)


combo_SwitchLanguage = Combobox(Qnxbottom,state="readonly")
combo_SwitchLanguage['values'] = ('选择驾驶模式', '标准','节能','运动','舒适','自适应','脱困','弹射','X—PEDAL','极客','车手')
combo_SwitchLanguage.set('选择驾驶模式')
combo_SwitchLanguage.bind("<<ComboboxSelected>>", DriveMode_smt)
combo_SwitchLanguage.place(x=580, y=12, width=100)