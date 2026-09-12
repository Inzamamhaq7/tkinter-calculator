import tkinter

window = tkinter.Tk()
window.title("My Calculator")
window.geometry("400x500")

window.configure(bg="#202124")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)


first_number = None
operator = None
calculation_done = False


def clear_calculator():
    global first_number
    global operator
    global calculation_done

    first_number = None
    operator = None
    calculation_done = False

    display.delete(0, "end")


def backspace():
    current = display.get()
    new_value = current[:-1]
    display.delete(0, "end")
    display.insert("end", new_value)


display = tkinter.Entry(window, font=("Arial", 24), justify="right", bg="#303134", fg="white", insertbackground="white", selectbackground="#5f6368", selectforeground="white", relief="flat", borderwidth=0)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10, sticky="nsew")

clear_button = tkinter.Button(window, text="C", font=("Arial", 18, "bold"), bg="#ea4335", fg="white", activebackground="#c5221f", activeforeground="white", relief="flat", borderwidth=0, command=clear_calculator)
clear_button.grid(row=1, column=2, padx=8, pady=8, sticky="nsew")

backspace_button = tkinter.Button(window, text="<-", font=("Arial", 18, "bold"), bg="#3c4043", fg="white", activebackground="#5f6368", activeforeground="white", relief="flat", borderwidth=0, command=backspace)
backspace_button.grid(row=1, column=3, padx=8, pady=8, sticky="nsew")


def button_clicked(number):
    global first_number
    global operator
    global calculation_done

    if number in ["+", "-", "*", "/"]:
        if display.get() == "":
            return
        first_number = display.get()
        display.delete(0, "end")
        operator = number

    elif number == "=":
        if first_number is None:
            return
        if display.get() == "":
            return

        try:
            first = float(first_number)
            second = float(display.get())
            display.delete(0, "end")

            if operator == "+":
                result = first + second
            elif operator == "-":
                result = first - second
            elif operator == "*":
                result = first * second
            elif operator == "/":
                result = first / second

            if result.is_integer():
                result = int(result)
            display.insert("end", result)
            first_number = result
            calculation_done = True

        except (ValueError, ZeroDivisionError):
            display.delete(0, "end")
            display.insert("end", "Error")

            first_number = None 
            operator = None 
            calculation_done = False

    elif number == ".":
        if "." not in display.get():
            display.insert("end", ".")
    
    else:
        if calculation_done:
            display.delete(0, "end")
            calculation_done = False
        display.insert("end", number)


numbers = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    [".", "0", "/", "="]
]

for row, numbers_in_row in enumerate(numbers):
    for column, number in enumerate(numbers_in_row):
        if number == "=":
            button_bg = "#8ab4f8"
            button_fg = "black"
            button_font = ("Arial", 18, "bold")

        elif number in ["+", "-", "*", "/"]:
            button_bg = "#3c4043"
            button_fg = "white"
            button_font = ("Arial", 18, "bold")

        elif number == ".":
            button_bg = "#3c4043"
            button_fg = "white"
            button_font = ("Arial", 18)

        else:
            button_bg = "#303134"
            button_fg = "white"
            button_font = ("Arial", 18)


        button = tkinter.Button(window, text=number, font=button_font, bg=button_bg, fg=button_fg, activebackground="#5f6368", activeforeground="white", relief="flat", borderwidth=0, command=lambda n=number: button_clicked(n))
        button.grid(row=row + 2, column=column, padx=8, pady=8, ipadx=15, ipady=12, sticky="nsew")

window.mainloop()