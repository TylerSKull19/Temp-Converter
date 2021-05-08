#csc102 - Class 8 
# F to C 
#Tyler Smith
# 4/9/2021

from tkinter import *

class TemperatureConversion:
    def __init__(self):
        window = Tk()
        window.title("Fah -> cel")
        
        Label(window,text="Fahrenheit:").grid(row=1,column=1)
        
        self.fah_entry = DoubleVar()
        Entry(window,textvariabl=self.fah_entry).grid(row=1,column=2,)
        Label(window,text="Celsius").grid(row=2,column=1)
        
        self.celsius_label = Label(
            window, text="(none)")
        self.celsius_label.grid(row=2,column=2)
        
        Button(window, text="convert",
               command=self.fah2cel).grid(row = 3, column =1, columnspan = 2)
        
        ###PART3###
        Label(window, text="Common Temperatures").grid(row=4,column =1, columnspan = 2)
        
        self.common_tmp = DoubleVar()
        self.common_tmp.set(212)
        
        Radiobutton(window, text="Freezing Point",
                    variable=self.common_tmp, value = 32).grid(row=7,column =1, columnspan = 2)
        Radiobutton(window, text="Boiling Point",
                    variable=self.common_tmp, value = 212).grid(row=8,column =1, columnspan = 2)
        Radiobutton(window, text="Room Temperature",
                    variable=self.common_tmp, value = 72).grid(row=9,column =1, columnspan = 2)
        
        Button(window, text="Show Temperature",
               command=self.common_temp_handler).grid(row=10,column =1, columnspan = 2)
        
        
        window.mainloop()
        
    def common_temp_handler(self):
        common_tmp = self.common_tmp.get()
        self.fah_entry.set(common_tmp)
        self.fah2cel.pack()
        
    def fah2cel(self):
        print("Button clicked")
        f = self.fah_entry.get()
        c = (5/9) * (f-32)
        self.celsius_label["text"] = str(c)
        
        
app = TemperatureConversion()