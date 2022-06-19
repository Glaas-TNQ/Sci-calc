import tkinter as tk
from tkinter import *
import math as m
from decimal import Decimal

# importo anche decimal per non incorrere in strani artefatti di calcolo quando utilizzo numeri con la virgola
# utilizzerò la funzione decimal() all'interno di evaluate()

root = Tk()
root.geometry("400x400")
root.minsize(420, 400)
root.maxsize(420, 400)
root.title("Scientific Calculator")

# il widget entry mi permette di inserire un input, grid mi permette di selezionare
# precisamente riga e colonna dove posizionare il widget
entry = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black", justify='center',
              font='Helvetica 10 bold')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# imposto un campo di input per il numero di decimali da considerare e lo setto di default a 2
n_decimal = Entry(root, width=10, borderwidth=3, relief=RAISED, fg="Red", bg="Black", justify='center',
                  font='Helvetica 10 bold')
n_decimal.insert(-1, 2)
n_decimal.grid(row=7, column=0, padx=10, pady=10)

firma = Entry(root, width=10, borderwidth=3, relief=RAISED, fg="white", bg="Black", justify='center',
              font='Helvetica 10 bold')
firma.insert(-1, "Luca T.")
firma.grid(row=7, column=4, padx=10, pady=10)

"""
Scientific buttons--> function sc
num and math functions--> function click
equal button --> funct evaluate
backspace --> backspace funct
clear button --> clear funct
"""


# Click sarà la mia funzione per l'inserimento di numeri e cifre. Prende il numero attualmente presente in "entry",
# ovvero la mia barra di input, e lo salva come variabile locale. Poi cancella il contenuto di "entry"
# e successivamente inserisce una concatenazione di cifre (Es. 1+0=10)
def click(to_print):
    old = entry.get()
    # 0 to end means dalla posizione 0 alla posizione finale, ovvero-->cancella tutto
    entry.delete(0, END)
    entry.insert(0, old + to_print)
    return


# Clear prende tutto ciò che è in "entry" e lo cancella
def clear():
    entry.delete(0, END)
    return


# Backspace prende "entry", salva il valore come variabile locale in Current, poi calcola length come la lunghezza di
# current -1 (es numero a 3 cifre, current_len=3, length_len=2) e poi cancella con delete solo ciò che rimane fuori,
# quindi sempre l'ultima cifra
def backspace():
    current = entry.get()
    length = len(current) - 1
    entry.delete(length, END)


# Evaluate prende il valore di "entry" e lo salva come ans, poi lo sovrascrive con il risultato della funzione "eval"
# che utilizza ans come argomento. Evaluate prende una stringa come argomento e la valuta dando in output un
# numero intero. Dopodiché come sempre cancello tutto "entry" e lo rimpiazzo con la versiona calcolata di "ans"

def evaluate():
    ans = entry.get()
    ans = eval(ans)
    print(ans)

    # logica per arrotondare a numero intero o a decimale con x cifre
    x = int(n_decimal.get())

    if (str(ans)[-3:] == ".00"):
        ans = round(ans)
    elif (str(ans)[-2:] == ".0"):
        ans = round(Decimal(ans))
    elif ("." in str(ans)):
        ans = round(Decimal(ans), x)

    entry.delete(0, END)
    entry.insert(0, ans)


# Science è una funzione un po' più "complessa" che prende come argomento un evento. L'evento verrà specificato dal
# singolo bottone ma la funzione contiene la logica matematica necessaria per svolgere tutti i calcoli di tipo
# scientifico come logaritmi, potenze ecc.. ||  Utilizzando degli IF andrò a selezionare, in base all'evento
# associato al bottone, la funzione matematica da eseguire

def science(event):
    key = event.widget
    text = key['text']
    no = entry.get()
    result = ''

    if text == 'deg':
        result = str(m.degrees(float(no)))
    if text == 'sin':
        result = str(m.sin(float(no)))
    if text == 'cos':
        result = str(m.cos(float(no)))
    if text == 'tan':
        result = str(m.tan(float(no)))
    if text == 'lg':
        result = str(m.log10(float(no)))
    if text == 'ln':
        result = str(m.log(float(no)))
    if text == 'Sqrt':
        result = str(m.sqrt(float(no)))
    if text == 'x!':
        result = str(m.factorial(float(no)))
    if text == '1/x':
        result = str(1 / (float(no)))
    if text == '^2':
        result = str((float(no) * float(no)))
    if text == 'MOD':
        result = str("mi chiedi troppo")
    if text == 'pi':
        if no == "":
            result = str(m.pi)
        else:
            result = str(float(no) * m.pi)
    if text == 'e':
        if no == "":
            result = str(m.e)
        else:
            result = str(m.e ** float(no))
    entry.delete(0, END)
    entry.insert(0, result)


# seleziono la larghezza del bottone
wid = 2

clear = tk.Button(root, text='C', width=wid, padx=25, pady=10, relief=RAISED, command=clear, bg='Red', fg='White',
                  font='Helvetica 10 bold')
clear.grid(row=3, column=1)

bksp = tk.Button(root, text='bksp', width=wid, padx=25, pady=10, relief=RAISED, command=backspace, bg='Red', fg='White',
                 font='Helvetica 10 bold')
bksp.grid(row=3, column=2)

