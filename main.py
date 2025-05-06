import tkinter as tk

#Criando a janela
janela = tk.Tk()
janela.geometry('1920x1080')
janela.title('Projeto Terraria')

#Texto da interface
texto_janela = tk.Text(janela)
texto_janela.insert(tk.END, 'Bem-vindo ao guia para iniciantes no game Terraria!')
texto_janela.insert(tk.END, 'Terraria é um jogo 2D sandbox extremamente caracteristico e único, tendo o objetivo de derrotar chefões em uma ordem especifica com até quatro classes. Sendo elas:')
texto_janela.pack()

#Botao classe meelee,
botao_meelee = tk.Button(janela, text='Guerreiro', font=fonte, width=20, height=2, bg="#FF5733", fg="#FFFFFF", relief="raised", command=mostrar_classe melee )
botao_meelee.pack(pady=10)

#Botao classe ranged
botao_ranged = tk.Button(janela, text='Atirador', font=fonte, width=20, height=2, bg="#2C3E50", fg="FFFFFF", relief= "raised", command=mostrar_classe ranged)
botao_ranged.pack(pady=10)

#Botao classe mage
botao_mage = tk.Button(janela, text='Mago')
botao_mage.pack(pady=10)

#Botao classe sumonner
botao_sumonner = tk.Button(janela, text='Invocador')
botao_sumonner.pack(pady=10)

janela.mainloop()
