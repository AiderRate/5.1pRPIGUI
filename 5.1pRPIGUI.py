import tkinter as tk
import RPi.GPIO as GPIO

#Define LED GPIO pins
RED_PIN = 18
GREEN_PIN = 12
BLUE_PIN = 17

#Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

#Function to turn off LEDs
def turn_off_all():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)

#Function to turn on selected LEDs
def turn_on_led(led_pin):
    turn_off_all()
    GPIO.output(led_pin, GPIO.HIGH)
    
#Create GUI
def create_gui():
    root = tk.Tk()
    root.title("LED Control")
    
    #function to handle radio button click
    def on_radio_button_click(led_pin):
        turn_on_led(led_pin)
    
    #Create radio buttons
    red_button = tk.Radiobutton(root, text="Red", command=lambda: on_radio_button_click(RED_PIN))
    red_button.pack()
    green_button = tk.Radiobutton(root, text="Green", command=lambda: on_radio_button_click(GREEN_PIN))
    green_button.pack()
    blue_button = tk.Radiobutton(root, text="Blue", command=lambda: on_radio_button_click(BLUE_PIN))
    blue_button.pack()
    
    #Create exit button
    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack()
    root.mainloop()
    
if __name__ == "__main__":
    create_gui()
