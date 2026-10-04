"""
Simple Calculator
A basic desktop calculator built with Python's Tkinter library.

Supports addition, subtraction, multiplication, division, decimals,
clearing, and backspace.

Run with: python calculator.py
"""

import tkinter as tk

BUTTON_LAYOUT = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""],
]


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.configure(bg="#1e1e1e")

        self.expression = ""
        self._build_display()
        self._build_buttons()

    def _build_display(self):
        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Consolas", 24),
            bd=0,
            justify="right",
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20, ipady=10)

    def _build_buttons(self):
        for row_index, row in enumerate(BUTTON_LAYOUT, start=1):
            for col_index, label in enumerate(row):
                if label == "":
                    continue
                btn = tk.Button(
                    self,
                    text=label,
                    font=("Consolas", 18),
                    bg="#333333" if not label.isdigit() else "#2b2b2b",
                    fg="white",
                    activebackground="#444444",
                    bd=0,
                    command=lambda ch=label: self._on_button(ch),
                )
                btn.grid(row=row_index, column=col_index, sticky="nsew", padx=4, pady=4, ipady=12)

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def _on_button(self, char):
        if char == "C":
            self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1]
        elif char == "=":
            self._evaluate()
            return
        else:
            self.expression += char

        self.display_var.set(self.expression if self.expression else "0")

    def _evaluate(self):
        try:
            # Only allow safe characters before evaluating.
            allowed = set("0123456789.+-*/%() ")
            if not self.expression or not set(self.expression) <= allowed:
                raise ValueError("Invalid expression")
            result = eval(self.expression, {"__builtins__": {}})
            self.display_var.set(str(result))
            self.expression = str(result)
        except (ZeroDivisionError, ValueError, SyntaxError):
            self.display_var.set("Error")
            self.expression = ""


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
