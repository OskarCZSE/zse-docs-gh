"""
Zaawansowane GUI Ttk
Moduł z dwoma zakładkami
"""


import tkinter as tk
from tkinter import ttk

def show_selection(event):
    """
    Wyświetla zaznaczony element w konsoli

    Args:
        event (tk.Event): Event triggerowany w momencie wykonania funkcji.
    
    Returns:
        None
    """
    print(combo.get())

def start_progress():
    pbar.start(10)
    status_label.config(text="Status: Proces trwa...")

def stop_progress():
    pbar.stop()
    status_label.config(text="Status: Proces zakończony.")

def save_settings():
    start_progress()
    root.after(3000, complete_save)

def complete_save():
    stop_progress()
    print("Ustawienia zapisane!")

root = tk.Tk()
root.title("Zaawansowane GUI Ttk")

# --- 1. Notebook (Karty) ---
notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10, expand=True, fill="both")

tab1 = ttk.Frame(notebook, padding="10")
tab2 = ttk.Frame(notebook, padding="10")

notebook.add(tab1, text="Karta 1: Wygląd")
notebook.add(tab2, text="Karta 2: Prywatność")

# --- Zawartość Karty 1 (Combobox) ---
ttk.Label(tab1, text="Wybierz motyw:").grid(row=0, column=0, padx=5, pady=5, sticky="w")

motyw = ["Jasny", "Ciemny", "Systemowy"]
combo = ttk.Combobox(tab1, values=motyw, state="readonly")
combo.current(0)
combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
checkbutton = ttk.Checkbutton(tab1, text="Włącz Wysoki Kontrast")
checkbutton.grid(row=1, column=0, padx=5, pady=5, sticky="w")

combo.bind("<<ComboboxSelected>>", show_selection)

# --- Zawartość Karty 2 (Progressbar) ---
status_label = ttk.Label(tab2, text="Status: Oczekuje")
status_label.pack(pady=10)

pbar = ttk.Progressbar(tab2, orient="horizontal", length=300, mode="indeterminate")
pbar.pack(pady=10)

sharing_var = tk.StringVar(value="Ani")
ttk.Label(tab2, text="Wybierz poziom udostępniania danych:").pack(pady=5)
ttk.Radiobutton(tab2, text="Wszystkie", variable=sharing_var, value="Wszystkie").pack(anchor='w')
ttk.Radiobutton(tab2, text="Anonimowe", variable=sharing_var, value="Anonimowe").pack(anchor='w')
ttk.Radiobutton(tab2, text="Żadne", variable=sharing_var, value="Żadne").pack(anchor='w')

ttk.Button(tab2, text="Zapisz Ustawienia", command=save_settings).pack(pady=10)

root.mainloop()
