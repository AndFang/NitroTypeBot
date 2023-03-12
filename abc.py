from selenium import webdriver
import keyboard
import time
import tkinter as tk
import customtkinter as ctk
from threading import Thread
import random

# pip install selenium, keyboard, tk, pyinstaller, customtkinter

global AUTO
global RUN
global TIME
global driver
global u
global p

AUTO = False
RUN = False
TIME = 0.1
driver = None

times = dict()
times["0.0"] = 0
times["0.1"] = 0.01
times["0.2"] = 0.1
times["0.3"] = 0.25
times["0.4"] = 0.5
times["0.5"] = 1

def botalgo():
    global driver
    global AUTO
    global RUN
    global TIME
    global u
    global p

    # Scrape the race characters
    while (RUN):
        if AUTO:
            try:
                result = driver.find_element("xpath", "//div[@class='raceResults-titles']")
                time.sleep(3)
                driver.get("https://www.nitrotype.com/race")
            except:
                pass
        try:
            error = driver.find_element("xpath", "//span[@class='dash-letter is-incorrect']").text
            keyboard.write(error)
        except:
            pass
        try:
            letter = driver.find_element("xpath", "//span[@class='dash-letter is-waiting']").text
            keyboard.write(letter, delay=TIME + random.uniform(TIME / 2, TIME / 2))
        except:
            pass

        if (random.randint(0, 100) <= 2):
             keyboard.write("z")

def main():
    def on_start():
        global driver
        global RUN
        global u
        global p

        if not driver:
            # Launch Chrome browser
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            options.add_argument('--disable-software-rasterize')
            driver = webdriver.Chrome(chrome_options=options)

            if (len(u.get()) and len(p.get())):
                driver.get("https://www.nitrotype.com/login")
                driver.find_element("xpath", "//input[@name='username']").send_keys(u.get())
                driver.find_element("xpath", "//input[@name='password']").send_keys(p.get())
                driver.find_element("xpath", "//button[@type='submit']").click()
            time.sleep(3)
            driver.get("https://www.nitrotype.com/race")

        RUN = True
        child = Thread(target=botalgo)
        child.start()
        
        startbutton.place(relx=1.5, rely=1.5, anchor="s")
        stopbutton.place(relx=0.5, rely=0.95, anchor="s")

    def on_stop():
        global RUN
        global driver
        global u
        global p

        RUN = False

        u.set("")
        p.set("")

        if driver:
            try:
                driver.close()
            except:
                pass
            driver = None
        
        startbutton.place(relx=0.5, rely=0.95, anchor="s")
        stopbutton.place(relx=1.5, rely=1.5, anchor="s")

    def on_closing():
        global driver
        global RUN

        RUN = False

        window.destroy()

        if driver:
            try:
                driver.close()
            except:
                pass
            driver = None
        
        

    global u
    global p

    ctk.set_appearance_mode("dark")

    window = ctk.CTk()
    window.title("Nitro Type Bot")

    u = tk.StringVar()
    p = tk.StringVar()

    window.geometry("400x300")
    window.resizable(False, False)

    title = ctk.CTkLabel(window, text="Nitro Type Bot", font=("Arial", 20))
    title.place(relx=0.5, rely=0.1, anchor="center")

    luser = ctk.CTkLabel(window, text="Username:", font=("Arial", 14))
    luser.place(relx=0.25, rely=0.3, anchor="center")
    user = ctk.CTkEntry(window, width = 200, height = 25, corner_radius = 10, textvariable = u)
    user.place(relx=0.6, rely=0.3, anchor="center")

    lpswd = ctk.CTkLabel(window, text="Password:", font=("Arial", 14))
    lpswd.place(relx=0.25, rely=0.4, anchor="center")
    pswd = ctk.CTkEntry(window, width = 200, height = 25, corner_radius = 10, textvariable = p, show="*")
    pswd.place(relx=0.6, rely=0.4, anchor="center")

    def setAUTO():
        global AUTO
        AUTO = auto.get()

    auto = ctk.CTkCheckBox(window, text='Automatically go to next race', command=setAUTO)
    auto.place(relx=0.5, rely=0.5, anchor="center")

    def setTIME(val):
        global TIME
        cur = str(val * 0.5)[0:3]
        TIME = times[cur]

        lslider.configure(text="Type Speed: " + str(times[cur]) + " sec delay")
        if TIME == 0:
            lwarning.place(relx=0.5, rely=0.8, anchor="center")
        else:
            lwarning.place(relx=1.5, rely=1.8, anchor="center")

    lslider = ctk.CTkLabel(window, text="Type Speed: " + str(times["0.2"]) + " sec delay", font=("Arial", 16))
    lslider.place(relx=0.5, rely=0.6, anchor="center")
    slider = ctk.CTkSlider(master=window, width=160, height=16, border_width=5.5, command=setTIME)
    slider.place(relx=0.5, rely=0.7, anchor="center")

    lwarning = ctk.CTkLabel(window, text="WARNING: Current typing speed can result in a ban", font=("Arial", 10), text_color="red")
    lwarning.place(relx=1.5, rely=1.8, anchor="center")

    startbutton = ctk.CTkButton(window, text="Start!", command = on_start, fg_color="green", hover_color="green")
    startbutton.place(relx=0.5, rely=0.95, anchor="s")

    stopbutton = ctk.CTkButton(window, text="Stop!", command = on_stop, fg_color="red", hover_color="red")
    stopbutton.place(relx=1.5, rely=1.5, anchor="s")

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

if __name__ == "__main__":
    main()