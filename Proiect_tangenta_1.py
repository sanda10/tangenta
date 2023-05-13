import tkinter as tk
from tkinter import messagebox

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def solve_equation(x0, eps, max_iterations, func, func_prime):
    x_prev = x0
    f_prev = func(x_prev)
    iterations = 0

    while True:
        iterations += 1
        f_prime_prev = func_prime(x_prev)

        if f_prime_prev == 0:
            messagebox.showerror("Error", "Derivative is zero.")
            return None

        x_next = x_prev - f_prev / f_prime_prev
        f_next = func(x_next)

        if abs(x_next - x_prev) < eps or abs(f_next) < eps or iterations >= max_iterations:
            return x_next

        x_prev = x_next
        f_prev = f_next

def solve_button_click():
    func = lambda x: float(equation_entry.get())
    func_prime = lambda x: float(derivative_entry.get())
    x0 = float(x0_entry.get())
    eps = float(eps_entry.get())
    max_iterations = int(max_iter_entry.get())

    if not all(map(is_float, [x0, eps])):
        messagebox.showerror("Error", "Invalid input.")
        return

    result = solve_equation(x0, eps, max_iterations, func, func_prime)

    if result is not None:
        result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Tangent Method Solver")

equation_label = tk.Label(root, text="Equation:")
equation_label.grid(row=0, column=0, sticky=tk.W)

equation_entry = tk.Entry(root)
equation_entry.grid(row=0, column=1)

derivative_label = tk.Label(root, text="Derivative:")
derivative_label.grid(row=1, column=0, sticky=tk.W)

derivative_entry = tk.Entry(root)
derivative_entry.grid(row=1, column=1)

x0_label = tk.Label(root, text="Initial value:")
x0_label.grid(row=2, column=0, sticky=tk.W)

x0_entry = tk.Entry(root)
x0_entry.grid(row=2, column=1)

eps_label = tk.Label(root, text="Epsilon:")
eps_label.grid(row=3, column=0, sticky=tk.W)

eps_entry = tk.Entry(root)
eps_entry.grid(row=3, column=1)

max_iter_label = tk.Label(root, text="Max iterations:")
max_iter_label.grid(row=4, column=0, sticky=tk.W)

max_iter_entry = tk.Entry(root)
max_iter_entry.grid(row=4, column=1)

solve_button = tk.Button(root, text="Solve", command=solve_button_click)
solve_button.grid(row=5, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2)

root.mainloop()


