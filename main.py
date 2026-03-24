import tkinter as tk

PI = 3.14159


def calculate_area():
    try:
        shape = area_shape_var.get()

        if shape == "Rechteck":
            a = float(area_entry_a.get())
            b = float(area_entry_b.get())
            area = a * b
            formula = f"A = a · b = {a} · {b}"
        elif shape == "Dreieck":
            a = float(area_entry_a.get())
            h = float(area_entry_b.get())
            area = (a * h) / 2
            formula = f"A = (a · h) / 2 = ({a} · {h}) / 2"
        elif shape == "Kreis":
            r = float(area_entry_a.get())
            area = PI * r * r
            formula = f"A = π · r² = {PI} · {r}²"
        else:
            area_result_label.config(text="Bitte eine Form auswählen.")
            return

        area_result_label.config(text=f"Fläche: {area:.2f}")
        area_formula_label.config(text=f"Formel: {formula}")

    except ValueError:
        area_result_label.config(text="Bitte gültige Zahlen eingeben.")
        area_formula_label.config(text="Formel:")


def update_area_inputs(*args):
    shape = area_shape_var.get()

    if shape == "Kreis":
        area_label_a.config(text="Radius r:")
        area_label_b.config(text="-")
        area_entry_b.delete(0, tk.END)
        area_entry_b.config(state="disabled")
    elif shape == "Rechteck":
        area_label_a.config(text="Seite a:")
        area_label_b.config(text="Seite b:")
        area_entry_b.config(state="normal")
    elif shape == "Dreieck":
        area_label_a.config(text="Grundseite a:")
        area_label_b.config(text="Höhe h:")
        area_entry_b.config(state="normal")


def calculate_volume():
    try:
        body = volume_shape_var.get()

        if body == "Quader":
            a = float(volume_entry_a.get())
            b = float(volume_entry_b.get())
            c = float(volume_entry_c.get())
            volume = a * b * c
        elif body == "Kugel":
            r = float(volume_entry_a.get())
            volume = (4 / 3) * PI * r * r * r
        else:
            volume_result_label.config(text="Bitte einen Körper auswählen.")
            return

        volume_result_label.config(text=f"Volumen: {volume:.2f}")

    except ValueError:
        volume_result_label.config(text="Bitte gültige Zahlen eingeben.")


def update_volume_inputs(*args):
    body = volume_shape_var.get()

    if body == "Kugel":
        volume_label_a.config(text="Radius r:")
        volume_label_b.config(text="-")
        volume_label_c.config(text="-")

        volume_entry_b.delete(0, tk.END)
        volume_entry_c.delete(0, tk.END)
        volume_entry_b.config(state="disabled")
        volume_entry_c.config(state="disabled")
    elif body == "Quader":
        volume_label_a.config(text="Seite a:")
        volume_label_b.config(text="Seite b:")
        volume_label_c.config(text="Seite c:")

        volume_entry_b.config(state="normal")
        volume_entry_c.config(state="normal")


root = tk.Tk()
root.title("Flächen- und Volumenrechner")
root.geometry("820x320")

container = tk.Frame(root)
container.pack(fill="both", expand=True, padx=20, pady=10)

area_frame = tk.Frame(container)
area_frame.grid(row=0, column=0, padx=(0, 20), sticky="n")

volume_frame = tk.Frame(container)
volume_frame.grid(row=0, column=1, padx=(20, 0), sticky="n")

area_shape_var = tk.StringVar(value="Rechteck")
area_shape_var.trace_add("write", update_area_inputs)

volume_shape_var = tk.StringVar(value="Quader")
volume_shape_var.trace_add("write", update_volume_inputs)

# Linke Seite: Flächenrechner
tk.Label(area_frame, text="Form auswählen:").pack(pady=(10, 5))
area_shape_menu = tk.OptionMenu(area_frame, area_shape_var, "Rechteck", "Dreieck", "Kreis")
area_shape_menu.pack()

area_label_a = tk.Label(area_frame, text="Seite a:")
area_label_a.pack(pady=(10, 5))
area_entry_a = tk.Entry(area_frame)
area_entry_a.pack()

area_label_b = tk.Label(area_frame, text="Seite b:")
area_label_b.pack(pady=(10, 5))
area_entry_b = tk.Entry(area_frame)
area_entry_b.pack()

area_calc_button = tk.Button(area_frame, text="Berechnen", command=calculate_area)
area_calc_button.pack(pady=15)

area_result_label = tk.Label(area_frame, text="Fläche:")
area_result_label.pack(pady=5)

area_formula_label = tk.Label(area_frame, text="Formel:")
area_formula_label.pack(pady=5)

# Rechte Seite: Volumenrechner
tk.Label(volume_frame, text="Körper auswählen:").pack(pady=(10, 5))
volume_shape_menu = tk.OptionMenu(volume_frame, volume_shape_var, "Quader", "Kugel")
volume_shape_menu.pack()

volume_label_a = tk.Label(volume_frame, text="Seite a:")
volume_label_a.pack(pady=(10, 5))
volume_entry_a = tk.Entry(volume_frame)
volume_entry_a.pack()

volume_label_b = tk.Label(volume_frame, text="Seite b:")
volume_label_b.pack(pady=(10, 5))
volume_entry_b = tk.Entry(volume_frame)
volume_entry_b.pack()

volume_label_c = tk.Label(volume_frame, text="Seite c:")
volume_label_c.pack(pady=(10, 5))
volume_entry_c = tk.Entry(volume_frame)
volume_entry_c.pack()

volume_calc_button = tk.Button(volume_frame, text="Volumen berechnen", command=calculate_volume)
volume_calc_button.pack(pady=15)

volume_result_label = tk.Label(volume_frame, text="Volumen:")
volume_result_label.pack(pady=5)


update_area_inputs()
update_volume_inputs()

root.mainloop()