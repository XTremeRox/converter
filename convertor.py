#Made by Ramswaroop Soren for GCI-2014
#Error proof code :)
#Features- clear button,images in button for good look, scientific notation automated and more...
from tkinter import*
from tkinter import ttk
import math
window = Tk()
window.wm_iconbitmap('images\\logo.ico')
window.geometry('480x300+50+100')
window.resizable(False, False)
window.title('Data Unit Convertor')
window.option_add('*tearOff',False)
menubar = Menu(window)
window.config(menu = menubar)
close_image=PhotoImage(file='images\\close.gif').subsample(10,10)
def about_window():
    aboutwindow = Toplevel(window)
    aboutwindow.title('About')
    frame = ttk.Frame(aboutwindow)
    frame.pack()
    ttk.Label(aboutwindow, text = 'Made by Ramswaroop Soren').place(x=10,y=20)
    frame.config(height = 100, width = 200)
    frame.config(relief = RIDGE)
    def closeabout():
        aboutwindow.destroy()
    closebutton_about=ttk.Button(frame, text = 'Close', command=closeabout)
    closebutton_about.place(x=50,y=50)
    closebutton_about.config(image = close_image,compound = LEFT)

def bytes_():
    input_value=entryfield.get()
    to=combobox2.get()
    if(to=='Bytes'):
        output_value=(float(input_value))*1.0
    elif(to=='KiloByte(KB)'):
        output_value=(float(input_value))*math.pow(1024,-1)
    elif(to=='MegaByte(MB)'):
        output_value=(float(input_value))*math.pow(1024,-2)
    elif(to=='GigaByte(GB)'):
        output_value=(float(input_value))*math.pow(1024,-3)
    elif(to=='TeraByte(TB)'):
        output_value=(float(input_value))*math.pow(1024,-4)
    elif(to=='PetaByte(PB)'):
        output_value=(float(input_value))*math.pow(1024,-5)
    elif(to=='ExaByte(EB)'):
        output_value=(float(input_value))*math.pow(1024,-6)
    else:
        messagebox.showinfo(title="Error", message="Enter/Select a valid Unit")
    entryfield2.insert(0,output_value)

def kilobyte():
    input_value=entryfield.get()
    to=combobox2.get()
    if(to=='Bytes'):
        output_value=(float(input_value))*math.pow(1024,1)
    elif(to=='KiloByte(KB)'):
        output_value=(float(input_value))*1.0
    elif(to=='MegaByte(MB)'):
        output_value=(float(input_value))*math.pow(1024,-1)
    elif(to=='GigaByte(GB)'):
        output_value=(float(input_value))*math.pow(1024,-2)
    elif(to=='TeraByte(TB)'):
        output_value=(float(input_value))*math.pow(1024,-3)
    elif(to=='PetaByte(PB)'):
        output_value=(float(input_value))*math.pow(1024,-4)
    elif(to=='ExaByte(EB)'):
        output_value=(float(input_value))*math.pow(1024,-5)
    else:
        messagebox.showinfo(title="Error", message="Enter/Select a valid Unit")
    entryfield2.insert(0,output_value)

def megabyte():
    input_value=entryfield.get()
    to=combobox2.get()
    if(to=='Bytes'):
        output_value=(float(input_value))*math.pow(1024,2)
    elif(to=='KiloByte(KB)'):
        output_value=(float(input_value))*math.pow(1024,1)
    elif(to=='MegaByte(MB)'):
        output_value=(float(input_value))*1.0
    elif(to=='GigaByte(GB)'):
        output_value=(float(input_value))*math.pow(1024,-1)
    elif(to=='TeraByte(TB)'):
        output_value=(float(input_value))*math.pow(1024,-2)
    elif(to=='PetaByte(PB)'):
        output_value=(float(input_value))*math.pow(1024,-3)
    elif(to=='ExaByte(EB)'):
        output_value=(float(input_value))*math.pow(1024,-4)
    else:
        messagebox.showinfo(title="Error", message="Enter/Select a valid Unit")
    entryfield2.insert(0,output_value)

def gigabyte():
    input_value=entryfield.get()
    to=combobox2.get()
    if(to=='Bytes'):
        output_value=(float(input_value))*math.pow(1024,3)
    elif(to=='KiloByte(KB)'):
        output_value=(float(input_value))*math.pow(1024,2)
    elif(to=='MegaByte(MB)'):
        output_value=(float(input_value))*math.pow(1024,1)
    elif(to=='GigaByte(GB)'):
        output_value=(float(input_value))*1.0
    elif(to=='TeraByte(TB)'):
        output_value=(float(input_value))*math.pow(1024,-1)
    elif(to=='PetaByte(PB)'):
        output_value=(float(input_value))*math.pow(1024,-2)
    elif(to=='ExaByte(EB)'):
        output_value=(float(input_value))*math.pow(1024,-3)
    else:
        messagebox.showinfo(title="Error", message="Enter/Select a valid Unit")
    entryfield2.insert(0,output_value)

def terabyte():
    input_value=entryfield.get()
    to=combobox2.get()
    if(to=='Bytes'):
        output_value=(float(input_value))*math.pow(1024,4)
    elif(to=='KiloByte(KB)'):
        output_value=(float(input_value))*math.pow(1024,3)
    elif(to=='MegaByte(MB)'):
        output_value=(float(input_value))*math.pow(1024,2)
    elif(to=='GigaByte(GB)'):
        output_value=(float(input_value))*math.pow(1024,1)
    elif(to=='TeraByte(TB)'):
        output_value=(float(input_value))*1.0
    elif(to=='PetaByte(PB)'):
        output_value=(float(input_value))*math.pow(1024,-1)
    elif(to=='ExaByte(EB)'):
        output_value=(float(input_value))*math.pow(1024,-2)
    else:
        messagebox.showinfo(title="Error", message="Enter/Select a valid Unit")
    entryfield2.insert(0,output_value)

