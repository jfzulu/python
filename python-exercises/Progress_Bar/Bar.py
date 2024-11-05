import tkinter as tk
from tkinter import ttk


def increase_bar():
    value = progress_bar['value']
    if value < 100:
        progress_bar['value']=value + 10
        update_percentage()


def complete_bar():
    value = progress_bar['value']
    if value < 100:
        progress_bar['value'] = value + 5
        update_percentage()
        window.after(100, complete_bar)

def reset_bar():
    progress_bar['value'] = 0
    update_percentage()

def update_percentage():
    value = progress_bar['value']
    percentage.set(f'{int(value)}%')

window = tk.Tk()
window.title('Progress Bar Tkinter')
window.geometry('300x250')
window.configure(bg='#2C3E50')

# Style for progress bar and buttons
style = ttk.Style()
style.theme_use('alt')

# Style for progress bar
style.configure("TProgressbar", troughcolor = '#34495E', background='#1ABC9C', thickness=20)

# Style for buttons
style.configure("TButton", font=('Helvetica', 10, 'bold'), background='#2980B9', foreground='white')
style.map("TButton", background=[('active', '#3498DB')])

#Create Widget
progress_bar = ttk.Progressbar(window, orient='horizontal', length=200,
                              mode='determinate', style="TProgressbar")

progress_bar.pack(pady = 20)

percentage = tk.StringVar()
percentage.set('0%')

#Label to show percentage
label_percentage = tk.Label(window, textvariable= percentage, font=('Helvetica', 10, 'bold'), bg='#2C3E50', fg='white')
label_percentage.pack(pady=10)

#Create Buttons
button_increase=ttk.Button(window, text='Increase', command=increase_bar,
                           style="TButton")
button_increase.pack(pady=5)

button_complete=ttk.Button(window, text='Complete', command=complete_bar, style="TButton")
button_complete.pack(pady=5)

button_reset=ttk.Button(window, text='Reset', command=reset_bar, style='TButton')
button_reset.pack(pady=5)

window.mainloop()
