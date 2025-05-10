import tkinter as tk
from tkinter import tkk, messagebox

def mostar_texto(texto_widget, conteudo):
 texto_widget.delete("1.0", tk.END
 texto_widget.insert(tk.END, conteudo)

def buscar():
 termo = barra_busca.get().strip().lower()
 if not termo: 
  mesagebox.showwarning("Aviso", "Digite um termo para pesquisar.")
  return

if "guerreiro" in termo:
 notebook.select(aba_guerreiro)
elif "atirador" in termo:
 notebook.select(aba_atirador)
elif "mago" in termo:
 notebook.select(aba_mago)
elif "invocador" in termo:
 notebook.select(aba_invocador)
else: messagebox.showinfo("resultado", "classe não encontrada,")

def mostrar_classe_melee():
 texto_janela.delete(1.0, tk.END)
  texto_janela.insert(tk.END, 'O Guerreiro é uma classe focada no combate corpo a corpo, com grande resistência e dano físico.' ) 

def mostrar_calsse_ranged():
texto_janela.delete(1.0, tk.END)
texto_janela.insert(tk.END, 'O Atirador usa armas a distancia, como arcos, armas de fogo e armas de aremeço.')

def mostrar_calsse_mage():
 texto_janela.delete(1.0, tk.END)
texto_janela.insert(tk.END, 'O Mago utiliza feitiços e magias para causar dano a distancia atraves de varios cajados forjados ou encontrados apos a derrota de certos mobs')

def mostrar_calsse_Sumonner():
 texto_janela.delete(1,0, tk.END)
texto_janela.insert(tk.END, 'O Invocador usa criaturas magicas e chicotes para infligir dano, além do chicote causar dano ele também mostras as criatura invocadas qual mob ele deve atacar primeiro, da buff de dano as criaturas de acordo com o material)

def buscar():
termo = barra_busca.get().strip().lower()
if not termo:
messegebox.showwarning("Aviso", "Digite um termo para pesquisar.")
return
if "guerreiro" in termo:
mostrar_classe_melee()
elif "atirador" in termo:
mostrar_classe_ranged()
elif "mago" in termo: 
mostrar_classe_mage()
elif "invocador" in termo:
mostrar_classe_summoner():
else:
messagebox.showinfo("resultado", "classe não encontrada.")
                    
#Criando a janela
janela = tk.Tk()
janela.geometry('1920x1080')
janela.title('Projeto Terraria')

imagem = Image.open("Terraria.png")
imagem = image.resize((800, 600))
fundo = imageTkphotoImagem(imagem)

fundo_label = tklabel(janela, imagem=fundo)
fundo_label =place(x=0, y=0 relwidth=1, relheoght=1)

container = Tk.frame(janela, bg="white")
container.placer(relx=0.05, rely=0.05, relwidth=0.9, relheoght=0.9)

Fonte = ("Arial",12)

Notebook = tkk.notbook(janela)
Notebook.pack(expand=True, fill='both')

aba_inicio = tk .Frame(notebook)
notebook.add(aba.inicio, text='Inicio')

Texto_inicio = tk.Frame(notebook)
notebook.add(aba_inicio, text='Inicio')

texto_inicio = tk.Text(aba_inicio, wrap="word", font= fonte)
text_inicio.insert(tk.END, " Bem-vindo ao guia para no game Terraria!/n/n"
"Teraria é um jogo 2D sandbox único, onde você emfrenta chefes em uma ordem específica usando uma das quatro classes principais: /n" 

#Texto da interface
texto_janela = tk.Text(janela)
texto_janela.insert(tk.END, 'Bem-vindo ao guia para iniciantes no game Terraria!')
texto_janela.insert(tk.END, 'Terraria é um jogo 2D sandbox extremamente caracteristico e único, tendo o objetivo de derrotar chefões em uma ordem especifica com até quatro classes. Sendo elas:')
texto_janela.pack()

#Botao classe meelee,
botao_meelee = tk.Button(janela, text='Guerreiro', font=fonte, width=20, height=2, bg="#FF5733", fg="#FFFFFF", relief="raised", command=mostrar_classe_melee)
botao_meelee.pack(pady=10)

#Botao classe ranged
botao_ranged = tk.Button(janela, text='Atirador', font=fonte, width=20, height=2, bg="#2C3E50", fg="FFFFFF", relief= "raised", command=mostrar_classe_ranged)
botao_ranged.pack(pady=10)

#Botao classe mage
botao_mage = tk.Button(janela, text='Mago', font=fonte, width=20, height2, bg="#800080", fg="FFFFFF", relief= "raised", command=mostrar_classe_mage)
botao_mage.pack(pady=10)

#Botao classe sumonner
botao_sumonner = tk.Button(janela, text='Invocador', font=fonte, widht=20, height2, bg"#FFFF00", relief "raised", command=mostar_classe_sumonner)
botao_sumonner.pack(pady=10)

janela.mainloop()
