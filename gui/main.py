# Following tutorial at https://likegeeks.com/python-gui-examples-tkinter-tutorial/

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to my training app")
window.geometry('750x500')

# label example
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
#lbl.pack(side=LEFT) #https://www.tutorialspoint.com/python/tk_pack.htm

# textbox entry example
txt = Entry(window, width=30)
txt.grid(column=0, row=1)
txt.focus()
#txt.pack(side=LEFT)

# button example
def button_clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)


btn = Button(window, text="Click Me", command=button_clicked)
btn.grid(column=1, row=1)
#btn.pack(side=LEFT)

#  combobox example
def selected(event=None):
    cmbsel = combo.get()
    lbl.configure(text=cmbsel)

combo = Combobox(window)
combo['values'] = (1,2,3,4,5,"Text")
combo.grid(column=0, row=2)
combo.bind('<<ComboboxSelected>>', selected)
#combo.pack(side=LEFT)

# checkbox example

def checked(event=None):
    lbl.configure(text=str(chk_state.get()))

chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(window, text='Choose', var=chk_state, command=checked)
chk.grid(column=0, row=3)
#chk.pack(side=LEFT)

# radiobutton example

def radio_clicked():
    lbl.configure(text=radio_selected.get())

radio_selected = IntVar()
rad1 = Radiobutton(window, text='First', value=1, variable=radio_selected, command=radio_clicked)
rad2 = Radiobutton(window, text='Second', value=2, variable=radio_selected, command=radio_clicked)
rad3 = Radiobutton(window, text='Third', value=3, variable=radio_selected, command=radio_clicked)
rad1.grid(column=0, row=4)
rad2.grid(column=0, row=5)
rad3.grid(column=0, row=6)

# text area example

from tkinter import scrolledtext

txtbox = scrolledtext.ScrolledText(window, width=40, height=10)
txtbox.insert(INSERT,'Sample pre-filled text')
#txtbox.delete(1.0,END) # sample of clearing textbox
txtbox.grid(column=0, row=7)

# messagebox example

from tkinter import messagebox

def msgbtn_clicked():
    messagebox.showinfo('Info Title','Info Content')
    #messagebox.showwarning('Warning Title','Warning Content')
    #messagebox.showerror('Error Title','Error Content')

btn = Button(window, text='Click here for messagebox', command=msgbtn_clicked)
btn.grid(column=0, row=8)

# dialog boxes prompting for user input

def questionbtn_clicked():
    res = messagebox.askyesnocancel("Question Title","Question Content")
    lbl.configure(text=res)

btn1 = Button(window, text='Click here to be asked', command=questionbtn_clicked)
btn1.grid(column=0, row=9)
#res = messagebox.askquestion("Question Title","Question Content")
#res = messagebox.askyesno("Question Title","Question Content")
#res = messagebox.askyesnocancel("Question Title","Question Content")
#res = messagebox.askokcancel("Question Title","Question Content")
#res = messagebox.askretrycancel("Question Title","Question Content")

# spinbox example

def spin_changed():
    lbl.configure(text=var.get())

var = IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var, command=spin_changed)
#spin = Spinbox(window, values=(3, 8, 11), width=5)
spin.grid(column=0, row=10)

# progressbar example

from tkinter.ttk import Progressbar

bar = Progressbar(window, length=500)
bar['value'] = 70 # 70 means 70%
bar.grid(column=0, row=11)

# style Progressbar

style = Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar2 = Progressbar(window, length=500, style='black.Horizontal.TProgressbar')
bar2['value'] = 70
bar2.grid(column=0, row=12)

# filedialog

from tkinter import filedialog

# the filetypes parameter is optional to filter by extensions
#file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("All files","*.*")))
#lbl.configure(text=file)
#files = filedialog.askopenfilenames()

# directory

#dir = filedialog.askdirectory()
#lbl.configure(text=dir)

# menu bar

from tkinter import Menu

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='New', command=msgbtn_clicked)
#new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

# tab control (Notebook)

tab_control = Notebook(window)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
lbl1 = Label(tab1, text='label1', padx=5, pady=5)
lbl1.grid(column=0, row=14)
lbl2 = Label(tab2, text='label2')
lbl2.grid(column=1, row=14)
#tab_control.pack(expand=1, fill='both')
tab_control.grid(column=0, row=13)

window.mainloop()
