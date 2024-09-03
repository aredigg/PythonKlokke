# PythonKlokke
# © 2024 Are Digranes

import tkinter as tk
import datetime, time
from math import floor, pi as pi, sin as sin, cos as cos

BASE_SEKUNDER = 1_000_000_000
BASE_MINUTTER = 60*BASE_SEKUNDER
BASE_TIMER = 60*BASE_MINUTTER
BASE_KLOKKE = 12*BASE_TIMER

SKJERM_MARGIN = 160
MARGIN = 10

VISER_LENGDE_TIMER = 0.6
VISER_LENGDE_MINUTTER = 0.8
VISER_LENGDE_SEKUNDER = 0.9
KLOKKE_SENTER = 0.05

OPPDATERING = 10

root = tk.Tk()
visere = []
størrelse = min(root.winfo_screenwidth(), root.winfo_screenheight())-SKJERM_MARGIN
midtpunkt = størrelse/2
canvas = tk.Canvas(root, width=størrelse, height=størrelse)
tidssone_avvik = (-time.altzone if time.daylight else -time.timezone)*BASE_SEKUNDER

def main():
    root.title("PythonKlokke")
    canvas.pack(anchor=tk.CENTER, expand=True)
    oval = canvas.create_oval(MARGIN,MARGIN,størrelse-MARGIN,størrelse-MARGIN,fill="black")
    visere.append(canvas.create_line(0,0,0,0,width=10))     # time
    visere.append(canvas.create_line(0,0,0,0,width=10))     # minutt
    visere.append(canvas.create_line(0,0,0,0,fill="red"))   # sekund
    v0 = midtpunkt-(midtpunkt*KLOKKE_SENTER)
    v1 = midtpunkt+(midtpunkt*KLOKKE_SENTER)
    oval = canvas.create_oval(v0,v0,v1,v1,fill="black")     # senter
    oppdater_visere()
    root.mainloop()

def viser(viser, vinkel, radius, midtpunkt):
    canvas.coords(viser, midtpunkt, midtpunkt, midtpunkt+radius*sin(vinkel), midtpunkt-radius*cos(vinkel))

def oppdater_visere():
    # time-viser
    radius = midtpunkt*VISER_LENGDE_TIMER
    tid = tidssone_avvik + time.time_ns() % BASE_KLOKKE
    vinkel = 2*pi*tid/BASE_KLOKKE
    viser(visere[0], vinkel, radius, midtpunkt)
    # minutt-viser
    radius = midtpunkt*VISER_LENGDE_MINUTTER
    tid = tid % BASE_TIMER
    vinkel = 2*pi*tid/BASE_TIMER
    viser(visere[1], vinkel, radius, midtpunkt)
    # sekund-viser
    radius = midtpunkt*VISER_LENGDE_SEKUNDER
    tid = tid % BASE_MINUTTER
    vinkel = 2*pi*tid/BASE_MINUTTER
    viser(visere[2], vinkel, radius, midtpunkt)
    root.after(OPPDATERING, oppdater_visere)

if __name__ == "__main__":
    main()
