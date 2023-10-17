'''Create a project that lets a user enter an URL and lets it know that the site is functioning
The way we determine this is by returning the code 200 from the getcode() function from urllib'''

from urllib.request import urlopen
import tkinter as tk
from tkinter import messagebox


#functions section

def start(url_entry_text):
    '''function that gets entry and returns connectivity'''
    try:

        if url_entry_text:
            url = urlopen(url_entry_text)
            code = url.getcode()
            if code == 200: #code 200 for available webpages
                messagebox.showinfo("Connection Test Results", "The webpage is available.")
            else:
                messagebox.showinfo("Connection Test Results",f"The webpage is not available. The code is {code}")
        else:
            messagebox.showerror("Test Connection Fail", "The URL cannot be blank.")
    except ValueError:
        messagebox.showerror("Test Connection Fail", "The entered URL is not valid.")

        

if __name__ == "__main__":
    main_window = tk.Tk()
    
    #settint the screen dimensions
    window_width = 500
    window_height = 400

    # get the screen dimension
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    main_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    main_window.resizable(0,0)

    #setting customization
    main_window.title("Connectivity test by Jesus Valencia")

    #Label for instructions
    instructions_label = tk.Label(main_window, text="Welcome to the Network Connectivity Test.\n Please insert your URL down below in the form of:\nhttp://page.com or https://page.com", font="Verdana")
    instructions_label.pack()

    #URL Entry
    url_entry_text = tk.StringVar()
    url_entry = tk.Entry(main_window, width=80, textvariable=url_entry_text)
    url_entry.pack()

    url_entry.focus()

    #button to start
    test_button = tk.Button(main_window, text="Test Connection", command=lambda: start(url_entry_text.get())) #as soon as the button is pressed, get the entry text from box
    test_button.pack()

    







    #start app
    main_window.mainloop()

