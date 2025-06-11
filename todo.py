# To-Do List (Project #2)
import tkinter as tk
from tkinter import PhotoImage, messagebox # Import messagebox for confirmations
import winsound
import datetime

class TodoApp:
    def __init__(self, master):  #initialize the attributes (variables) of that new object.
        #constructor function 
        self.master = master  # self = first parameter of any method inside a class.    
         # 'self' refers to the object being created
        master.title("Python TO-DO List")
        master.geometry("700x600")  #refer to the parent window or widget that the current widget/frame will be placed inside.
        """self.master = master: This line stores a reference to the root window as an attribute of the TodoApp instance. This allows any method within TodoApp to easily access and manipulate the main window"""
        
        # Configure the main window's grid for responsiveness
        master.grid_rowconfigure(1, weight=1) # Row for tasks will expand
        master.grid_columnconfigure(0, weight=1) # Column for tasks will expand

        # --- Top Section (Header) ---
        header_frame = tk.Frame(master)
        header_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew") # Spans across columns
        header_frame.grid_columnconfigure(0, weight=1) # Makes the title column expandable

        self.title_label = tk.Label(header_frame, text="To-Do List", font=('Arial', 24, 'bold'))
        self.title_label.grid(row=0, column=0, sticky="w", padx=10) # Left-align in header

        current_date = datetime.date.today().strftime("%d/%m/%Y") # d; date, m; month, Y; year
        self.date_label = tk.Label(header_frame, text=f"Date: {current_date}", font=('Arial', 12))
        self.date_label.grid(row=0, column=1, sticky="e", padx=10) # Right-align in header, 'e' as in east; right side

        # --- Add Task Button ---
        try:
            self.add_icon = PhotoImage(file="more.png", height = 24, width = 24) 
            # Resize icon if needed
            #self.add_icon = self.add_icon.subsample(2, 2) # Example: makes it half size
        except tk.TclError:
            print("Warning: 'more.png' not found. Using text button.")
            self.add_icon = None

        if self.add_icon:
            self.add_button = tk.Button(header_frame, image=self.add_icon, command=self.add_task)
        else:
            self.add_button = tk.Button(header_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, sticky="e", padx=10) # Far right in header

        # --- Task Container Frame (Scrollable) ---
        # This frame will hold all individual task frames
        self.tasks_container_frame = tk.Frame(master, bd=2, relief="groove")
        self.tasks_container_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        # Configure the container frame to expand internally
        self.tasks_container_frame.grid_rowconfigure(0, weight=1) # Makes the canvas row expandable
        self.tasks_container_frame.grid_columnconfigure(0, weight=1) # Makes the canvas column expandable

        # Use a Canvas for scrollability if many tasks are expected
        self.canvas = tk.Canvas(self.tasks_container_frame, borderwidth=0, background="#ffffff")
        self.task_scrollbar = tk.Scrollbar(self.tasks_container_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, background="#ffffff")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.task_scrollbar.set)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.task_scrollbar.grid(row=0, column=1, sticky="ns")

        # List -> Dict; to store references to task frames
        self.task_frames = []
        self.task_counter = 0 # To give unique IDs to tasks

        # Load delete icon once
        try:
            self.delete_icon = PhotoImage(file="delete.png") # Replace with your delete icon path
            self.delete_icon = self.delete_icon.subsample(2, 2) # Example: makes it half size
        except tk.TclError:
            print("Warning: 'delete.png' not found. Using text for delete button.")
            self.delete_icon = None

        # Load done/completed icon 
        try: 
            self.complete_icon = PhotoImage(file="accept.png")
            self.complete_icon = self.complete_icon.subsample(2, 2)
        except tk.TclError:
            print("Warning: 'accept.png' not found. Using text for complete button.")
            self.complete_icon = None
        # Add an initial task
        self.add_task()

    def add_task(self):
        self.task_counter += 1
        task_id = self.task_counter

        # Create a new Frame for each task
        task_frame = tk.Frame(self.scrollable_frame, bd=2, relief="solid", padx=10, pady=10, bg="gray")
        # Grid this task_frame within the scrollable_frame
        # The row will be dynamic, and it will span all columns (if any others were added)
        task_frame.grid(row=len(self.task_frames) , column=0, sticky="nsew", pady=5)
        self.scrollable_frame.grid_columnconfigure(1, weight=1) # Make the column for tasks expand

        # --- Widgets inside the Task Frame ---

        # Delete Button (Far Left)
        if self.delete_icon:
            delete_button = tk.Button(task_frame, image=self.delete_icon, command=lambda: self.delete_task(task_frame, task_id))
        else:
            delete_button = tk.Button(task_frame, text="Del", command=lambda: self.delete_task(task_frame, task_id))
        delete_button.grid(row=0, column=0, rowspan=2, sticky="ns", padx=(0, 10)) # Mid-left, spans 2 rows

        # Complete Button (Far Right)
        if self.complete_icon:
            complete_button = tk.Button(task_frame, image=self.complete_icon, command=lambda: self.complete_task(task_frame, task_id))
        else:
            complete_button = tk.Button(task_frame, text="Del", command=lambda: self.complete_task(task_frame, task_id))
        complete_button.grid(row=0, column=2, rowspan=2, sticky="ns", padx=(10, 0)) # Mid-right, spans 2 rows

        # Task Title (Entry widget)
        title_entry = tk.Entry(task_frame, font=('Arial', 14, 'bold'))
        title_entry.insert(0, f"Task #{task_id}")
        title_entry.grid(row=0, column=1, sticky="ew", pady=(0, 5))
        task_frame.grid_columnconfigure(1, weight=1) # Title entry column expands

        # Task Description (Text widget)
        # Use wrap=tk.WORD for readability
        description_text = tk.Text(task_frame, height=3, wrap=tk.WORD, font=('Arial', 10))
        description_text.insert(tk.END, "Enter description here...")
        description_text.grid(row=1, column=1, sticky="ew")

        # Store a reference to the task frame and its ID for later deletion
        self.task_frames.append({'id': task_id, 'frame': task_frame, 'title_entry': title_entry, 'description_text': description_text})

        # Update the scroll region after adding a new task
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # PLAYING SOUND IF DEL/COMPLETING TASK(S)
    def play_sound(self, action):
        if action == "complete":
            winsound.Beep(1000, 300)
        else:
            winsound.Beep(600, 250)

    # Deleting Task Function 
    def delete_task(self, task_frame_to_delete, task_id):
        if messagebox.askyesno("Delete Task", f"Are you sure you want to delete Task #{task_id}?"):
            self.play_sound("delete")
            task_frame_to_delete.destroy() # Destroy the frame and all its contents

            # Remove the task from our tracking list
            self.task_frames = [task for task in self.task_frames if task['id'] != task_id]

            # Re-grid the remaining tasks to fill any gaps (optional, but good for appearance)
            for i, task_dict in enumerate(self.task_frames):
                task_dict['frame'].grid(row=i, column=0, sticky="ew", pady=5)
            # Update scroll region after deletion
            self.canvas.update_idletasks()
            self.canvas.config(scrollregion=self.canvas.bbox("all"))
    # Completing Tasks
    def complete_task(self, task_frame_to_comp, task_id):
            if messagebox.askyesno("Task Completed?", f"Task#{task_id} completed?"):
                self.play_sound("complete")
                task_frame_to_comp.destroy() # Destroy the frame and all its contents
                 # Remove the task from our tracking list
                self.task_frames = [task for task in self.task_frames if task['id'] != task_id]
                 
                for i, task_dict in enumerate(self.task_frames):
                    task_dict['frame'].grid(row=i, column=0, sticky="ew", pady=5)

                # Update scroll region after completion
                self.canvas.update_idletasks()
                self.canvas.config(scrollregion=self.canvas.bbox("all"))

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()