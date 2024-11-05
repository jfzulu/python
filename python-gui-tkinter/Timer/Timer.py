import tkinter as tk

class Timer:
    def __init__(self, master):
        self.master = master
        self.hours= 0
        self.minutes=0
        self.seconds=0
        self.milliseconds=0
        self.running=False
        self.display=tk.StringVar()
        self.update_display("00:00:00.000")

        #Configure GUI
        self.master.title("Timer")
        self.master.configure(bg="#34495e")
        self.master.geometry("300x200")
        self.display_label=tk.Label(master, textvariable=self.display, font=("Arial", 36), bg="#34495e", fg="#ffffff")
        self.display_label.pack()
        self.button_frame=tk.Frame(master, bg="#000000")
        self.button_frame.pack()

        self.start_button=tk.Button(self.button_frame, text="START", command=self.start, bg="#2ecc71", fg="#ffffff")
        self.start_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.stop_button=tk.Button(self.button_frame, text="STOP", command=self.stop, bg="#e74c3c", fg="#ffffff")
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.stop_button=tk.Button(self.button_frame, text="RESET", command=self.reset, bg="#3498db", fg="#ffffff")
        self.stop_button.pack(side=tk.RIGHT, padx=5, pady=10)


    #UPDATE_DISPLAY
    def update_display(self, time):
        self.display.set(time)

    #START
    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()

    #STOP
    def stop(self):
        self.running=False


    #RESET
    def reset(self):
        self.hours=0
        self.minutes=0
        self.seconds=0
        self.milliseconds=0
        self.update_display("00:00:00.000")

    def update_timer(self):
        if self.running:
            self.milliseconds += 10
            if self.milliseconds >= 1000:
                self.milliseconds =0
                self.seconds +=1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.horas += 1

            time_format= f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}.{self.milliseconds:03}"
            self.update_display(time_format)
            self.master.after(10, self.update_timer)


if __name__=="__main__":
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()




