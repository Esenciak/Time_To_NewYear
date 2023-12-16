from datetime import datetime
import tkinter as tk

def liczenie():
    dzis = datetime.now()
    sylwester = datetime(dzis.year + 1, 1, 1)
    swieta = datetime(dzis.year,12,24,8,0,0)

    roznica = sylwester - dzis
    roznica_sw = swieta - dzis
    sekundy = roznica.total_seconds()
    sekundy_sw = roznica_sw.total_seconds()
    dni_poz = int(sekundy // (24 * 3600))
    dni_poz_sw = int(sekundy_sw // (24 * 3600))
    godz_poz = int((sekundy % (24 * 3600)) // 3600)
    godz_poz_sw = int((sekundy_sw % (24 * 3600)) // 3600)
    min_poz = int((sekundy % 3600) // 60)
    min_poz_sw = int((sekundy_sw % (24 * 3600)) // 3600)
    sek_poz_reszta = int(sekundy % 60)
    sek_poz_reszta_sw = int(sekundy_sw % 60)



    etykieta.config(text=f"Do sylwestra pozostalo: {dni_poz:.0f} dni, {godz_poz:.0f} godzin, {min_poz:.0f} minut, {sek_poz_reszta:.0f} sekund.\n Do swiat bozego narodzenai zostalo:  {dni_poz_sw:.0f} dni, {godz_poz_sw:.0f} godzin, {min_poz_sw:.0f} minut, {sek_poz_reszta_sw:.0f} sekund.")

    okno.after(1000, liczenie)

def rysuj_choinke():
    wysokosc_choinki = int(entry_wysokosc_choinki.get())

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
    rysuj_choinke()

okno = tk.Tk()
okno.title("Ile do sylwestra by Karol Jablonski")

etykieta = tk.Label(okno, font=("Helvetica", 14), pady=20)
etykieta.pack()

liczenie()


today = datetime.now()
christmas = datetime(today.year, 12, 24)
if today.day == christmas.day and today.month == christmas.month:
    entry_wysokosc_choinki = tk.Entry(okno)
    entry_wysokosc_choinki.pack()

    entry_wysokosc_choinki.insert(0, "5")

    canvas = tk.Canvas(okno, width=400, height=400)
    canvas.pack()

    button_rysuj_choinke = tk.Button(okno, text="Rysuj choinke", command=rysuj_choinke_button)
    button_rysuj_choinke.pack()

okno.mainloop()
