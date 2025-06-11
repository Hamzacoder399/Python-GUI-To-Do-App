# Python-Utility-Calculator-CLI-
# Command-Line Calculator

A simple Python command-line calculator that supports multiple menus and submenus for basic arithmetic operations including:

- Addition
- Subtraction
- Multiplication
- Division
- Modulo
- Floor Division
- Handles edge cases like division by zero

## 🔁 Menu Navigation System

The program uses a looping structure with dynamic submenus. Users can navigate through different operation menus and submenus, and return to previous menus as needed. The logic ensures the menu stays active until the user exits.

## ✅ Features

- Interactive CLI-based menu system
- Supports chained navigation between menus
- Validates input and handles exceptions (e.g., division/modulo by 0)
- Keeps returning to submenu after a task is completed
- Clean, tested and ready-to-use code
- Has multiple converters; Temperature, Mass and Length Converters.

## 🖥 How to Run

1. Make sure Python is installed on your system. (Python version at least 3.6 and above)
2. Clone or download the project.
3. Open a terminal and run: 

```bash
py calculator.py

Main Menu:
1; Basic Arithmetic
2; Length Converter
3; Mass Converter
4; Length Converter
0; Exit

> 1

Basic Arithmetic:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Remainder (Mod)
6. Floor Division 
7. Power
8. Back (change menu)

> 4

Enter first number: 10  
Enter second number: 0  
Dividing by zero (0) is not allowed.
