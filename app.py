import tkinter as tk
from PIL import Image, ImageTk

# Definindo conteúdo interno da janela do programa
root = tk.Tk()

canvas = tk.Canvas(root, width=1280, height=720)
# Para um design em um grid em 3 colunas
canvas.grid(columnspan=3)

#logo
logo = Image.open('assets/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo_label
logo_label.grid(column=0, row=0)



# Definindo limite do conteúdo interno do programa
root.mainloop()