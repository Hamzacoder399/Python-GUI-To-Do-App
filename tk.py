# btn = tk.Button(window, image=icon)
# Create a 3x3 button grid
# for r in range(3):
#     for c in range(3):
#         btn = tk.Button(window, text=f"{r},{c}", width=10, height=3)
#         btn.grid(row=r, column=c, padx=10, pady=10)

# btn.image = icon  # Keep a reference to prevent garbage collection
# btn.grid(row = 0, column = 0)
# Button
# button = tk.Button(window, text="Click me!", font=('Cambria', 10), height=4)
# button.pack(padx=12, pady = 8)
# # Buttons in Grid
# button_frame = tk.Frame(window)
# button_frame.columnconfigure(0, weight=1)
# button_frame.columnconfigure(1, weight=1)
# # button_frame.columnconfigure(2, weight=1)
# # button_frame.columnconfigure(4, weight=1)
# butn1 = tk.Button(button_frame, text="1", font=('Arial', 14))
# butn1.grid(row = 0, column = 0, sticky = tk.W + tk.E)
# butn2 = tk.Button(button_frame, text="2", font=('Arial', 14))
# butn2.grid(row = 0, column = 1, sticky = tk.W + tk.E)
# butn3 = tk.Button(button_frame, text="3", font=('Arial', 14))
# butn3.grid(row = 2, column = 0, sticky = tk.W + tk.E)
# butn4 = tk.Button(button_frame, text="4", font=('Arial', 14))
# butn4.grid(row = 2, column = 1, sticky = tk.W + tk.E)   

# Input Box/Text Box
# text_box = tk.Text(window, font=('Cambria', 22), height=4)
# text_box.grid()
# Configure 2 columns so button goes far right
import tkinter as tk
root = tk.Tk()
root.title("Banana")
root.geometry("500x600")
title = tk.Label(root, text='Please take the survey', font=('Arial', 16, 'bold'), bg='brown', fg='#FF0')
title.pack(pady = 10)

name_label = tk.Label(root, text='What is your name?') 
name_label.pack()

name_inp = tk.Entry(root)
name_inp.pack(pady=5)
stored_value = name_inp.get()
button = tk.Button(
    root, 
    text="Print Entry Value",
    command=lambda: print("Current value:", name_inp.get())  # Get value directly
)
button.pack()

color_label = tk.Label(root, text='What is the best color for a banana?') 
color_label.pack()
color_choices = ( 'Any', 'Green', 'Green-Yellow', 'Yellow', 'Brown Spotted', 'Black') 
selected_color = tk.StringVar(root)
selected_color.set(color_choices[0])
color_inp = tk.OptionMenu(root, selected_color, *color_choices) # dropdown menu
color_inp.pack(pady = 5)

# for choice in color_choices: 
#     color_inp.insert(tk.END, choice)
# color_inp.pack(pady=5)

root.mainloop()