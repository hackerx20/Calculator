#importing GUI python Library

import tkinter as tk

calculation = "" #creating a empty calculation string

#Creating a add_to_calculation function that will add the symbol pressed to the calculation string
def add_to_Calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)
#this combination first clears the existing display and then inserts the new value, ensuring that only the latest calculation or input is shown on the calculator screen.


#Creating a function that will evaluate the calculation string and return the result in the form of a string
def evaluate_calculation(): 
    global calculation
    # evaluating the calculation string and storing the result in the calculation variable
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
# calculation = ""
# if the calculation is not possible then except statement runs
    except:
        clear_calculation()
        text_result.insert(1.0, "Error")


#creating a clear_calculation function that will clear the calculation string
def clear_calculation():
    global calculation
    calculation = ""
    text_result.delete(1.0, 'end')



#creating a root window
root=tk.Tk()
root.title("Calculator")  #assigning a title to the root window
root.geometry("400x400")  #assigning a geometry to the root window
root.resizable(True,True)
root.config(bg="#1E1E1E")  #background color to the calculator


#creating a text widget to display the calculation result
text_result = tk.Text(root,height="2", width="20", font=("arial",24),bg="black", fg="white")
text_result.grid(columnspan=5)



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
def on_enter(e):
    e.widget['background'] = '#4C4C4C'

def on_leave(e):
    e.widget['background'] = e.widget.default_bg




# Define a function to create buttons with hover effect
def create_button(text, command, row, column, bg, fg="white", columnspan=1):
    button = tk.Button(root, text=text, command=command, width=5, font=("Helvetica", 16), bg=bg, fg=fg, activebackground="#4C4C4C", bd=0, highlightthickness=0)
    button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)
    button.default_bg = bg  # Store original color
    button.bind("<Enter>", on_enter)  # Hover effect
    button.bind("<Leave>", on_leave)
    return button


# Create buttons
create_button("1", lambda: add_to_Calculation(1), 2, 1, "#333333")
create_button("2", lambda: add_to_Calculation(2), 2, 2, "#333333")
create_button("3", lambda: add_to_Calculation(3), 2, 3, "#333333")
create_button("4", lambda: add_to_Calculation(4), 3, 1, "#333333")
create_button("5", lambda: add_to_Calculation(5), 3, 2, "#333333")
create_button("6", lambda: add_to_Calculation(6), 3, 3, "#333333")
create_button("7", lambda: add_to_Calculation(7), 4, 1, "#333333")
create_button("8", lambda: add_to_Calculation(8), 4, 2, "#333333")
create_button("9", lambda: add_to_Calculation(9), 4, 3, "#333333")
create_button("0", lambda: add_to_Calculation(0), 5, 2, "#333333")

# Operator buttons styled differently
create_button("+", lambda: add_to_Calculation("+"), 2, 4, "#FF5733")
create_button("-", lambda: add_to_Calculation("-"), 3, 4, "#FF5733")
create_button("*", lambda: add_to_Calculation("*"), 4, 4, "#FF5733")
create_button("/", lambda: add_to_Calculation("/"), 5, 4, "#FF5733")
create_button("(", lambda: add_to_Calculation("("), 5, 1, "#FF5733")
create_button(")", lambda: add_to_Calculation(")"), 5, 3, "#FF5733")

# Special buttons
create_button("Clear", clear_calculation, 6, 1, "#FF5733", columnspan=2)
create_button("Enter", evaluate_calculation, 6, 3, "#FF5733", columnspan=2)


# Adding keyboard shortcuts to the calculator
def key_press(event):
    if event.char.isdigit():
        add_to_Calculation(event.char)
    elif event.char in '+-*/().':
        add_to_Calculation(event.char)
    elif event.keysym == 'Return':
        evaluate_calculation()
    elif event.keysym == 'BackSpace':
        clear_calculation()

root.bind("<Key>", key_press)
root.mainloop()