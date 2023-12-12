from ast import For
from datetime import date, datetime
import time
import tkinter as tk

def liczenie():
    dzis = datetime.now()
    sylwester = datetime(dzis.year + 1,1,1)

    roznica = sylwester - dzis

    sekundy = roznica.total_seconds()
    minuty = sekundy/60
    godziny = minuty/60
    dni = roznica.days
    
    dni_poz = int(sekundy // (24 * 3600))
    godz_poz = int((sekundy % (24 * 3600)) // 3600)
    min_poz = int((sekundy % 3600) // 60)
    sek_poz_reszta = int(sekundy % 60)

    etykieta.config(text=f"Do sylwestra pozostalo: {dni_poz:.0f} dni, {godz_poz:.0f} godzin, {min_poz:.0f} minut, {sek_poz_reszta:.0f} sekund. ")
    

    okno.after(1000, liczenie)

def obrazek():
    for wys in []:
        pass



okno = tk.Tk()
okno.title("Ile do sylwestra by Karol Jablonski")

etykieta = tk.Label(okno, font=("Helvetica", 14), pady=20)
etykieta.pack()

liczenie()

okno.mainloop()

    
    







