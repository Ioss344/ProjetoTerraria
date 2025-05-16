import tkinter as tk
from tkinter import ttk

def semcomando():
    print("Semcomando")

#Definicao para mostrar a janela
def subirjanela(frame):
    frame.tkraise()

#funcao que cria frame com canvas e implementa scrollbar
def criarframescroll(root):
    frame_base = tk.Frame(root)
    canvas = tk.Canvas(frame_base)
    scrollbar = tk.Scrollbar(frame_base, orient='vertical', command=canvas.yview)
    framecomscroll = tk.Frame(canvas)

    #Fazendo o scrollbar acompanhar as mudancas no app
    framecomscroll.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #Colocando o frame de conteudo dentro do canva
    canvas.create_window((0,0), window=framecomscroll, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    return frame_base, canvas, framecomscroll

# Criando a janela principal
janela = tk.Tk()
janela.title('Terraria')
janela.geometry('700x500')

#Base de todas as paginas
base_frame = tk.Frame(janela)
base_frame.pack(fill="both", expand=True)

#Criando os frames de classes
frame_inicial_base, _, frame_inicial = criarframescroll(base_frame)
frame_melee_base, _, frame_melee = criarframescroll(base_frame)
frame_ranged_base, _, frame_ranged = criarframescroll(base_frame)
frame_mage_base, _, frame_mage = criarframescroll(base_frame)
frame_sumonner_base, _, frame_sumonner = criarframescroll(base_frame)

#Criando o "ocultandor de janelas" (frames)
for frame in (frame_inicial_base, frame_melee_base, frame_ranged_base, frame_mage_base, frame_sumonner_base):
    frame.place(x=0, y=0, width=700, height=500)

#Pesonalizando o frame inicial
textoinicial = tk.Label(frame_inicial, text='Bem vindo ao guia para principiantes do Terraria!\n', font= ('Andy Negrito', '20', 'bold', 'underline' ))
textoinicial1 = tk.Label(frame_inicial, text='Cave, Lute e Construa! \nO mundo está ao seu alcance enquanto você luta por sobrevivência, fortuna e glória. Mergulhe em extensões cavernosas, busque inimigos cada vez maiores para testar sua coragem em combate ou construa sua própria cidade - no mundo de Terraria,a escolha é sua! \n\nCombinando elementos de jogos de ação clássicos com a liberdade da criatividade no estilo sandbox, Terraria é uma experiência de jogo única, onde tanto a jornada quanto o destino são tão únicos (e exóticos) quanto os próprios jogadores! \n\n No jogo o mundo é seu, faça suas escolhas e desbrave o universo terrariano, o ambiente é seu deleite! Nesse universo é possível de tudo, até mesmo atirar uma uma arma de abelhas, vestido de abelha, em cima de uma abelha! \n\n A gameplay do jogo é relativamente simples, porém não deixa a desejar em dificuldade e mecânicas de jogabilidade, o mundo possui um visual caracteristico e simples, sendo um mundo 2D com um visual pixelado bem característico.' ,
font= ('Andy Negrito', '14'),
wraplength=650,
justify='center' )
textoinicial.pack(pady= 10)
textoinicial1.pack(pady= 15)

#Personalizando o frame melee
textomelee = tk.Label(frame_melee, text='Guerreiro', font= ('Andy Negrito', '20', 'bold', 'underline'))
textomelee1 = tk.Label(frame_melee, text='A escolha mais escolha mais clássica e mais segura dentre todos os jogos, não tem como errar quando se trata de um bom e velho guerreiro, e no Terraria não iria ser diferente. \n\n Possuindo um arsenal diverso, variando de espadas que poden lançar projetéis, ou não, foicez, adagas, boomerangues, chakrans, Io-Iôs e mais uma penca de armas e armaduras extremament fortes, atualmente o guerreiro é a classe com o arsenal mais tank, completo e variado do jogo. \n\n Infelizmente rosas possuem espinhos, a classe possui uma progressão lenta, podendo sofrer nas fases inciais do pre-hardmode por não possuis um alcance consistente no começo da gameplay, mas caso você persista por esses desafios as recompensas são gloriósas! O guerreiro, após  passar pelas fases inciais do game se torna uma fortaleza impenetrável, com muito dano e vida, sendo uma classe muito popular por todos, de veteranos, verdadeiros intímos do universo terrariano, ou iniciantes que buscam uma gameplay mais amigável e relativamente simples. ',
font= ('Andy Negrito', '14'),
wraplength=650,
justify='center')
textomelee.pack(pady= 10)
textomelee1.pack(pady= 15)

#Personalizando o frame ranged
textoranged = tk.Label(frame_ranged, text='Atirador', font= ('Andy Negrito', '20', 'bold', 'underline'))
textoranged1 = tk.Label(frame_ranged, text='A classe mais original do terraria, o atirador, essa classe foge dos arquetipos comuns dos rpgs clássicos, pois se tretaria de uma fusão entre a classe gunner (especialista com armas) e o padrão arqueiro, seu arsenal varia entre arcos, armas, shurikens, adagas arremesáveis e bombas, como grandadas e mísseis. \n\nEste arquétipo é o com mais potêncial de dano do jogo possível, sendo tembém uma ótima escolha para novos jogadores, por possuir um alcance enorme e um dano capaz de obliterar a maioria dos inimigos do jogo facilmente.\n\n A classe possui uma defensa balanceada e alto poder ofensivo, onde se desempenha bem com multidões e alvos únicos ela faz uso de municões para poder utilizar suas armas, como flechas, balas e suas variantes, gel, bolas de neve e até mesmo estrelas! Uma das mecânicas extras da classe é o fato do atirador poder posicionar armadilhas que escalam com seu dano, como as bolas de espinho e as minas.\n\n Sua progressão é bem uniforme, possuiuma gama ampla de acessórios e armas, alem do fato de serem de fácil obtenção, uma vez que a maioria de suas bugingangas sao obtidas por chefões os quais fazem parte da trajetória natural do mundo , ou seja, para o atirador atingir seu potencial máximo não são necessários muitos desvios de exploração ou pesca, como em outras classes.',
font=('Andy Negrito', '14'),
wraplength=650,
justify='center' )
textoranged.pack(pady= 10)
textoranged1.pack(pady= 15)

#Personalizado o frame mage
textomage = tk.Label(frame_mage, text='Mago', font= ('Andy Negrito', '20', 'bold', 'underline'))
textomage1 = tk.Label(frame_mage, text='O famoso e famigerado mago, clásico dos rpgs de turno. No Terraria a classe se sobresai com a classe mais versátil do jogo, pois suas armas são dotadas de diferentes mecânicas, sendo capazes de lançarem arco-íris fofinhos, ou talvez criarem uma nebulosa que é capaz de debilitar toda a vida pelo seu trajeto, essa é a versalidade da magia desse mundo!\n\n O mago é especialista em causar dano a ditância, possuindo uma amplitude de armas para as mais diversas situações, podendo usar cetros, grimórios, cajados e até objetos amaldiçados para causar um dano supreendente, tanto em situações com muitos inimigos ou em alvos únicos \n\n A classe faz uso de um recurso chamado mana, que, naturalmente, pode atingir até 200 de mana com o uso de cristais de mana, cujos podem ser cirados utilizando 5 estrelas caída. As armaduras e acessórios do mago giram entorno do seu dano, e da sua gestão de mana, alguns aumentam o limite máximo de mana enquanto outro aumentam o dano bruto da classe em si.\n\n Todos os fatos listados acima criam um poder destrutivo enorme, porém limitado, uma vez que cabe ao jogador saber gerir sua mana corretamente, mas, mesmo com essa limitação a classe não fica atrás das outras em sua progessão, e uma certeza sempre haverá, durante todas as fases do jogo a classe do mago é a que mais possui armas, logo não possui uma progessão truncada e satisfaz todos os estilos de gameplay',
font= ('Andy Negrito', '14'),
wraplength=650,
justify='center')
textomage.pack(pady= 10)
textomage1.pack(pady= 15)

#personalizando a janela sumonner
textosumonner = tk.Label(frame_sumonner, text='Invocador', font= ('Andy Negrito', '20', 'bold', 'underline'))
textosumonner1 = tk.Label(frame_sumonner, text='O Invocador, famoso por usar lacaios para causar grande parte de seu dano. No terraria essa classe é responsável por usar cajados que podem invocar de criaturas mágicas ou até robôs!\n\n O invocador faz uso de dois diferentes tipos de cajados, os cajados de invocação e os cajados de sentinelas, as invocações batem automaticamente, e ao inciar desse quadriculado mundo você só pode ter apenas uma invocação, porém esse limite aumenta ao decorrer da progressão do jogo, devido à acesso a armaduras ou acessórios que expandem esse número, as sentinelas seguem o mesmo raciocínio, porém ficam estáticas em uma localização, o jogador só inicia podendo posicionar apenas uma sentila, podendo também ser expandido por meio de artefatos, mas de forma mais controlada. \n\n Os invocadores também fazem uso dos famigerados chicotes, que fazem as invocações terem como alvo os inimigos atingidos pelo chicote, além de aplicar, geralmente, duas melhorioas para o usuário, sendo uma acerca de seus ataques normais, melhorando seu dano ou aplicando debuffs como queimadura ou envenenamento, e a outra melhoria seria as marcas de invocações, que faz as invocações causarem mais dano quanto mais marcas você possui, cada chicote possui um limite máximo de marcas possível. \n\n A Progressão do summoner é bem baseada em eventos e em areás geralmente não muito visitadas pelos jogadores, porém é uma classe extremamente divertida e dinâmica, porém os desenvolvedores não gostam de verem seus jogadores felizes, a classe possui a defesa mais baixa de todo jogo, onde suas armaduras do harmode são inferiores a muitas armaduras de outras classes do pré-hardmode. Todos esses fatos culminam para tornar a classe mais divertida do jogo, também a mais desafiadora!',
font= ('Andy Negrito', '14'),
wraplength=650,
justify='center')
textosumonner.pack(pady= 10)
textosumonner1.pack(pady= 15)

# Criando o menu principal
menu_principal = tk.Menu(janela)

# Menu "Início"
menu_inicio = tk.Menu(menu_principal, tearoff=0)
menu_inicio.add_command(label='Norteamento', command=semcomando)
menu_principal.add_cascade(label='Início', menu=menu_inicio)

# Menu "Classes"
menu_classes = tk.Menu(menu_principal, tearoff=0)
menu_classes.add_command(label='Guerreiro', command=lambda: subirjanela(frame_melee_base))
menu_classes.add_command(label='Atirador', command=lambda: subirjanela(frame_ranged_base))
menu_classes.add_command(label='Mago', command=lambda: subirjanela(frame_mage_base))
menu_classes.add_command(label='Invocador', command=lambda: subirjanela(frame_sumonner_base))
menu_principal.add_cascade(label='Classes', menu=menu_classes)

# Aplicando o menu à janela
janela.config(menu=menu_principal)

frame_inicial_base.tkraise()

janela.mainloop()