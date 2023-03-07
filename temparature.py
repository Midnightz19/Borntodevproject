from tkinter import *
import tkinter as tk


class TemperatureConverterGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("แปลงอุณหภูมิ ")
        self.window.geometry("420x410")
        #ตารางรับค่า-แปลงค่าอุณหภูมิ
        self.celsius_label = tk.Label(self.window, text="องศาเซลเซียส (°C) ")
        self.celsius_label.grid(row=0, column=0)
        self.fahrenheit_label = tk.Label(self.window, text="ฟาเรนไฮต์ (°F) ")
        self.fahrenheit_label.grid(row=1, column=0)
        self.fahrenheit_label = tk.Label(self.window, text="เควิน (°K) ")
        self.fahrenheit_label.grid(row=2, column=0)
        self.celsius_entry = tk.Entry(self.window)
        self.celsius_entry.grid(row=0, column=1)
        self.fahrenheit_entry = tk.Entry(self.window)
        self.fahrenheit_entry.grid(row=1, column=1)
        self.kelvin_entry = tk.Entry(self.window)
        self.kelvin_entry.grid(row=2, column=1)
        #ปุ่มแปลงค่า
        self.convert_button = tk.Button(self.window, text="แปลงค่า", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=1)
        #ปุ่มล้างค่า
        self.reset_button = tk.Button(self.window, text="ล้างค่า", command=self.reset)
        self.reset_button.grid(row=3, column=1, columnspan=1)
        #ใส่รูป
        self.image = tk.PhotoImage(file="temp.png")
        self.image_label =tk.Label(self.window, image=self.image)
        self.image_label.grid(row=4,column=0 ,columnspan=2)

        self.window.mainloop()
    #ฟังก์ชั่นอุณหภูมิ
    def convert(self):

        celsius = float(self.celsius_entry.get())
        #แปลงค่าองศาเซลเซียสเป็นองศาฟาเรนไฮต์
        fahrenheit = celsius * 9/5 + 32
        self.fahrenheit_entry.delete(0, tk.END)
        self.fahrenheit_entry.insert(0, fahrenheit)
         #แปลงค่าองศาเซลเซียสเป็นเคลวิน
        kelvin = celsius + 273
        self.kelvin_entry.delete(0, tk.END)
        self.kelvin_entry.insert(0, kelvin)
    #ฟังก์ชั่นปุ่มรีเซท
    def reset(self):
        self.celsius_entry.delete(0, tk.END)
        self.fahrenheit_entry.delete(0, tk.END)
        self.kelvin_entry.delete(0, tk.END)

app = TemperatureConverterGUI()
