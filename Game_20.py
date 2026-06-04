import tkinter as tk
from tkinter import font
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#2d2d2d")
        
        # Variables
        self.display_var = tk.StringVar(value="0")
        self.current_input = "0"
        self.operator = None
        self.previous_value = None
        self.should_reset = False
        
        # Create UI
        self.create_display()
        self.create_buttons()
    
    def create_display(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="#2d2d2d", pady=10)
        display_frame.pack(fill=tk.BOTH, padx=10)
        
        # Display label
        display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 32, "bold"),
            bg="#1a1a1a",
            fg="#00ff00",
            anchor="e",
            padx=15,
            pady=20
        )
        display_label.pack(fill=tk.BOTH, expand=True)
    
    def create_buttons(self):
        # Button frame
        button_frame = tk.Frame(self.root, bg="#2d2d2d", padx=10, pady=10)
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button layout
        buttons = [
            ("AC", 0, 0, 2, "#e74c3c"),
            ("DEL", 0, 2, 1, "#f39c12"),
            ("/", 0, 3, 1, "#667eea"),
            
            ("7", 1, 0, 1, "#ecf0f1"),
            ("8", 1, 1, 1, "#ecf0f1"),
            ("9", 1, 2, 1, "#ecf0f1"),
            ("*", 1, 3, 1, "#667eea"),
            
            ("4", 2, 0, 1, "#ecf0f1"),
            ("5", 2, 1, 1, "#ecf0f1"),
            ("6", 2, 2, 1, "#ecf0f1"),
            ("-", 2, 3, 1, "#667eea"),
            
            ("1", 3, 0, 1, "#ecf0f1"),
            ("2", 3, 1, 1, "#ecf0f1"),
            ("3", 3, 2, 1, "#ecf0f1"),
            ("+", 3, 3, 1, "#667eea"),
            
            ("0", 4, 0, 2, "#ecf0f1"),
            (".", 4, 2, 1, "#ecf0f1"),
            ("=", 4, 3, 1, "#27ae60"),
        ]
        
        for (text, row, col, colspan, color) in buttons:
            self.create_button(button_frame, text, row, col, colspan, color)
    
    def create_button(self, frame, text, row, col, colspan, color):
        button = tk.Button(
            frame,
            text=text,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white" if color != "#ecf0f1" else "#2d2d2d",
            activebackground="lightgray" if color == "#ecf0f1" else "#555555",
            activeforeground="black" if color == "#ecf0f1" else "white",
            bd=0,
            padx=20,
            pady=20,
            command=lambda: self.on_button_click(text)
        )
        
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights
        frame.grid_rowconfigure(row, weight=1)
        frame.grid_columnconfigure(col, weight=1)
    
    def on_button_click(self, value):
        if value == "AC":
            self.clear_display()
        elif value == "DEL":
            self.delete_last()
        elif value == "=":
            self.calculate()
        elif value in "+-*/%":
            self.append_operator(value)
        else:
            self.append_number(value)
    
    def append_number(self, num):
        if self.should_reset:
            self.current_input = num
            self.should_reset = False
        else:
            if self.current_input == "0" and num != ".":
                self.current_input = num
            elif num == "." and "." in self.current_input:
                return
            else:
                self.current_input += num
        
        self.update_display()
    
    def append_operator(self, op):
        if self.operator is not None and not self.should_reset:
            self.calculate()
        
        self.previous_value = float(self.current_input)
        self.operator = op
        self.should_reset = True
    
    def calculate(self):
        if self.operator is None or self.previous_value is None:
            return
        
        try:
            current = float(self.current_input)
            
            if self.operator == "+":
                result = self.previous_value + current
            elif self.operator == "-":
                result = self.previous_value - current
            elif self.operator == "*":
                result = self.previous_value * current
            elif self.operator == "/":
                if current == 0:
                    self.display_var.set("Error: Div by 0")
                    return
                result = self.previous_value / current
            elif self.operator == "%":
                result = self.previous_value % current
            
            # Format result
            if result == int(result):
                self.current_input = str(int(result))
            else:
                self.current_input = str(round(result, 10))
            
            self.operator = None
            self.previous_value = None
            self.should_reset = True
            self.update_display()
        
        except Exception as e:
            self.display_var.set("Error")
    
    def clear_display(self):
        self.current_input = "0"
        self.operator = None
        self.previous_value = None
        self.should_reset = False
        self.update_display()
    
    def delete_last(self):
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = "0"
        self.update_display()
    
    def update_display(self):
        self.display_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
