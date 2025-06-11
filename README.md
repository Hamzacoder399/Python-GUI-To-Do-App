
# Python-GUI-To-Do-App

📝 Python To-Do List App
A simple yet visually appealing To-Do List GUI built using tkinter. This app lets users create, update, and manage tasks with descriptions. It includes modern UI elements, date display, and even plays system sounds for interaction feedback.

✅ Features
🗂️ Add, edit, and remove tasks

📄 Each task has a title and description

📅 Displays current date

🔔 Plays system sounds on actions (optional)

🎨 Clean, user-friendly interface

🔼 Scroll support for multiple tasks

🚀 Technologies Used
Python

tkinter (GUI framework)

datetime (for showing current date)

winsound (for system alert sounds — Windows only)

💻 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/todo-list-python.git
cd todo-list-python
Run the script:

bash
Copy
Edit
python todo.py
🔊 Sound Support (Optional)
The app uses winsound.PlaySound() for system alert sounds when tasks are added, completed, or deleted.

⚠️ Works only on Windows. On Linux/macOS, remove or replace the sound code.

🛠️ Project Structure
bash
Copy
Edit
todo-list-python/
│
├── todo.py         # Main application file
├── README.md       # Project overview and setup instructions
└── assets/         # (Optional) Icons, sounds, or screenshots
📌 Future Improvements
✅ Save tasks locally using JSON or pickle

☁️ Add persistent storage (SQLite or Firebase)

📱 Convert to mobile app using Kivy or PyQt

🌗 Add dark mode support

📜 License
This project is open-source under the MIT License.

🙌 Acknowledgements
Inspired by productivity apps like Microsoft To-Do and Google Tasks.

Built as part of Python learning and GUI practice.
