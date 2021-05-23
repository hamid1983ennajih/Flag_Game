from tkinter import *
from random import *

def action():
    N= int(entrynbre1.get())
    N2= 2*N
    entrynbre2.delete(0, END)
    entrynbre2.insert(0, N2)
def start():

    pays= [photo1, photo2,photos3]
          #Egypte.png, Mauritanie.png,Soudan.png, Eritrea.png, Mali.png,Djibouti.png, Ethiopie.png]
    Drapeau = random.choice(pays)

    photo1 = PhotoImage("Maroc.png")
    photo2 = PhotoImage("Algerie.png")
    photo3 = PhotoImage("Tunisie.png")
    label_photo = Label(fen, image=photo)
    label_photo.place(x=300, y=200)




fen = Tk()
fen.title("Calcule du Double")
fen.geometry("700x500")
fen.minsize(480, 360)
fen.iconbitmap("logo.ico")
lbl1=Label(fen, text= "Flag Game", font=("Monotype Corsiva", 30), bg="#41B77F",
           fg="red", bd=2, relief= SUNKEN)
lbl1.pack()

lbl2= Button(fen, text = " Start Game", font=("Sakkal Majalla", 15), bg= "yellow",
             fg="red", bd=5, relief= RAISED, command= start)
lbl2.place(x= 315, y= 80)

lbl3=Label(fen, text = " C'est le drapeau du :")
lbl3.place(x= 200, y= 380)
entrynbre3= Entry(fen)
entrynbre3.place(x= 350, y= 380)

Calculer= Button(fen, text= "calculer le double", command= action)
Calculer.place(x= 350, y= 420)
fen.config(background="#41B77F")
fen.mainloop()