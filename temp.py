import tkinter as tk
from tkinter import messagebox

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Function to convert temperature
def convert_temperature():
    try:
        value = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "C":
            f = celsius_to_fahrenheit(value)
            k = celsius_to_kelvin(value)
            result_label.config(text=f"{value}°C = {f:.2f}°F = {k:.2f}K")
        elif unit == "F":
            c = fahrenheit_to_celsius(value)
            k = fahrenheit_to_kelvin(value)
            result_label.config(text=f"{value}°F = {c:.2f}°C = {k:.2f}K")
        elif unit == "K":
            c = kelvin_to_celsius(value)
            f = kelvin_to_fahrenheit(value)
            result_label.config(text=f"{value}K = {c:.2f}°C = {f:.2f}°F")
        else:
            messagebox.showerror("Error", "Invalid unit selected!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")

# Input Fields
tk.Label(root, text="Enter Temperature:").pack(pady=5)
entry_temp = tk.Entry(root)
entry_temp.pack(pady=5)

# Unit Selection
tk.Label(root, text="Select Unit:").pack(pady=5)
unit_var = tk.StringVar(value="C")
tk.Radiobutton(root, text="Celsius (°C)", variable=unit_var, value="C").pack()
tk.Radiobutton(root, text="Fahrenheit (°F)", variable=unit_var, value="F").pack()
tk.Radiobutton(root, text="Kelvin (K)", variable=unit_var, value="K").pack()

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run GUI
root.mainloop()
