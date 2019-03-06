from tkinter import *

# cria uma nova janela
window = Tk()

# seta o título da janela
window.title('Meu programa')

# cria uma entrada de texto
entry_text = Entry(window, width=30)
entry_text.pack()
entry_text.focus_set()

def click_button():
	print(entry_text.get())

btn = Button(window, text='Clique aqui', width=20, command=click_button)
btn.pack()

# seta o tamanho
window.geometry('300x150')

# desenha a janela e inicia a aplicação
window.mainloop()