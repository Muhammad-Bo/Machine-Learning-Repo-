try:  # Support For Python 3 & 2
    import tkinter
except ImportError:
    import Tkinter as tkinter
import os

mainWindow = tkinter.Tk()
mainWindow.title("Grid Demo For UT")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 7

label = tkinter.Label(mainWindow, text="Tkinter Demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('C:/Windows/System32'):
    fileList.insert(tkinter.END, zone) # End entry must be added to ODF
lisScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
lisScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
fileList['yscrollcommand'] = lisScroll.set

lisScroll2 = tkinter.Scrollbar(mainWindow, orient=tkinter.HORIZONTAL, command=fileList.xview)
lisScroll2.grid(row=1, column=0, sticky='swe', rowspan=2)
fileList['xscrollcommand'] = lisScroll2.set

# Frame + Radio Buttons
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')
radioValue = tkinter.IntVar()
radioValue.set(3)
r1 = tkinter.Radiobutton(optionFrame, text="FileName", value=1, variable=radioValue)
r2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=radioValue)
r3 = tkinter.Radiobutton(optionFrame, text="TimeStamp", value=3, variable=radioValue)
r1.grid(row=0, column=0, sticky='w')
r2.grid(row=1, column=0, sticky='w')
r3.grid(row=2, column=0, sticky='w')

# Result Section

resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Time
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')

hourSpinner = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0, 60)))
secondSpinner = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0, 60)))
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)

# Padding
timeFrame['padx'] = 26

# Date Frame
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
dayLabel.grid(row=0, column=0, stick="w")
monthLabel.grid(row=0, column=1, stick="w")
yearLabel.grid(row=0, column=2, stick="w")
# Date Spin

daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=12)
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2020)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# Bts

okButton = tkinter.Button(mainWindow, text='Ok')
cancelButton = tkinter.Button(mainWindow, text="Quit", command=mainWindow.quit)  # No()
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()

# print(radioValue.get())