mod = tk.Button(root, text='MOD', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold',bg='Red', fg='White')
mod.bind('<Button-1>', science)
mod.grid(row=3, column=3)

div = tk.Button(root, text='/', width=wid, padx=25, pady=10, relief=RAISED, command=lambda: click('/'),
                font='Helvetica 10 bold')
div.grid(row=3, column=4)

mult = tk.Button(root, text='*', width=wid, padx=25, pady=10, relief=RAISED, command=lambda: click('*'),
                 font='Helvetica 10 bold')
mult.grid(row=4, column=4)

minus = tk.Button(root, text='-', width=wid, padx=25, pady=10, relief=RAISED, command=lambda: click('-'),
                  font='Helvetica 10 bold')
minus.grid(row=5, column=4)

plus = tk.Button(root, text='+', width=wid, padx=25, pady=10, relief=RAISED, command=lambda: click('+'),
                 font='Helvetica 10 bold')
plus.grid(row=6, column=4)

equal = tk.Button(root, text='=', width=wid, padx=25, pady=10, relief=RAISED, command=evaluate,
                  font='Helvetica 10 bold')
equal.grid(row=7, column=3)

power = tk.Button(root, text='^2', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
power.bind('<Button-1>', science)
power.grid(row=2, column=0)

deg = tk.Button(root, text='deg', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
deg.bind('<Button-1>', science)
deg.grid(row=2, column=1)

sin = tk.Button(root, text='sin', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
sin.bind('<Button-1>', science)
sin.grid(row=2, column=2)

cos = tk.Button(root, text='cos', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
cos.bind('<Button-1>', science)
cos.grid(row=2, column=3)

tan = tk.Button(root, text='tan', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
tan.bind('<Button-1>', science)
tan.grid(row=2, column=4)

lg = tk.Button(root, text='lg', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
lg.bind('<Button-1>', science)
lg.grid(row=1, column=0)

ln = tk.Button(root, text='ln', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
ln.bind('<Button-1>', science)
ln.grid(row=1, column=1)

Sqrt = tk.Button(root, text='SQRT', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
Sqrt.bind('<Button-1>', science)
Sqrt.grid(row=3, column=0)

factorial = tk.Button(root, text='x!', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
factorial.bind('<Button-1>', science)
factorial.grid(row=4, column=0)

fracto = tk.Button(root, text='1/x', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
fracto.bind('<Button-1>', science)
fracto.grid(row=5, column=0)

pi = tk.Button(root, text='pi', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
pi.bind('<Button-1>', science)
pi.grid(row=6, column=0)

e = tk.Button(root, text='e', width=wid, padx=25, pady=10, relief=RAISED, font='Helvetica 10 bold')
e.bind('<Button-1>', science)
e.grid(row=7, column=1)

pleft = tk.Button(root, width=wid, text='(', padx=25, pady=10, relief=RAISED, command=lambda: click('('),
                  font='Helvetica 10 bold')
pleft.grid(row=1, column=2)

pright = tk.Button(root, text=')', width=wid, padx=25, pady=10, relief=RAISED, command=lambda: click(')'),
                   font='Helvetica 10 bold')
pright.grid(row=1, column=3)

dot = tk.Button(root, text='.', width=wid, padx=25, pady=10, relief=RAISED, command=lambda: click('.'),
                font='Helvetica 10 bold')
dot.grid(row=1, column=4)

zero = tk.Button(root, text='0', width=wid, padx=25, pady=10, relief=RAISED, bg='Grey', fg='White',
                 command=lambda: click('0'), font='Helvetica 10 bold')
zero.grid(row=7, column=2)

uno = tk.Button(root, text='1', width=wid, padx=25, pady=10, relief=RAISED, bg='Grey', fg='White',
                command=lambda: click('1'), font='Helvetica 10 bold')
uno.grid(row=6, column=1)

due = tk.Button(root, text='2', width=wid, padx=25, pady=10, relief=RAISED, bg='Grey', fg='White',
                command=lambda: click('2'), font='Helvetica 10 bold')
due.grid(row=6, column=2)

tre = tk.Button(root, text='3', width=wid, padx=25, pady=10, relief=RAISED, bg='Grey', fg='White',
                command=lambda: click('3'), font='Helvetica 10 bold')
tre.grid(row=6, column=3)

quattro = tk.Button(root, text='4', width=wid, padx=25, pady=10, relief=RAISED, bg='Grey', fg='White',
                    command=lambda: click('4'), font='Helvetica 10 bold')
quattro.grid(row=5, column=1)

cinque = tk.Button(root, text='5', width=wid, padx=25, pady=10, relief=RAISED, bg='Grey', fg='White',
                   command=lambda: click('5'), font='Helvetica 10 bold')
cinque.grid(row=5, column=2)

sei = tk.Button(root, text='6', width=wid, padx=25, pady=10, relief=RAISED, bg='Grey', fg='White',
                command=lambda: click('6'), font='Helvetica 10 bold')
sei.grid(row=5, column=3)

sette = tk.Button(root, text='7', width=wid, padx=25, pady=10, relief=RAISED, bg='Grey', fg='White',
                  command=lambda: click('7'), font='Helvetica 10 bold')
sette.grid(row=4, column=1)

otto = tk.Button(root, text='8', width=wid, padx=25, pady=10, relief=RAISED, bg='Grey', fg='White',
                 command=lambda: click('8'), font='Helvetica 10 bold')
otto.grid(row=4, column=2)

nove = tk.Button(root, text='9', width=wid, padx=25, pady=10, relief=RAISED, bg='Grey', fg='White',
                 command=lambda: click('9'), font='Helvetica 10 bold')
nove.grid(row=4, column=3)

root.mainloop()
