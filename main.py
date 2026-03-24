import tkinter as tk
import math


def add_history_entry(text):
    history_listbox.insert(tk.END, text)
    history_listbox.yview_moveto(1.0)


def clear_history():
    history_listbox.delete(0, tk.END)


def calculate():
    try:
        shape = shape_var.get()

        if shape == "Rechteck":
            a = float(entry_a.get())
            b = float(entry_b.get())
            area = a * b
            formula = f"A = a · b = {a} · {b}"
            history_entry = f"Rechteck: {a} * {b} = {area:.2f}"
        elif shape == "Dreieck":
            a = float(entry_a.get())
            h = float(entry_b.get())
            area = (a * h) / 2
            formula = f"A = (a · h) / 2 = ({a} · {h}) / 2"
            history_entry = f"Dreieck: ({a} * {h}) / 2 = {area:.2f}"
        elif shape == "Kreis":
            r = float(entry_a.get())
            area = math.pi * r * r
            formula = f"A = π · r² = {math.pi:.5f} · {r}²"
            history_entry = f"Kreis: π* {r}² = {area:.2f}"
        else:
            result_label.config(text="Bitte eine Form auswählen.")
            return

        result_label.config(text=f"Fläche: {area:.2f}")
        formula_label.config(text=f"Formel: {formula}")
        add_history_entry(history_entry)

    except ValueError:
        result_label.config(text="Bitte gültige Zahlen eingeben.")
        formula_label.config(text="Formel:")


def update_inputs(*args):
    shape = shape_var.get()

    if shape == "Kreis":
        label_a.config(text="Radius r:")
        label_b.config(text="-")
        entry_b.delete(0, tk.END)
        entry_b.config(state="disabled")
    elif shape == "Rechteck":
        label_a.config(text="Seite a:")
        label_b.config(text="Seite b:")
        entry_b.config(state="normal")
    elif shape == "Dreieck":
        label_a.config(text="Grundseite a:")
        label_b.config(text="Höhe h:")
        entry_b.config(state="normal")


root = tk.Tk()
root.title("Flaechenrechner")
root.geometry("640x420")

shape_var = tk.StringVar(value="Rechteck")
shape_var.trace_add("write", update_inputs)

content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_frame = tk.Frame(content_frame)
left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

right_frame = tk.Frame(content_frame)
right_frame.pack(side="right", fill="both", expand=True)

tk.Label(left_frame, text="Form auswählen:").pack(pady=(0, 5))
shape_menu = tk.OptionMenu(left_frame, shape_var, "Rechteck", "Dreieck", "Kreis")
shape_menu.pack()

label_a = tk.Label(left_frame, text="Seite a:")
label_a.pack(pady=(10, 5))
entry_a = tk.Entry(left_frame)
entry_a.pack()

label_b = tk.Label(left_frame, text="Seite b:")
label_b.pack(pady=(10, 5))
entry_b = tk.Entry(left_frame)
entry_b.pack()

calc_button = tk.Button(left_frame, text="Berechnen", command=calculate)
calc_button.pack(pady=15)

result_label = tk.Label(left_frame, text="Fläche:")
result_label.pack(pady=5)

formula_label = tk.Label(left_frame, text="Formel:")
formula_label.pack(pady=5)

history_label = tk.Label(right_frame, text="Berechnungsverlauf:")
history_label.pack(anchor="w", pady=(0, 5))

history_listbox = tk.Listbox(right_frame, height=14)
history_listbox.pack(fill="both", expand=True)

clear_history_button = tk.Button(right_frame, text="Verlauf leeren", command=clear_history)
clear_history_button.pack(pady=(8, 0), anchor="e")

update_inputs()

root.mainloop()