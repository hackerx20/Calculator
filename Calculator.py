#importing GUI python Library

# import tkinter as tk

# calculation = "" #creating a empty calculation string

# #Creating a add_to_calculation function that will add the symbol pressed to the calculation string
# def add_to_Calculation(symbol):
#     global calculation
#     calculation += str(symbol)
#     text_result.delete(1.0, 'end')
#     text_result.insert(1.0, calculation)
# #this combination first clears the existing display and then inserts the new value, ensuring that only the latest calculation or input is shown on the calculator screen.


# #Creating a function that will evaluate the calculation string and return the result in the form of a string
# def evaluate_calculation(): 
#     global calculation
#     # evaluating the calculation string and storing the result in the calculation variable
#     try:
#         calculation = str(eval(calculation))
#         text_result.delete(1.0, "end")
#         text_result.insert(1.0, calculation)
# # calculation = ""
# # if the calculation is not possible then except statement runs
#     except:
#         clear_calculation()
#         text_result.insert(1.0, "Error")


# #creating a clear_calculation function that will clear the calculation string
# def clear_calculation():
#     global calculation
#     calculation = ""
#     text_result.delete(1.0, 'end')



# #creating a root window
# root=tk.Tk()
# root.title("Calculator")  #assigning a title to the root window
# root.geometry("400x400")  #assigning a geometry to the root window
# root.resizable(True,True)
# root.config(bg="#1E1E1E")  #background color to the calculator


# #creating a text widget to display the calculation result
# text_result = tk.Text(root,height="2", width="20", font=("arial",24),bg="black", fg="white")
# text_result.grid(columnspan=5)



#    <<<------------------------------------------NOOB WAY------------------------------------------------------------>>>


# btn_1=tk.Button(root, text="1", command=lambda: add_to_Calculation(1), width=5, font=("arial",14), bg="#333333", fg="white")
# btn_1.grid(row=2, column=1)

# btn_2=tk.Button(root, text="2", command=lambda: add_to_Calculation(2), width=5, font=("arial",14), bg="#333333", fg="white")
# btn_2.grid(row=2, column=2)

# btn_3=tk.Button(root, text="3", command=lambda: add_to_Calculation(3), width=5, font=("arial",14), bg="#333333", fg="white")
# btn_3.grid(row=2, column=3)

# btn_4=tk.Button(root, text="4", command=lambda: add_to_Calculation(4), width=5, font=("arial",14), bg="#333333", fg="white")
# btn_4.grid(row=3, column=1)

# btn_5=tk.Button(root, text="5", command=lambda: add_to_Calculation(5), width=5, font=("arial",14), bg="#333333", fg="white")
# btn_5.grid(row=3, column=2)

# btn_6=tk.Button(root, text="6", command=lambda: add_to_Calculation(6), width=5, font=("arial",14), bg="#333333", fg="white")
# btn_6.grid(row=3, column=3)

# btn_7=tk.Button(root, text="7", command=lambda: add_to_Calculation(7), width=5, font=("arial",14), bg="#333333", fg="white")
# btn_7.grid(row=4, column=1)

# btn_8=tk.Button(root, text="8", command=lambda: add_to_Calculation(8), width=5, font=("arial",14), bg="#333333", fg="white")
# btn_8.grid(row=4, column=2)

# btn_9=tk.Button(root, text="9", command=lambda: add_to_Calculation(9), width=5, font=("arial",14), bg="#333333", fg="white")
# btn_9.grid(row=4, column=3)

# btn_0=tk.Button(root, text="0", command=lambda: add_to_Calculation(0), width=5, font=("arial",14), bg="#333333", fg="white")
# btn_0.grid(row=5, column=2)

# btn_Plus=tk.Button(root, text="+", command=lambda: add_to_Calculation("+"), width=5, font=("arial",14), bg="orange", fg="white")
# btn_Plus.grid(row=2, column=4)

# btn_minus=tk.Button(root, text="-", command=lambda: add_to_Calculation("-"), width=5, font=("arial",14), bg="orange", fg="white")
# btn_minus.grid(row=3, column=4)

# btn_product=tk.Button(root, text="*", command=lambda: add_to_Calculation("*"), width=5, font=("arial",14), bg="orange", fg="white")
# btn_product.grid(row=4, column=4)

# btn_divide=tk.Button(root, text="/", command=lambda: add_to_Calculation("/"), width=5, font=("arial",14), bg="orange", fg="white")
# btn_divide.grid(row=5, column=4)

