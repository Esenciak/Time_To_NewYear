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

def obrazek(wysokosc_choinki):
    okno.delete("all")
    for i in range(1, wysokosc_choinki + 1):
        x = (wysokosc_choinki - i) * 20  # 
        y = i * 40
        szerokosc_gwiazdki = 40
        
        okno.create_text(x, y, text="*" * (2*i - 1), font=("Courier", 14), anchor="w")

    okno.create_rectangle((wysokosc_choinki - 1) * 20 + 15, wysokosc_choinki * 40, (wysokosc_choinki - 1) * 20 + 25, wysokosc_choinki * 40 + 40, fill="brown")

def rysuj_choinke_button():
    wysokosc_choinki = int(entry_wysokosc_choinki.get())
    rysuj_choinke(wysokosc_choinki)


okno = tk.Tk()
okno.title("Ile do sylwestra by Karol Jablonski")

etykieta = tk.Label(okno, font=("Helvetica", 14), pady=20)
etykieta.pack()

liczenie()

okno.mainloop()

    
    