def petabyte():
    input_value=entryfield.get()
    to=combobox2.get()
    if(to=='Bytes'):
        output_value=(float(input_value))*math.pow(1024,5)
    elif(to=='KiloByte(KB)'):
        output_value=(float(input_value))*math.pow(1024,4)
    elif(to=='MegaByte(MB)'):
        output_value=(float(input_value))*math.pow(1024,3)
    elif(to=='GigaByte(GB)'):
        output_value=(float(input_value))*math.pow(1024,2)
    elif(to=='TeraByte(TB)'):
        output_value=(float(input_value))*math.pow(1024,1)
    elif(to=='PetaByte(PB)'):
        output_value=(float(input_value))*1.0
    elif(to=='ExaByte(EB)'):
        output_value=(float(input_value))*math.pow(1024,-1)
    else:
        messagebox.showinfo(title="Error", message="Enter/Select a valid Unit")
    entryfield2.insert(0,output_value)

def exabyte():
    input_value=entryfield.get()
    to=combobox2.get()
    if(to=='Bytes'):
        output_value=(float(input_value))*math.pow(1024,6)
    elif(to=='KiloByte(KB)'):
        output_value=(float(input_value))*math.pow(1024,5)
    elif(to=='MegaByte(MB)'):
        output_value=(float(input_value))*math.pow(1024,4)
    elif(to=='GigaByte(GB)'):
        output_value=(float(input_value))*math.pow(1024,3)
    elif(to=='TeraByte(TB)'):
        output_value=(float(input_value))*math.pow(1024,2)
    elif(to=='PetaByte(PB)'):
        output_value=(float(input_value))*math.pow(1024,1)
    elif(to=='ExaByte(EB)'):
        output_value=(float(input_value))*1.0
    else:
        messagebox.showinfo(title="Error", message="Enter/Select a valid Unit")
    entryfield2.insert(0,output_value)

def checkthenconvert():
    if(len(entryfield.get())==0):
        messagebox.showinfo(title="Error", message="Enter Something in Value")
    elif((entryfield.get()).isnumeric()):
        convert()
    else:
         messagebox.showinfo(title="Error", message="Enter a valid Numeric Value")
    
def convert():
    entryfield2.delete(0,END)
    from_=combobox.get()
    if(from_=='Bytes'):
        bytes_()
    elif(from_=='KiloByte(KB)'):
        kilobyte()
    elif(from_=='MegaByte(MB)'):
        megabyte()
    elif(from_=='GigaByte(GB)'):
        gigabyte()
    elif(from_=='TeraByte(TB)'):
        terabyte()
    elif(from_=='PetaByte(PB)'):
        petabyte()
    elif(from_=='ExaByte(EB)'):
        exabyte()
    else:
        messagebox.showinfo(title="Error", message="Enter/Select a Valid Unit")

def clearall():
    entryfield.delete(0,END)
    entryfield2.delete(0,END)

about = Menu(menubar)
menubar.add_cascade(menu = about, label = "About")
about.add_command(label = 'About Convertor', command = about_window)
ttk.LabelFrame(window, height = 260, width = 220, text = 'From').place(x=10,y=1)
ttk.LabelFrame(window, height = 260, width = 220, text = 'To').place(x=250,y=1)
ttk.Label(window, text="Unit").place(x=30, y=70)
ttk.Label(window, text="Unit").place(x=265, y=70)
from_ = StringVar()
combobox = ttk.Combobox(window, textvariable = from_)
combobox.place(x=60, y=70)
combobox.set('Select from Dropdown')
combobox.config(values = ('Bytes','KiloByte(KB)','MegaByte(MB)','GigaByte(GB)','TeraByte(TB)','PetaByte(PB)','ExaByte(EB)'))
arrow = PhotoImage(file = 'images\\arrow.gif').subsample(10,10)
ttk.Label(window, image=arrow).place(x=220,y=20)
to=StringVar()
combobox2=ttk.Combobox(window, textvariable = to)
combobox2.place(x=300, y=70)
combobox2.set('Select from Dropdown')
combobox2.config(values = ('Bytes','KiloByte(KB)','MegaByte(MB)','GigaByte(GB)','TeraByte(TB)','PetaByte(PB)','ExaByte(EB)'))
convert_image=PhotoImage(file='images\\convert_button.gif').subsample(10,10)
entryfield2=ttk.Entry(window, width=30)
entryfield2.place(x=270,y=150)
button=ttk.Button(window, text = 'Convert',command=checkthenconvert)
button.place(x=70, y=200)
button.config(image = convert_image,compound = LEFT)
close_button=ttk.Button(window, text = 'Close', command = lambda:window.destroy())
close_button.config(image = close_image,compound = LEFT)
close_button.place(x=300, y=200)
clear_button=ttk.Button(window, command = clearall)
clear_image = PhotoImage(file = 'images\\clear.gif').subsample(20,20)
clear_button.config(image = clear_image)
clear_button.place(x=215, y=140)
ttk.Label(window, text="Value:").place(x=30, y=150)
ttk.Label(window, text="Result:").place(x=270, y=130)
entryfield=ttk.Entry(window, width=20)
entryfield.place(x=70,y=150)