# btn_open=tk.Button(root, text="(", command=lambda: add_to_Calculation("("), width=5, font=("arial",14), bg="orange", fg="white")
# btn_open.grid(row=5, column=1)

# btn_close=tk.Button(root, text=")", command=lambda: add_to_Calculation(")"), width=5, font=("arial",14), bg="orange", fg="white")
# btn_close.grid(row=5, column=3)

# btn_enter=tk.Button(root, text="Enter", command=evaluate_calculation, width=12, font=("arial",14), bg="orange", fg="white")
# btn_enter.grid(row=6, column=3, columnspan=2)

# btn_clear=tk.Button(root, text="Clear", command=clear_calculation, width=12, font=("arial",14), bg="orange", fg="white")
# btn_clear.grid(row=6, column=1, columnspan=2)



#    <<<----------------------------------------BETTER WAY----------------------------------------------------->>>


# Add padding and hover effect for buttons
# def on_enter(e):
#     e.widget['background'] = '#4C4C4C'

# def on_leave(e):
#     e.widget['background'] = e.widget.default_bg




# Define a function to create buttons with hover effect
# def create_button(text, command, row, column, bg, fg="white", columnspan=1):
#     button = tk.Button(root, text=text, command=command, width=5, font=("Helvetica", 16), bg=bg, fg=fg, activebackground="#4C4C4C", bd=0, highlightthickness=0)
#     button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)
#     button.default_bg = bg  # Store original color
#     button.bind("<Enter>", on_enter)  # Hover effect
#     button.bind("<Leave>", on_leave)
#     return button


# Create buttons
# create_button("1", lambda: add_to_Calculation(1), 2, 1, "#333333")
# create_button("2", lambda: add_to_Calculation(2), 2, 2, "#333333")
# create_button("3", lambda: add_to_Calculation(3), 2, 3, "#333333")
# create_button("4", lambda: add_to_Calculation(4), 3, 1, "#333333")
# create_button("5", lambda: add_to_Calculation(5), 3, 2, "#333333")
# create_button("6", lambda: add_to_Calculation(6), 3, 3, "#333333")
# create_button("7", lambda: add_to_Calculation(7), 4, 1, "#333333")
# create_button("8", lambda: add_to_Calculation(8), 4, 2, "#333333")
# create_button("9", lambda: add_to_Calculation(9), 4, 3, "#333333")
# create_button("0", lambda: add_to_Calculation(0), 5, 2, "#333333")

# Operator buttons styled differently
# create_button("+", lambda: add_to_Calculation("+"), 2, 4, "#FF5733")
# create_button("-", lambda: add_to_Calculation("-"), 3, 4, "#FF5733")
# create_button("*", lambda: add_to_Calculation("*"), 4, 4, "#FF5733")
# create_button("/", lambda: add_to_Calculation("/"), 5, 4, "#FF5733")
# create_button("(", lambda: add_to_Calculation("("), 5, 1, "#FF5733")
# create_button(")", lambda: add_to_Calculation(")"), 5, 3, "#FF5733")

# Special buttons
# create_button("Clear", clear_calculation, 6, 1, "#FF5733", columnspan=2)
# create_button("Enter", evaluate_calculation, 6, 3, "#FF5733", columnspan=2)


# Adding keyboard shortcuts to the calculator
# def key_press(event):
#     if event.char.isdigit():
#         add_to_Calculation(event.char)
#     elif event.char in '+-*/().':
#         add_to_Calculation(event.char)
#     elif event.keysym == 'Return':
#         evaluate_calculation()
#     elif event.keysym == 'BackSpace':
#         clear_calculation()

# root.bind("<Key>", key_press)
# root.mainloop()


import tkinter as tk
from tkinter import ttk, messagebox, font
import math
import re
from datetime import datetime
import json
import os

class ScientificCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_variables()
        self.create_styles()
        self.create_widgets()
        self.bind_keyboard_events()
        self.load_history()
        
    def setup_window(self):
        """Configure the main window"""
        self.root.title("Professional Scientific Calculator")
        self.root.geometry("500x700")
        self.root.minsize(450, 650)
        self.root.configure(bg='#1a1a1a')
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"500x700+{x}+{y}")
        
        # Configure grid weights for responsiveness
        self.root.grid_columnconfigure(0, weight=1)
        for i in range(10):
            self.root.grid_rowconfigure(i, weight=1)
    
    def setup_variables(self):
        """Initialize calculator variables"""
        self.current_input = ""
        self.result = ""
        self.memory = 0
        self.history = []
        self.is_scientific_mode = False
        self.last_operation = ""
        self.last_number = ""
        
    def create_styles(self):
        """Create custom styles for the calculator"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Display.TEntry', 
                       fieldbackground='#2d2d2d',
                       foreground='white',
                       borderwidth=2,
                       relief='flat',
                       insertcolor='white')
        
        style.configure('Number.TButton',
                       background='#3d3d3d',
                       foreground='white',
                       borderwidth=1,
                       focuscolor='none',
                       font=('Segoe UI', 12, 'bold'))
        
        style.configure('Operator.TButton',
                       background='#ff6b35',
                       foreground='white',
                       borderwidth=1,
                       focuscolor='none',
                       font=('Segoe UI', 12, 'bold'))
        
        style.configure('Function.TButton',
                       background='#4a90e2',
                       foreground='white',
                       borderwidth=1,
                       focuscolor='none',
                       font=('Segoe UI', 10, 'bold'))
        
        style.configure('Special.TButton',
                       background='#2d2d2d',
                       foreground='white',
                       borderwidth=1,
                       focuscolor='none',
                       font=('Segoe UI', 11, 'bold'))
        
        # Map hover effects
        style.map('Number.TButton', background=[('active', '#4d4d4d')])
        style.map('Operator.TButton', background=[('active', '#ff8555')])
        style.map('Function.TButton', background=[('active', '#5aa0f2')])
        style.map('Special.TButton', background=[('active', '#3d3d3d')])
    
    def create_widgets(self):
        """Create all calculator widgets"""
        self.create_display()
        self.create_memory_indicators()
        self.create_button_frame()
        self.create_history_frame()
        
    def create_display(self):
        """Create the calculator display"""
        display_frame = tk.Frame(self.root, bg='#1a1a1a', height=120)
        display_frame.grid(row=0, column=0, sticky='ew', padx=10, pady=(10, 5))
        display_frame.grid_propagate(False)
        
        # Main display
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Entry(display_frame, 
                               textvariable=self.display_var,
                               font=('Segoe UI', 24, 'bold'),
                               justify='right',
                               state='readonly',
                               bg='#2d2d2d',
                               fg='white',
                               bd=0,
                               highlightthickness=2,
                               highlightcolor='#4a90e2',
                               highlightbackground='#3d3d3d')
        self.display.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Secondary display for operations
        self.operation_var = tk.StringVar()
        self.operation_display = tk.Label(display_frame,
                                         textvariable=self.operation_var,
                                         font=('Segoe UI', 12),
                                         bg='#2d2d2d',
                                         fg='#888888',
                                         anchor='e')
        self.operation_display.pack(fill='x', padx=5, pady=(0, 5))
    
    def create_memory_indicators(self):
        """Create memory and mode indicators"""
        indicator_frame = tk.Frame(self.root, bg='#1a1a1a')
        indicator_frame.grid(row=1, column=0, sticky='ew', padx=10, pady=5)
        
        self.memory_indicator = tk.Label(indicator_frame, text="", 
                                        font=('Segoe UI', 9),
                                        bg='#1a1a1a', fg='#4a90e2')
        self.memory_indicator.pack(side='left')
        
        self.mode_indicator = tk.Label(indicator_frame, text="Standard Mode",
                                      font=('Segoe UI', 9),
                                      bg='#1a1a1a', fg='#888888')
        self.mode_indicator.pack(side='right')
    
    def create_button_frame(self):
        """Create the main button layout"""
        button_frame = tk.Frame(self.root, bg='#1a1a1a')
        button_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)
        
        # Configure grid weights
        for i in range(8):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(6):
            button_frame.grid_columnconfigure(i, weight=1)
        
        self.create_standard_buttons(button_frame)
        self.create_scientific_buttons(button_frame)
    
    def create_standard_buttons(self, parent):
        """Create standard calculator buttons"""
        # Row 0: Memory and mode functions
        self.create_button(parent, "MC", self.memory_clear, 0, 0, 'Special.TButton')
        self.create_button(parent, "MR", self.memory_recall, 0, 1, 'Special.TButton')
        self.create_button(parent, "M+", self.memory_add, 0, 2, 'Special.TButton')
        self.create_button(parent, "M-", self.memory_subtract, 0, 3, 'Special.TButton')
        self.create_button(parent, "MS", self.memory_store, 0, 4, 'Special.TButton')
        self.create_button(parent, "Sci", self.toggle_scientific, 0, 5, 'Function.TButton')
        
        # Row 1: Special functions
        self.create_button(parent, "C", self.clear_all, 1, 0, 'Operator.TButton')
        self.create_button(parent, "CE", self.clear_entry, 1, 1, 'Operator.TButton')
        self.create_button(parent, "⌫", self.backspace, 1, 2, 'Operator.TButton')
        self.create_button(parent, "±", self.change_sign, 1, 3, 'Operator.TButton')
        self.create_button(parent, "√", lambda: self.add_function("sqrt("), 1, 4, 'Function.TButton')
        self.create_button(parent, "÷", lambda: self.add_operator("/"), 1, 5, 'Operator.TButton')
        
        # Row 2: Numbers and operations
        self.create_button(parent, "7", lambda: self.add_number("7"), 2, 0, 'Number.TButton')
        self.create_button(parent, "8", lambda: self.add_number("8"), 2, 1, 'Number.TButton')
        self.create_button(parent, "9", lambda: self.add_number("9"), 2, 2, 'Number.TButton')
        self.create_button(parent, "×", lambda: self.add_operator("*"), 2, 5, 'Operator.TButton')
        
        # Row 3
        self.create_button(parent, "4", lambda: self.add_number("4"), 3, 0, 'Number.TButton')
        self.create_button(parent, "5", lambda: self.add_number("5"), 3, 1, 'Number.TButton')
        self.create_button(parent, "6", lambda: self.add_number("6"), 3, 2, 'Number.TButton')
        self.create_button(parent, "-", lambda: self.add_operator("-"), 3, 5, 'Operator.TButton')
        
        # Row 4
        self.create_button(parent, "1", lambda: self.add_number("1"), 4, 0, 'Number.TButton')
        self.create_button(parent, "2", lambda: self.add_number("2"), 4, 1, 'Number.TButton')
        self.create_button(parent, "3", lambda: self.add_number("3"), 4, 2, 'Number.TButton')
        self.create_button(parent, "+", lambda: self.add_operator("+"), 4, 5, 'Operator.TButton')
        
        # Row 5
        self.create_button(parent, "0", lambda: self.add_number("0"), 5, 0, 'Number.TButton', columnspan=2)
        self.create_button(parent, ".", lambda: self.add_decimal(), 5, 2, 'Number.TButton')
        self.create_button(parent, "=", self.calculate, 5, 5, 'Operator.TButton')
        
        # Row 6: Additional functions
        self.create_button(parent, "(", lambda: self.add_operator("("), 6, 0, 'Special.TButton')
        self.create_button(parent, ")", lambda: self.add_operator(")"), 6, 1, 'Special.TButton')
        self.create_button(parent, "%", lambda: self.add_operator("%"), 6, 2, 'Function.TButton')
        self.create_button(parent, "x²", lambda: self.add_function("**2"), 6, 3, 'Function.TButton')
        self.create_button(parent, "1/x", self.reciprocal, 6, 4, 'Function.TButton')
        
    def create_scientific_buttons(self, parent):
        """Create scientific function buttons (initially hidden)"""
        self.sci_buttons = []
        
        # Scientific functions that appear when in scientific mode
        sci_functions = [
            ("sin", lambda: self.add_function("sin("), 2, 3),
            ("cos", lambda: self.add_function("cos("), 2, 4),
            ("tan", lambda: self.add_function("tan("), 3, 3),
            ("log", lambda: self.add_function("log10("), 3, 4),
            ("ln", lambda: self.add_function("log("), 4, 3),
            ("e^x", lambda: self.add_function("exp("), 4, 4),
            ("π", lambda: self.add_number(str(math.pi)), 5, 3),
            ("e", lambda: self.add_number(str(math.e)), 5, 4),
            ("x^y", lambda: self.add_operator("**"), 6, 5),
        ]
        
        for text, command, row, col in sci_functions:
            btn = self.create_button(parent, text, command, row, col, 'Function.TButton')
            btn.grid_remove()  # Hide initially
            self.sci_buttons.append(btn)
    
    def create_button(self, parent, text, command, row, col, style, columnspan=1):
        """Create a button with specified properties"""
        btn = ttk.Button(parent, text=text, command=command, style=style)
        btn.grid(row=row, column=col, columnspan=columnspan, 
                sticky='nsew', padx=2, pady=2)
        return btn
    
    def create_history_frame(self):
        """Create the calculation history panel"""
        history_frame = tk.LabelFrame(self.root, text="History", 
                                     bg='#1a1a1a', fg='white',
                                     font=('Segoe UI', 10, 'bold'))
        history_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=5)
        
        # History listbox with scrollbar
        history_list_frame = tk.Frame(history_frame, bg='#1a1a1a')
        history_list_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(history_list_frame, bg='#3d3d3d')
        scrollbar.pack(side='right', fill='y')
        
        self.history_listbox = tk.Listbox(history_list_frame, 
                                         yscrollcommand=scrollbar.set,
                                         bg='#2d2d2d', fg='white',
                                         font=('Consolas', 10),
                                         selectbackground='#4a90e2',
                                         borderwidth=0,
                                         highlightthickness=1,
                                         highlightcolor='#4a90e2')
        self.history_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.history_listbox.yview)
        
        # History controls
        history_controls = tk.Frame(history_frame, bg='#1a1a1a')
        history_controls.pack(fill='x', padx=5, pady=(0, 5))
        
        ttk.Button(history_controls, text="Clear History", 
                  command=self.clear_history, 
                  style='Special.TButton').pack(side='left')
        
        ttk.Button(history_controls, text="Use Result", 
                  command=self.use_history_result,
                  style='Function.TButton').pack(side='right')
        
        # Bind double-click to use result
        self.history_listbox.bind('<Double-1>', lambda e: self.use_history_result())
    
    def add_number(self, number):
        """Add a number to the current input"""
        if self.current_input == "0" or self.current_input == "Error":
            self.current_input = number
        else:
            self.current_input += number
        self.update_display()
    
    def add_operator(self, operator):
        """Add an operator to the current input"""
        if self.current_input and self.current_input[-1] not in "+-*/()":
            self.current_input += operator
        elif operator in "()":
            self.current_input += operator
        elif self.current_input == "" and operator == "-":
            self.current_input = operator
        self.update_display()
    
    def add_function(self, function):
        """Add a mathematical function"""
        if self.current_input == "0" or self.current_input == "Error":
            self.current_input = function
        else:
            # Add multiplication if needed
            if self.current_input and self.current_input[-1] not in "+-*/()":
                self.current_input += "*" + function
            else:
                self.current_input += function
        self.update_display()
    
    def add_decimal(self):
        """Add decimal point"""
        # Find the last number in the expression
        matches = re.findall(r'\d*\.?\d+', self.current_input)
        if matches:
            last_number = matches[-1]
            if '.' not in last_number:
                self.current_input += "."
        else:
            if self.current_input == "" or self.current_input[-1] in "+-*/()":
                self.current_input += "0."
        self.update_display()
    
    def change_sign(self):
        """Change the sign of the current number"""
        if self.current_input:
            try:
                value = float(self.current_input)
                self.current_input = str(-value)
                self.update_display()
            except ValueError:
                pass
    
    def reciprocal(self):
        """Calculate reciprocal of current number"""
        if self.current_input:
            try:
                value = float(self.current_input)
                if value != 0:
                    self.current_input = str(1 / value)
                    self.update_display()
                else:
                    self.show_error("Cannot divide by zero")
            except ValueError:
                pass
    
    def backspace(self):
        """Remove the last character"""
        if self.current_input and self.current_input != "Error":
            self.current_input = self.current_input[:-1]
            if not self.current_input:
                self.current_input = "0"
            self.update_display()
    
    def clear_entry(self):
        """Clear the current entry"""
        self.current_input = "0"
        self.update_display()
    
    def clear_all(self):
        """Clear everything"""
        self.current_input = "0"
        self.operation_var.set("")
        self.update_display()
    
    def calculate(self):
        """Perform the calculation"""
        if not self.current_input or self.current_input == "Error":
            return
        
        try:
            # Replace mathematical functions with Python equivalents
            expression = self.current_input
            expression = expression.replace('×', '*').replace('÷', '/')
            
            # Handle mathematical functions
            expression = self.process_math_functions(expression)
            
            # Evaluate the expression
            result = eval(expression)
            
            # Handle special cases
            if math.isnan(result):
                self.show_error("Invalid operation")
                return
            elif math.isinf(result):
                self.show_error("Overflow")
                return
            
            # Format result
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)
            
            # Add to history
            self.add_to_history(f"{self.current_input} = {result}")
            
            # Update display
            self.operation_var.set(self.current_input + " =")
            self.current_input = str(result)
            self.update_display()
            
        except ZeroDivisionError:
            self.show_error("Cannot divide by zero")
        except Exception as e:
            self.show_error("Error")
    
    def process_math_functions(self, expression):
        """Process mathematical functions in the expression"""
        # Replace function names with math module equivalents
        replacements = {
            'sin(': 'math.sin(',
            'cos(': 'math.cos(',
            'tan(': 'math.tan(',
            'log(': 'math.log(',
            'log10(': 'math.log10(',
            'sqrt(': 'math.sqrt(',
            'exp(': 'math.exp(',
        }
        
        for old, new in replacements.items():
            expression = expression.replace(old, new)
        
        return expression
    
    def show_error(self, message):
        """Display error message"""
        self.current_input = "Error"
        self.operation_var.set(message)
        self.update_display()
    
    def update_display(self):
        """Update the main display"""
        display_text = self.current_input if self.current_input else "0"
        self.display_var.set(display_text)
    
    def toggle_scientific(self):
        """Toggle between standard and scientific modes"""
        self.is_scientific_mode = not self.is_scientific_mode
        
        if self.is_scientific_mode:
            self.mode_indicator.config(text="Scientific Mode", fg='#4a90e2')
            for btn in self.sci_buttons:
                btn.grid()
        else:
            self.mode_indicator.config(text="Standard Mode", fg='#888888')
            for btn in self.sci_buttons:
                btn.grid_remove()
    
    # Memory functions
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        self.memory_indicator.config(text="")
    
    def memory_recall(self):
        """Recall memory value"""
        self.current_input = str(self.memory)
        self.update_display()
    
    def memory_store(self):
        """Store current value in memory"""
        try:
            self.memory = float(self.current_input)
            self.memory_indicator.config(text="M")
        except ValueError:
            pass
    
    def memory_add(self):
        """Add current value to memory"""
        try:
            self.memory += float(self.current_input)
            self.memory_indicator.config(text="M")
        except ValueError:
            pass
    
    def memory_subtract(self):
        """Subtract current value from memory"""
        try:
            self.memory -= float(self.current_input)
            self.memory_indicator.config(text="M")
        except ValueError:
            pass
    
    # History functions
    def add_to_history(self, calculation):
        """Add calculation to history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_entry = f"[{timestamp}] {calculation}"
        self.history.append(history_entry)
        self.history_listbox.insert(0, history_entry)
        
        # Limit history to 100 entries
        if len(self.history) > 100:
            self.history.pop()
            self.history_listbox.delete(tk.END)
        
        self.save_history()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        self.history_listbox.delete(0, tk.END)
        self.save_history()
    
    def use_history_result(self):
        """Use selected history result"""
        try:
            selection = self.history_listbox.curselection()
            if selection:
                history_entry = self.history_listbox.get(selection[0])
                # Extract result from history entry
                result = history_entry.split(" = ")[-1]
                self.current_input = result
                self.update_display()
        except:
            pass
    
    def save_history(self):
        """Save history to file"""
        try:
            with open('calculator_history.json', 'w') as f:
                json.dump(self.history, f)
        except:
            pass
    
    def load_history(self):
        """Load history from file"""
        try:
            if os.path.exists('calculator_history.json'):
                with open('calculator_history.json', 'r') as f:
                    self.history = json.load(f)
                    for entry in reversed(self.history):
                        self.history_listbox.insert(0, entry)
        except:
            pass
    
    def bind_keyboard_events(self):
        """Bind keyboard shortcuts"""
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()
    
    def on_key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        keysym = event.keysym
        
        if key.isdigit():
            self.add_number(key)
        elif key in '+-*/':
            self.add_operator(key)
        elif key == '.':
            self.add_decimal()
        elif key == '(':
            self.add_operator('(')
        elif key == ')':
            self.add_operator(')')
        elif keysym == 'Return':
            self.calculate()
        elif keysym == 'BackSpace':
            self.backspace()
        elif keysym == 'Delete' or (event.state & 0x4 and key.lower() == 'a'):
            self.clear_all()
        elif keysym == 'Escape':
            self.clear_entry()
    
    def run(self):
        """Start the calculator"""
        self.root.mainloop()

# Create and run the calculator
if __name__ == "__main__":
    calculator = ScientificCalculator()
    calculator.run()