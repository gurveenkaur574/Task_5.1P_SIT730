import RPi.GPIO as GPIO
from tkinter import *

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# Define functions to control LEDs
def turn_on_red():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)

def turn_on_green():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)

def turn_on_blue():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)

def exit_program():
    GPIO.cleanup()
    root.destroy()

# Create the GUI
root = Tk()
root.title("LED Controller")

red_button = Radiobutton(root, text="Red", command=turn_on_red)
red_button.pack()

green_button = Radiobutton(root, text="Green", command=turn_on_green)
green_button.pack()

blue_button = Radiobutton(root, text="Blue", command=turn_on_blue)
blue_button.pack()


root.mainloop()

import tkinter as tk
from tkinter import messagebox
import RPi.GPIO as GPIO

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins
led_pins = {
    "Red": 17,
    "Green": 27,
    "Blue": 22
}

# Set up each LED pin as an output
for pin in led_pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Ensure all LEDs are off initially

def turn_on_led(color):
    color = color.capitalize()  # Capitalize the first letter to match dictionary keys
    if color in led_pins:
        for pin in led_pins.values():
            GPIO.output(pin, GPIO.LOW)
        GPIO.output(led_pins[color], GPIO.HIGH)
    else:
        messagebox.showerror("Error", "Invalid color name! Please enter Red, Green, or Blue.")

def on_closing():
    GPIO.cleanup()
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("LED Controller")

# Create radio buttons for LED selection (if you still want them)
led_var = tk.StringVar()
led_var.set("Red")  # Default selection

for color in led_pins.keys():
    tk.Radiobutton(root, text=color, variable=led_var, value=color).pack(anchor=tk.W)

# Create an entry widget for color input
color_label = tk.Label(root, text="Enter LED Color (Red, Green, Blue):")
color_label.pack()

color_entry = tk.Entry(root)
color_entry.pack()

# Create a button to turn on the LED based on the color input
color_button = tk.Button(root, text="Turn On", command=lambda: turn_on_led(color_entry.get()))
color_button.pack()

# Replace the exit button with a proper exit handling using on_closing function
exit_button = tk.Button(root, text="Exit", command=on_closing)
exit_button.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()



