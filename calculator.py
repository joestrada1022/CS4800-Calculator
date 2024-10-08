import tkinter as tk
import google.generativeai as genai
import os
from dotenv import load_dotenv

if not load_dotenv():
    print("Error loading .env file")
    exit(1)
genai.configure(api_key=os.getenv("api_key"))

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()
chat.history.clear()

chat.send_message(
    "I have a few requirements for this conversation. take note of them all"
)
chat.send_message("if the expression is invalid in any way print out invalid")
chat.send_message("assume log is in base 10")
chat.send_message(
    "for the rest of this conversation, only print out the answer to the expression. if undefined print undefined"
)

calculation = ""


def add_to_calculation(symbol):
    text_result.configure(state="normal")
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    text_result.configure(state="disabled")


def evaluate_calculation():
    text_result.configure(state="normal")
    global calculation
    try:
        response = chat.send_message(calculation)
        calculation = str(response.text).replace("\n", "").strip()
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
    text_result.configure(state="disabled")


def clear_field():
    text_result.configure(state="normal")
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    text_result.configure(state="disabled")


root = tk.Tk(screenName="Calculator")
root.geometry("300x350")

text_result = tk.Text(
    root, height=2, width=17, font=("Arial", 24), bg="#7E8082", state="disabled"
)
text_result.grid(columnspan=6)


btn_clear = tk.Button(
    root,
    text="C",
    command=clear_field,
    width=11,
    font=("Arial", 14),
    bg="#D23030",
)
btn_clear.grid(row=1, column=1, columnspan=2)
btn_exp = tk.Button(
    root,
    text="^",
    command=lambda: add_to_calculation("^"),
    width=5,
    font=("Arial", 14),
)
btn_exp.grid(row=1, column=3)

btn_sin = tk.Button(
    root,
    text="sin",
    command=lambda: add_to_calculation("sin"),
    width=5,
    font=("Arial", 14),
)
btn_sin.grid(row=1, column=4)

btn_cos = tk.Button(
    root,
    text="cos",
    command=lambda: add_to_calculation("cos"),
    width=5,
    font=("Arial", 14),
)
btn_cos.grid(row=2, column=1)

btn_tan = tk.Button(
    root,
    text="tan",
    command=lambda: add_to_calculation("tan"),
    width=5,
    font=("Arial", 14),
)
btn_tan.grid(row=2, column=2)

btn_log = tk.Button(
    root,
    text="log",
    command=lambda: add_to_calculation("log"),
    width=5,
    font=("Arial", 14),
)
btn_log.grid(row=2, column=3)

btn_ln = tk.Button(
    root,
    text="ln",
    command=lambda: add_to_calculation("ln("),
    width=5,
    font=("Arial", 14),
)
btn_ln.grid(row=3, column=1)

btn_e = tk.Button(
    root,
    text="e",
    command=lambda: add_to_calculation("e^("),
    width=5,
    font=("Arial", 14),
)
btn_e.grid(row=2, column=4)

btn_open = tk.Button(
    root,
    text="(",
    command=lambda: add_to_calculation("("),
    width=5,
    font=("Arial", 14),
)
btn_open.grid(row=3, column=2)

btn_close = tk.Button(
    root,
    text=")",
    command=lambda: add_to_calculation(")"),
    width=5,
    font=("Arial", 14),
)
btn_close.grid(row=3, column=3)

btn_plus = tk.Button(
    root,
    text="+",
    command=lambda: add_to_calculation("+"),
    width=5,
    font=("Arial", 14),
)
btn_plus.grid(row=3, column=4)

btn_minus = tk.Button(
    root,
    text="-",
    command=lambda: add_to_calculation("-"),
    width=5,
    font=("Arial", 14),
)
btn_minus.grid(row=4, column=4)

btn_mult = tk.Button(
    root,
    text="*",
    command=lambda: add_to_calculation("*"),
    width=5,
    font=("Arial", 14),
)
btn_mult.grid(row=5, column=4)

btn_div = tk.Button(
    root,
    text="/",
    command=lambda: add_to_calculation("/"),
    width=5,
    font=("Arial", 14),
)
btn_div.grid(row=6, column=4)

btn_1 = tk.Button(
    root,
    text="1",
    command=lambda: add_to_calculation(1),
    width=5,
    font=("Arial", 14),
)
btn_1.grid(row=4, column=1)

btn_2 = tk.Button(
    root,
    text="2",
    command=lambda: add_to_calculation(2),
    width=5,
    font=("Arial", 14),
)
btn_2.grid(row=4, column=2)

btn_3 = tk.Button(
    root,
    text="3",
    command=lambda: add_to_calculation(3),
    width=5,
    font=("Arial", 14),
)
btn_3.grid(row=4, column=3)

btn_4 = tk.Button(
    root,
    text="4",
    command=lambda: add_to_calculation(4),
    width=5,
    font=("Arial", 14),
)
btn_4.grid(row=5, column=1)

btn_5 = tk.Button(
    root,
    text="5",
    command=lambda: add_to_calculation(5),
    width=5,
    font=("Arial", 14),
)
btn_5.grid(row=5, column=2)

btn_6 = tk.Button(
    root,
    text="6",
    command=lambda: add_to_calculation(6),
    width=5,
    font=("Arial", 14),
)
btn_6.grid(row=5, column=3)

btn_7 = tk.Button(
    root,
    text="7",
    command=lambda: add_to_calculation(7),
    width=5,
    font=("Arial", 14),
)
btn_7.grid(row=6, column=1)

btn_8 = tk.Button(
    root,
    text="8",
    command=lambda: add_to_calculation(8),
    width=5,
    font=("Arial", 14),
)
btn_8.grid(row=6, column=2)

btn_9 = tk.Button(
    root,
    text="9",
    command=lambda: add_to_calculation(9),
    width=5,
    font=("Arial", 14),
)
btn_9.grid(row=6, column=3)

btn_0 = tk.Button(
    root,
    text="0",
    command=lambda: add_to_calculation(0),
    width=5,
    font=("Arial", 14),
)
btn_0.grid(row=7, column=2)

btn_decimal = tk.Button(
    root,
    text=".",
    command=lambda: add_to_calculation("."),
    width=5,
    font=("Arial", 14),
)
btn_decimal.grid(row=7, column=1)

btn_equals = tk.Button(
    root,
    text="=",
    command=evaluate_calculation,
    width=11,
    font=("Arial", 14),
    bg="#43A047",
)
btn_equals.grid(row=7, column=3, columnspan=2)

root.mainloop()
