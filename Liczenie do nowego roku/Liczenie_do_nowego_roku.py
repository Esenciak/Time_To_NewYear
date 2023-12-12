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

def rysuj_choinke(wysokosc_choinki):
    for i in range(1, min(wysokosc_choinki, 10) + 1):  
        x = (wysokosc_choinki - i) * 20
        y = i * 40
        szerokosc_gwiazdki = 40

        odstep_miedzy_gwiazdkami = 20
        x_gwiazdki = x
        for _ in range(2 * i - 1):
            canvas.create_text(x_gwiazdki, y, text="*", font=("Courier", 14), anchor="w")
            x_gwiazdki += odstep_miedzy_gwiazdkami

    
    canvas.create_rectangle((min(wysokosc_choinki, 10) - 1) * 20 + 15, min(wysokosc_choinki, 10) * 40,
                            (min(wysokosc_choinki, 10) - 1) * 20 + 25, min(wysokosc_choinki, 10) * 40 + 40, fill="brown")

def rysuj_choinke_button():
    wysokosc_choinki = int(entry_wysokosc_choinki.get())
    rysuj_choinke(wysokosc_choinki)

okno = tk.Tk()
okno.title("Ile do sylwestra by Karol Jablonski")

etykieta = tk.Label(okno, font=("Helvetica", 14), pady=20)
etykieta.pack()

label_wysokosc_choinki = tk.Label(okno, text="Wysokosc choinki:")
label_wysokosc_choinki.pack()

entry_wysokosc_choinki = tk.Entry(okno)
entry_wysokosc_choinki.pack()

entry_wysokosc_choinki.insert(0, "5")

canvas = tk.Canvas(okno, width=400, height=400)
canvas.pack()

button_rysuj_choinke = tk.Button(okno, text="Rysuj choinke", command=rysuj_choinke_button)
button_rysuj_choinke.pack()

liczenie()

okno.mainloop()
