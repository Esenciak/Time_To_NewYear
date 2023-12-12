
from datetime import datetime
import tkinter as tk

def liczenie():
    dzis = datetime.now()
    sylwester = datetime(dzis.year + 1, 1, 1)

    roznica = sylwester - dzis
    sekundy = roznica.total_seconds()
    minuty = sekundy / 60
    godziny = minuty / 60
    dni_poz = int(sekundy // (24 * 3600))
    godz_poz = int((sekundy % (24 * 3600)) // 3600)
    min_poz = int((sekundy % 3600) // 60)
    sek_poz_reszta = int(sekundy % 60)

    etykieta.config(text=f"Do sylwestra pozostalo: {dni_poz:.0f} dni, {godz_poz:.0f} godzin, {min_poz:.0f} minut, {sek_poz_reszta:.0f} sekund.")

    canvas.after(1000, liczenie)

def rysuj_choinke_button():
    today = datetime.now()
    christmas = datetime(today.year, 12, 24)

    if today.day == christmas.day and today.month == christmas.month:
        wysokosc_choinki = int(entry_wysokosc_choinki.get())
        rysuj_choinke(wysokosc_choinki)

okno = tk.Tk()
okno.title("Ile do sylwestra by Karol Jablonski")

etykieta = tk.Label(okno, font=("Helvetica", 14), pady=20)
etykieta.pack()

entry_wysokosc_choinki = tk.Entry(okno)
entry_wysokosc_choinki.pack()

entry_wysokosc_choinki.insert(0, "5")

canvas = tk.Canvas(okno, width=400, height=400)
canvas.pack()

liczenie()


today = datetime.now()
christmas = datetime(today.year, 12, 24)
if today.day == christmas.day and today.month == christmas.month:
    button_rysuj_choinke = tk.Button(okno, text="Rysuj choinke", command=rysuj_choinke_button)
    button_rysuj_choinke.pack()

okno.mainloop()