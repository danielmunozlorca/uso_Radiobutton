import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Conversor")
window.geometry ("400x500+700+100")
window.minsize(width=400, height=600)
window.configure (bg="orange")
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

######## FUNCIONES ########

def Ver():
    pelicula_elegida = selected.get()
    if pelicula_elegida == 1:
        resultado = "Terror"
    elif pelicula_elegida == 2:
        resultado = "Western"
    elif pelicula_elegida == 3:
        resultado = "Romántica"
    else:
        resultado = "no elegido"    
    rotulo_resultado.config(text=f"Género seleccionado:\n{resultado}")
    boton_elegir ['state'] = 'disabled'
    boton_reiniciar ['state'] = 'normal'

def Reinicio ():
    selected.set(0)
    rotulo_resultado.config(text=f"Elija tipo de película:")
    boton_elegir ['state'] = 'normal'
    boton_reiniciar ['state'] = 'disabled'
    
###### ROTULO TITULO ########

rotulo_titulo = tkinter.Label(window,
    text="CARTELERA",
    bg= "orange",fg= "black",
    font = "consolas 20 bold",
    relief=tkinter.GROOVE,bd= 2,
    width=18,pady=10)
rotulo_titulo.pack(padx=20,pady=20)


######## CUADRO BOTONES #######
cuadro1 = tkinter.LabelFrame(window,
    bg= "orange",
    width=300,    height=200,
    text="Género favorito",
    font="arial 16 underline")

selected = tkinter.IntVar()

option1 = tkinter.Radiobutton(cuadro1,text='Terror',value='1',variable=selected,bg="orange",font="arial 14")

option2 = tkinter.Radiobutton(cuadro1,text='Western',value='2',variable=selected,bg="orange",font="arial 14")

option3 = tkinter.Radiobutton(cuadro1,text='Romántica',value='3',variable=selected,bg="orange",font="arial 14")

option1.grid(column=0,row=1,pady=5,padx=5,sticky=tkinter.W)
option2.grid(column=0,row=2,pady=5,padx=5,sticky=tkinter.W)
option3.grid(column=0,row=3,pady=5,padx=5,sticky=tkinter.W)

cuadro1.pack()


###### CUADRO PARA BOTONES #####

cuadro2 = tkinter.Frame(window,
    bg = "orange",
    width=800,    height=200)

###### CUADRO PARA BOTONES #######

boton_reiniciar = tkinter.Button(cuadro2,
    text= "Reiniciar",
    font= ("consolas 16 bold"),
    bg="lightgreen",fg="black",
    padx=10,
    width=8,
    state="disabled",
    command=Reinicio)
boton_reiniciar.pack(side = tkinter.LEFT,padx=10,pady=10)    

boton_elegir= tkinter.Button(cuadro2,
    text= "Elegir",
    font= ("consolas",16,"bold"),
    bg="lightgreen",fg="black",
    padx=10,
    width=8,
    command=Ver)
boton_elegir.pack(side = tkinter.LEFT,padx=10,pady=10) 

cuadro2.pack()

rotulo_resultado = tkinter.Label(window,
    text = "Elija tipo de película",
    bg = "lightgreen",fg="black",
    font = "arial 16",
    relief=tkinter.GROOVE,bd=2,
    width=20,height=3,
    pady=10)
rotulo_resultado.pack(padx=20,pady=20)

############  BUCLE PRINCIPAL  ############
window.mainloop()
