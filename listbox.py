import tkinter
from tkinter import ttk

window = tkinter.Tk()
#window.title("Conversor")
window.geometry ("400x500+700+100")
#window.minsize(width=400, height=600)
#window.configure (bg="yellow")
window.columnconfigure(0,weight =1)
window.columnconfigure(1,weight =3)

#restaurante_menu = ttk.Label(window,text="MENU DE HOY:")
#restaurante_menu.grid(column=0,row=0,sticky=tkinter.W,padx=10,pady=10)

label_tituloR = ttk.Label(window,
    text="Restaurante \n 'Donde Danisha'",
    #tkinter.bg == "orange",tkinter.fg == "black",
    font = "Arial 18 bold")
    #relief=tkinter.GROOVE,bd= 2,
    #width=18,pady=10)
#label_titulo.pack(ipadx=20,ipady=20)
label_tituloR.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)

label_titulo = ttk.Label(window,
    text="MENU DE HOY:",
    #tkinter.bg == "orange",tkinter.fg == "black",
    font = "consolas 18 bold")
    #relief=tkinter.GROOVE,bd= 2,
    #width=18,pady=10)
#label_titulo.pack(ipadx=20,ipady=20)
label_titulo.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)



Lista = ['Cazuela  $2.890','Pollo asado  $3.000','Pescado frito  $2.500','Carne mechada  $3.200','Porotos $1.500','Palta reina $8.000']
Lista_items = tkinter.StringVar(value=Lista)
Listbox = tkinter.Listbox(window,height=15,width=30,listvariable=Lista_items,font = "consolas 13 bold")
Listbox.grid(column=0,row=2,sticky=tkinter.W)

window.mainloop()