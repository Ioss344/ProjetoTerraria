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

#Criando frames guia da classe meele
frame_guia_melee_boss_base, _, frame_guia_melee_boss = criarframescroll(base_frame)
frame_guia_melee_skeletron_base, _, frame_guia_melee_skeletron = criarframescroll(base_frame)
frame_guia_melee_parededecarne_base, _, frame_guia_melee_parededecarne = criarframescroll(base_frame)

#Criando frames guia da classe ranged
frame_guia_ranged_boss_base, _, frame_guia_ranged_boss = criarframescroll(base_frame)
frame_guia_ranged_skeletron_base, _, frame_guia_ranged_skeletron = criarframescroll(base_frame)
frame_guia_ranged_parededecarne_base, _, frame_guia_ranged_parededecarne = criarframescroll(base_frame)

#Criando frames guia da classe mage
frame_guia_mage_boss_base, _, frame_guia_mage_boss = criarframescroll(base_frame)
frame_guia_mage_skeletron_base, _, frame_guia_mage_skeletron = criarframescroll(base_frame)
frame_guia_mage_parededecarne_base, _, frmame_guia_mage_parededecarne = criarframescroll(base_frame)

#Criando frames guia da classe sumonner
frame_guia_sumonner_boss_base, _, frame_guia_sumonner_boss = criarframescroll(base_frame)
frame_guia_sumonner_skeletron_base, _, frame_guia_sumonner_skeletron = criarframescroll(base_frame)
frame_guia_sumonner_parededecarne_base, _, frame_guia_sumonner_parededecarne = criarframescroll(base_frame)

#Criando frames Chefes
frame_boss_rei_slime_base, _, frame_boss_rei_slime = criarframescroll(base_frame)
frame_boss_olho_base, _, frame_boss_olho = criarframescroll(base_frame)
frame_boss_devorador_base , _, frame_boss_devorador = criarframescroll(base_frame)
frame_boss_cerebro_base , _, frame_boss_cerebro = criarframescroll(base_frame)
frame_boss_abelha_base , _, frame_boss_abelha = criarframescroll(base_frame)
frame_boss_skeletron_base , _, frame_boss_skeletron = criarframescroll(base_frame)
frame_boss_parede_base , _, frame_boss_parede = criarframescroll(base_frame)

#Criando frames de Biomas
frame_bioma_floresta_base , _, frame_bioma_floresta = criarframescroll(base_frame)
frame_bioma_deserto_base , _, frame_bioma_deserto = criarframescroll(base_frame)
frame_bioma_tundra_base , _, frame_bioma_tundra = criarframescroll(base_frame)
frame_bioma_selva_base , _, frame_bioma_selva = criarframescroll(base_frame)
frame_bioma_oceano_base , _, frame_bioma_oceano = criarframescroll(base_frame)
frame_bioma_carmim_base , _, frame_bioma_carmim = criarframescroll(base_frame)
frame_bioma_corrupcao_base , _, frame_bioma_corrupcao = criarframescroll(base_frame)
frame_bioma_submundo_base , _, frame_bioma_submundo = criarframescroll(base_frame)

#Criando o "ocultandor de janelas" (frames)
for frame in (frame_inicial_base, frame_melee_base, frame_ranged_base, frame_mage_base, frame_sumonner_base,
              frame_guia_melee_parededecarne_base,frame_guia_melee_skeletron_base,frame_guia_melee_boss_base,
              frame_guia_ranged_boss_base,frame_guia_ranged_skeletron_base,frame_guia_ranged_parededecarne_base,
              frame_guia_mage_boss_base,frame_guia_mage_skeletron_base,frame_guia_mage_parededecarne_base,
              frame_guia_sumonner_boss_base,frame_guia_sumonner_skeletron_base,frame_guia_sumonner_parededecarne_base,
              frame_boss_rei_slime_base, frame_boss_olho_base,frame_boss_devorador_base,frame_boss_cerebro_base,
              frame_boss_abelha_base, frame_boss_skeletron_base, frame_boss_parede_base,
              frame_bioma_deserto_base, frame_bioma_oceano_base, frame_bioma_carmim_base, frame_bioma_corrupcao_base,
              frame_bioma_submundo_base, frame_bioma_floresta_base, frame_bioma_tundra_base, frame_bioma_selva_base,):
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

bt_guia_melee_boss = tk.Button(frame_melee, text='Chefões Iniciais', command=lambda: subirjanela(frame_guia_melee_boss_base))
bt_guia_melee_boss.pack(pady= 10)

bt_guia_melee_skeletron = tk.Button(frame_melee, text='Skeletron', command=lambda: subirjanela(frame_guia_melee_skeletron_base))
bt_guia_melee_skeletron.pack(pady= 10)

bt_guia_melee_parededecarne = tk.Button(frame_melee, text='Parede de Carne', command=lambda: subirjanela(frame_guia_melee_parededecarne_base))
bt_guia_melee_parededecarne.pack(pady= 10)

#---------Guia melee: Bosses-----------
titulomeleeboss = tk.Label(frame_guia_melee_boss, text='Guerreiro vs Chefes', font= ('Andy Negrito', '20', 'bold', 'underline'), justify='center')
titulomeleeboss.pack(pady= 10)
textoguiameleeboss = tk.Label(frame_guia_melee_boss, text='Essa fase pode ser considerada a mais truncada para o guerreiro devido a sua falta de alcance, essa fase do pré-hardmode corresponde aos Chefes: Rei Slime,Cthullhu, Cerébro de Cthullhu (Carmim) ou Devorador de Mundos (Corrupção) e Rainha Abelha',
                          font=('Andy Negrito', '14'),
                          wraplength=650,
                          justify='center')
textoguiameleeboss.pack(pady= 10)
titulomeleeboss1=tk.Label(frame_guia_melee_boss, text='Guerreiro vs Rei Slime', font= ('Andy Negrito', '16', 'bold', 'underline'))
titulomeleeboss1.pack(pady= 10)
textoguiameleeboss1 = tk.Label(frame_guia_melee_boss, text="""
Armadura:
-Elmo de ouro / Elmo de Platina (Capacete).
-Cota de malha de ouro / Cota de malha de Platina (Peitoral).
-Grevas de ouro / Grvas de Platina (Bota).
*Ouro ou Platina podem ser encontrados nas carvenas de qualquer bioma, e podem ser derretidos para criarem armas e armaduras.

Armas:
-Espada Larga de Ouro.
-Massa Flamejante.
-Bumerangue Mágico.
*A massa e o bumerangue podem ser encontrados em baús no subsolo, e o bumerangue pode ser criado com estrelas e um bumerangue de madeira.

Acessórios:
-Pulseira da regeneração.
-Botas de hermes.
-Nuvem na Garrafa.
*Todos os acessórios podem ser achados em baús espalhados pelo mundo.
""",font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiameleeboss1.pack(pady= 10)

titulomeleeboss2=tk.Label(frame_guia_melee_boss, text='Guerreiro vs Olho de Cthullhu', font= ('Andy Negrito', '16', 'bold', 'underline'))
titulomeleeboss2.pack(pady= 10)
textoguiameleeboss2 = tk.Label(frame_guia_melee_boss, text="""
Armadura:
-Elmo de ouro / Elmo de Platina (Capacete).
-Cota de malha de ouro / Cota de malha de Platina (Peitoral).
-Grevas de ouro / Grvas de Platina (Bota).
*Ouro ou Platina podem ser encontrados nas carvenas de qualquer bioma, e podem ser derretidos para criarem armas e armaduras.

Armas:
-Espada Larga de Ouro.
-Massa Flamejante.
-Bumerangue Mágico.
*A massa e o bumerangue podem ser encontrados em baús no subsolo, e o bumerangue pode ser criado com estrelas e um bumerangue de madeira.

Acessórios:
-Pulseira da regeneração.
-Botas de hermes.
-Nuvem na Garrafa.
*Todos os acessórios podem ser achados em baús espalhados pelo mundo.
""",font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiameleeboss2.pack(pady= 10)

titulomeleeboss3 = tk.Label(frame_guia_melee_boss, text='Guerreiro vs Cerébro de Cthullhu / Devorador de Mundos', font= ('Andy Negrito', '16', 'bold', 'underline'))
titulomeleeboss3.pack(pady= 10)

textoguiameleeboss3 = tk.Label(frame_guia_melee_boss, text="""
Armadura:
-Elmo de ouro / Elmo de Platina (Capacete).
-Cota de malha de ouro / Cota de malha de Platina (Peitoral).
-Grevas de ouro / Grvas de Platina (Bota).

Armas:
-Fúria das estrelas.
-Trimerangue.
-Massa Flamejante.

Acesórios:
-Pulseira da regeneração.
-Botas Espectrais (Botas foguete + Botas de Hermes).
-Nuvem no balão (Balão vermelho + Nuvem na Garrafa).
-Escudo de Cthullhu.
*Botas foguetes são vendidas pelo Inventor Goblin, após acha-lo em uma caverna depois de derrotar uma invasão goblin, e o Escudo de Cthullhu é dropado pelo Olho de Cthullhu.
""",
font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiameleeboss3.pack(pady= 10)

titulomeleeboss4 = tk.Label(frame_guia_melee_boss, text='Guerreiro vs Abelha Rainha', font= ('Andy Negrito', '16', 'bold', 'underline'))
titulomeleeboss4.pack()

textoguiameleeboss4 = tk.Label(frame_guia_melee_boss, text="""
Armadura:
-Elmo das Sombras (Corrupção) / Elmo de Carmim (Carmim).
-Armadura de Placas das Sombras (Corrução) / Armadura de Placas Carmim (Carmim).
-Grevas das Sombras (Corrupção) / Grevas de Placas Carmim (Carmim).
*Criados com itens do Devorador de Mundos / Cerébro de Cthullhu.

Armas:
-A Almôndega.
-Folha de Grama.
-Amazona.
*A almôndega é feita a partir de itens dropados pelo Cerébro, a Folha de Grama e o Amazona são criados com itens do subsolo da selva.

Acessórios:
-Pulseira da regeneração.
-Botas Relâmpago (Botas Espectais + Tornozeleira dos Ventos + Aglet).
-Cachecol de Verme / Cerébro da Confusão.
-Escudo de Cthullhu.
-Bezoar.
-Garras Ferozes.
*As Garras ferozes, o bezoar e a tornozeleira dos ventos podem ser adquiridos na selva, já o aglet pode ser achado em báus de madeira comum e o(s) Cachecol de Verme e Cerébro da Confusão podem ser dropados pelos chefões da corrupção e do carmim, repectivamente.

""",
font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiameleeboss4.pack(pady= 10)

bt_voltar_guia_melee_boss = tk.Button(frame_guia_melee_boss, text='Voltar', command=lambda: subirjanela(frame_melee_base))
bt_voltar_guia_melee_boss.pack(pady=10)


#---------Guia melee: Skeletron-----------
tituloguiameleeskeletron = tk.Label(frame_guia_melee_skeletron, text='Guerreiro vs Skeletron', font= ('Andy Negrito', '20', 'bold', 'underline'), justify='center')
tituloguiameleeskeletron.pack(pady=10)

texotoguiameleeskeletron = tk.Label(frame_guia_melee_skeletron, text='O Skeletron é o segundo boss mais dificíl de todo o pré-hardmode, e é especialmente difícil para o guerreiro, já que chegar próximo demais do chefe é uma senteça de morte. O skeletron é responsável por liberar o acesso do jogador a <asmorra, que em contraparte faz o jogador ficar forte  suficiente para explorar as profundezas do inferno (literalmente).',
                                wraplength=650, font= ('Andy Negrito', '14') , justify='center')
texotoguiameleeskeletron.pack()

textoguiameleeskeletron1 = tk.Label(frame_guia_melee_skeletron, text="""
Armadura:
-Elmo das Sombras (Corrupção) / Elmo de Carmim (Carmim).
-Armadura de Placas das Sombras (Corrução) / Armadura de Placas Carmim (Carmim).
-Grevas das Sombras (Corrupção) / Grevas de Placas Carmim (Carmim).

Armas:
-Folha de Grama.
-A Almôndega.
-Amazona.
-Mestre das Abelhas.
*O Mestre das Abelhas é dropado pela Rainha Abelha.

Acessórios:
-Pulseira da regeneração.
-Botas Relâmpago (Botas Espectais + Tornozeleira dos Ventos + Aglet).
-Cachecol de Verme / Cerébro da Confusão.
-Escudo de Cthullhu.
-Garras Ferozes.
-Colar da Amada (Colar do Pânico + Favo de Mel).
*Colar do Pânico é obtido no carmir ao quebrar corações o Favo de Mel é dropado pela Rainha Abelha.

 """,font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiameleeskeletron1.pack(pady= 10)

bt_voltar_guia_melee_skeletron= tk.Button(frame_guia_melee_skeletron, text='Voltar', command=lambda: subirjanela(frame_melee_base))
bt_voltar_guia_melee_skeletron.pack(pady=10)

#---------Guia melee: Parede De Carne-----------

tituloguiameleeparede = tk.Label(frame_guia_melee_parededecarne, text='Guerreiro vs Parede de Carne', font= ('Andy Negrito', '20', 'bold', 'underline'), justify='center')
tituloguiameleeparede.pack(pady=10)

textoguiameleeparededecarne = tk.Label(frame_guia_melee_parededecarne, text='O famoso e temido divisor de águas, esse chefe é a ultima barreira entre o jogador e o temido Harmode armado até os dentes com lacaios e lasers para dilacerar o jogador. Esse chefe já é difícil por si só, mas imgaine matar uma literal parede que se movimenta, mais criaturar que ele invoca, mais lidar com as criaturas do submundo, e, ainda pro cima lidar com os bloqueios, o terreno e a lava do submundo, é literalmente o inferno!',
font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiameleeparededecarne.pack(pady=10)

textoguiameleeparededecarne1= tk.Label(frame_guia_melee_parededecarne, text="""
Armadura:
-Elmo Derretido (Capacete).
-Peitoral Derretido (Peitoral).
-Grevas Derretido (Botas).
*Barras de Pedra infernal podem ser feitas com pedras infernais e obsidianas, na forja infernal, e são usados para fazer essa armadura.

Armas:
-Lâmina da Noite (Espada de Grama + Muramasa + Espada do Carmin/Corrupção + Volcano)
-Fúria do Sol.
-Cascade
-Bumenrangue Infernal.
*Todos os intens adicionados são achados no submundo ou feitos com barras de pedra infernal.

Acessórios:
-Botas Terrísca (Se possível).
-Escudo de Cthullhu.
-Garras Ferozes.
-Colar da Amada.
-Cachecol de Verme / Cerébro da Confusão.
-Pulseira de Regeneração.
""",
font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiameleeparededecarne1.pack(pady=10)

bt_voltar_guia_melee_parededecarne= tk.Button(frame_guia_melee_parededecarne, text='Voltar', command=lambda: subirjanela(frame_melee_base))
bt_voltar_guia_melee_parededecarne.pack(pady=10)

#Personalizando o frame ranged
textoranged = tk.Label(frame_ranged, text='Atirador', font= ('Andy Negrito', '20', 'bold', 'underline'))
textoranged1 = tk.Label(frame_ranged, text='A classe mais original do terraria, o atirador, essa classe foge dos arquetipos comuns dos rpgs clássicos, pois se tretaria de uma fusão entre a classe gunner (especialista com armas) e o padrão arqueiro, seu arsenal varia entre arcos, armas, shurikens, adagas arremesáveis e bombas, como grandadas e mísseis. \n\nEste arquétipo é o com mais potêncial de dano do jogo possível, sendo tembém uma ótima escolha para novos jogadores, por possuir um alcance enorme e um dano capaz de obliterar a maioria dos inimigos do jogo facilmente.\n\n A classe possui uma defensa balanceada e alto poder ofensivo, onde se desempenha bem com multidões e alvos únicos ela faz uso de municões para poder utilizar suas armas, como flechas, balas e suas variantes, gel, bolas de neve e até mesmo estrelas! Uma das mecânicas extras da classe é o fato do atirador poder posicionar armadilhas que escalam com seu dano, como as bolas de espinho e as minas.\n\n Sua progressão é bem uniforme, possuiuma gama ampla de acessórios e armas, alem do fato de serem de fácil obtenção, uma vez que a maioria de suas bugingangas sao obtidas por chefões os quais fazem parte da trajetória natural do mundo , ou seja, para o atirador atingir seu potencial máximo não são necessários muitos desvios de exploração ou pesca, como em outras classes.',
font=('Andy Negrito', '14'),
wraplength=650,
justify='center' )
textoranged.pack(pady= 10)
textoranged1.pack(pady= 15)

bt_guia_ranged_boss = tk.Button(frame_ranged, text='Boss', command=lambda: subirjanela(frame_guia_ranged_boss_base))
bt_guia_ranged_boss.pack(pady= 10)

bt_guia_ranged_skeletron = tk.Button(frame_ranged, text='Skeletron', command=lambda: subirjanela(frame_guia_ranged_skeletron_base))
bt_guia_ranged_skeletron.pack(pady= 10)

bt_guia_ranged_parededecarne = tk.Button(frame_ranged, text='Parede de Carne', command=lambda: subirjanela(frame_guia_ranged_parededecarne_base))
bt_guia_ranged_parededecarne.pack(pady= 10)

#---------Guia ranged: Boss-----------

tituloguiatangedboss = tk.Label(frame_guia_ranged_boss, text='Atirador vs Chefes', font=('Andy Negrito', '20', 'bold', 'underline' ), justify='center')
tituloguiatangedboss.pack(pady= 10)

textoguiarangedboss = tk.Label(frame_guia_ranged_boss, text='Essa fase do jogo foca principalmente em arcos e requer a exploração de biomas fora da rota principal, como o deserto, essa fase do pré-hardmode corresponde aos Chefes: Rei Slime,Cthullhu, Cerébro de Cthullhu (Carmim) ou Devorador de Mundos (Corrupção) e Rainha Abelha',font=('Andy Negrito', '14'),justify='center', wraplength=650,)
textoguiarangedboss.pack(pady= 10)

tituloguiarangedboss1= tk.Label(frame_guia_ranged_boss, text='Atirador vs Rei Slime', font=('Andy Negrito', '16', 'bold', 'underline' ), justify='center')
tituloguiarangedboss1.pack(pady= 10)

textoguiarangedboss1 =tk.Label(frame_guia_ranged_boss, text="""
Armadura:
-Elmo de Fóssil (Capacete).
-Placas de Fóssil (Peitoral).
-Grevas de Fóssil (Botas).
*Armadura de fósseis e cirada com fósseis resistentes, obrtidos ao refinar fósseis do deserto em um extrator.

Armas:
-Arco de Ouro (Flecha Flamejante, Flecha de Jeste, Flecha de Queimadura de Gelo).
-Arco da Chuva de Sangue (Flecha de Madeira).
-Granadas.
*Arco de outro é criado com ouro, cujo é encontrado no subsolo, o arco da chuva de sangue pode ser obtido ao pescar na lua de sangue, e as granadas são encontradas em baús e vendidas pelo comerciante de bombas.

Acessórios:
-Bota de Hermes.
-Nuvem na Garrafa.
-Pulseira de Regeneração.
-Colar de Dente de Tubarão.
*Bota de Hermes, Nuvem na Garrafa e a Pulseira de Regeneração podem ser encontrados em baús pelo mundo, já o Colar de Dente de Tubarão pode ser dropado por criaturas da Lua de Sange.
""",
font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiarangedboss1.pack(pady=10)

tituloguiarangedboss2 = tk.Label(frame_guia_ranged_boss, text='Atirador vs Olho de Cthullhu', font=('Andy Negrito', '16', 'bold', 'underline' ), justify='center')
tituloguiarangedboss2.pack(pady= 10)

textoguiarangedboss1 =tk.Label(frame_guia_ranged_boss, text="""
Armadura:
-Elmo de Fóssil (Capacete).
-Placas de Fóssil (Peitoral).
-Grevas de Fóssil (Botas).
*Armadura de fósseis e cirada com fósseis resistentes, obrtidos ao refinar fósseis do deserto em um extrator.

Armas:
-Arco de Ouro (Flecha Flamejante, Flecha de Jeste, Flecha de Queimadura de Gelo).
-Arco da Chuva de Sangue (Flecha de Madeira).
-Granadas.
*Arco de outro é criado com ouro, cujo é encontrado no subsolo, o arco da chuva de sangue pode ser obtido ao pescar na lua de sangue, e as granadas são encontradas em baús e vendidas pelo comerciante de bombas.

Acessórios:
-Bota de Hermes.
-Nuvem na Garrafa.
-Pulseira de Regeneração.
-Colar de Dente de Tubarão.
*Bota de Hermes, Nuvem na Garrafa e a Pulseira de Regeneração podem ser encontrados em baús pelo mundo, já o Colar de Dente de Tubarão pode ser dropado por criaturas da Lua de Sange.
""",
font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiarangedboss1.pack(pady=10)

tituloguiarangedboss3 =tk.Label(frame_guia_ranged_boss, text='Atirador vs Cerébro de Cthullhu / Devorador de Mundos', font=('Andy Negrito', '16', 'bold', 'underline' ), justify='center')
tituloguiarangedboss3.pack(pady= 10)

textoguiarangedboss2 =tk.Label(frame_guia_ranged_boss, text="""
-Elmo de Fóssil (Capacete).
-Placas de Fóssil (Peitoral).
-Grevas de Fóssil (Botas).
*Armadura de fósseis e cirada com fósseis resistentes, obrtidos ao refinar fósseis do deserto em um extrator.

Armas:
-Arco de Tendão (Carmim) / Arco Demoníaco (Corrupção);(Flecha de Jeste, Flecha Flamejante, Flecha de Queimadura de Gelo).
-O Coveiro (Carmim) / Mosquete (Corrupção);(Balas de Prata, Balas de Mosquete).
-Granadas.

Acessórios:
-Botas Espectrais (Botas foguete + Botas de Hermes).
-Nuvem no balão (Balão vermelho + Nuvem na Garrafa).
-Pulseira de Regeneração.
-Colar de Dente de Tubarão.
-Escudo de Cthullhu.
""",
font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiarangedboss2.pack(pady=10)

tituloguiarangedboss4 = tk.Label(frame_guia_ranged_boss, text='Atirador vs Abelha Rainha', font=('Andy Negrito', '16', 'bold', 'underline' ), justify='center')
tituloguiarangedboss4.pack(pady= 10)

textoguiarangedboss3 =tk.Label(frame_guia_ranged_boss, text="""
Armadura:
-Elmo de Fóssil (Capacete).
-Placas de Fóssil (Peitoral).
-Grevas de Fóssil (Botas).
*Armadura de fósseis e cirada com fósseis resistentes, obrtidos ao refinar fósseis do deserto em um extrator.

Armas:
-Arco de Tendão (Carmim) / Arco Demoníaco (Corrupção);(Flecha de Jeste, Flecha Flamejante, Flecha de Queimadura de Gelo).
-Mini-Tubarão ; (Balas de Meteoro, Balas de Prata, Balas de Mosquete).
-Cabo de Vassoura ; (Balas de Meteoro, Balas de Prata, Balas de Mosquete).
-Granadas.
*O Mini-Tubarão é vendido pelo Comerciante de Armas e o Cabo de Vassoura pode ser achado nos baús do  subsolo da selva.

Acessórios:
-Botas Relâmpago (Botas Espectais + Tornozeleira dos Ventos + Aglet).
-Bezoar.
-Pulseira de Regeneração.
-Colar de Dente de Tubarão.
-Escudo de Cthullhu.
-Cachecol de Verme / Cerébro da Confusão.
*A tornozeleira dos ventos podem ser adquiridos na selva, já o aglet pode ser achado em báus de madeira comum e o(s) Cachecol de Verme e Cerébro da Confusão podem ser dropados pelos chefões da corrupção e do carmim, repectivamente. O bezoar é dropado por vespas.
""",
font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiarangedboss3.pack(pady=10)

bt_voltar_guia_ranged_boss= tk.Button(frame_guia_ranged_boss, text='Voltar', command=lambda: subirjanela(frame_ranged_base))
bt_voltar_guia_ranged_boss.pack(pady=10)

#---------Guia ranged: Skeletron-----------
tituloguiarangedskeletron = tk.Label(frame_guia_ranged_skeletron, text='Atirador vs Skeletron', font=('Andy Negrito', '20', 'bold', 'underline' ), justify='center')
tituloguiarangedskeletron.pack(pady= 10)

textoguiarangedskeletron = tk.Label(frame_guia_ranged_skeletron, text = 'Mesmo com o alcance gigantesco do atirador o Skeletron não se torna menos desafiador, porém, devido aos dotes dessa classe, ele caba por ser mais aturável. O Skeletron também é responsável dar acesso ao jogador à Masmorra e ao Submundo', font=('Andy Negrito', '14' ),wraplength=650,justify='center')
textoguiarangedskeletron.pack(pady=10)

textoguiarangedskeletron1= tk.Label(frame_guia_ranged_skeletron, text = """
Armadura:
-Elmo de Fóssil (Capacete).
-Placas de Fóssil (Peitoral).
-Grevas de Fóssil (Botas).
*Armadura de fósseis e cirada com fósseis resistentes, obrtidos ao refinar fósseis do deserto em um extrator.

Armas:
-Abelharco ; (Flecha de Madeira).
-Mini-Tubarão ; (Balas de Meteoro, Balas de Prata, Balas de Mosquete).
-Cabo de Vassoura ; (Balas de Meteoro, Balas de Prata, Balas de Mosquete).
-Granadas.
*O Abelharco é dropado pela Rainha Abelha.

Acessórios:
-Botas Relâmpago (Botas Espectais + Tornozeleira dos Ventos + Aglet).
-Nuvem no Balão.
-Pulseira de Regeneração.
-Colar de Dente de Tubarão.
-Escudo de Cthullhu.
-Cachecol de Verme / Cerébro da Confusão.
""",
font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiarangedskeletron1.pack(pady=10)
bt_voltar_guia_ranged_skeletron= tk.Button(frame_guia_ranged_skeletron, text='Voltar', command=lambda: subirjanela(frame_ranged_base))
bt_voltar_guia_ranged_skeletron.pack(pady=10)

#---------Guia ranged: Parede de Carne-----------

tituloguiarangedparededecarne = tk.Label(frame_guia_ranged_parededecarne, text='Atirador vs Parede de Carne', font=('Andy Negrito', '20', 'bold', 'underline' ), justify='center')
tituloguiarangedparededecarne.pack(pady= 10)

textoguiarangedparededecarne = tk.Label(frame_guia_ranged_parededecarne, text='O famoso divisor de águas, a grande parede carnifera, um chefe estremamente dificl, por si só e por onde é enfrentad, pois o chefe só pode ser invocado no submundo. O chefe dá acesso ao jogador ao temido Hard-Mode, que abre mais um leque de armmas pesadas para o atirador.',font=('Andy Negrito', '14' ),wraplength=650,justify='center')
textoguiarangedparededecarne.pack(pady=10)

textoguiarangedparededecarne1 = tk.Label(frame_guia_ranged_parededecarne, text="""
Armadura:
-Elmo Necrosado (Capacete).
-Peitoral Necrosado (Peitoral).
-Grevas Necrosadas (Botas).
*A armadura necrosada é criada com ossos da masmorra e teias de aranha.

Armas:
-Mini-Tubarão ; (Balas de Meteoro, Balas de Prata, Balas de Mosquete).
-Pistola da Fênix ; (Balas de Meteoro).
-Canhão de Estrelas ; (Estrelas).
-Arco Derretido ; (Flechas Infernais).
-Arco das Asas Infernais ; (Flechas de Madeira).
*Pistola da Fênix é feita com a arma, encontrada nas masmorras e barras de pedra infernal, arco derretido também é criado com essas barras, já o canhão de estrelas é feito com a mini-tubarão, estrelas e barras de meteorito. O arco de asas infernais é encontrado no submundo.

Acessórios:
-Botas Terraísca (Se possível).
-Nuvem no Balão.
-Pulseira de Regeneração.
-Colar de Dente de Tubarão.
-Escudo de Cthullhu.
-Cachecol de Verme / Cerébro da Confusão.
""",
font=('Andy Negrito', '14'),
wraplength=650,
justify='left')
textoguiarangedparededecarne1.pack(pady=10)

bt_voltar_guia_ranged_parededecarne= tk.Button(frame_guia_ranged_parededecarne, text='Voltar', command=lambda: subirjanela(frame_ranged_base))
bt_voltar_guia_ranged_parededecarne.pack(pady=10)
#Personalizado o frame mage
textomage = tk.Label(frame_mage, text='Mago', font= ('Andy Negrito', '20', 'bold', 'underline'))
textomage1 = tk.Label(frame_mage, text='O famoso e famigerado mago, clásico dos rpgs de turno. No Terraria a classe se sobresai com a classe mais versátil do jogo, pois suas armas são dotadas de diferentes mecânicas, sendo capazes de lançarem arco-íris fofinhos, ou talvez criarem uma nebulosa que é capaz de debilitar toda a vida pelo seu trajeto, essa é a versalidade da magia desse mundo!\n\n O mago é especialista em causar dano a ditância, possuindo uma amplitude de armas para as mais diversas situações, podendo usar cetros, grimórios, cajados e até objetos amaldiçados para causar um dano supreendente, tanto em situações com muitos inimigos ou em alvos únicos \n\n A classe faz uso de um recurso chamado mana, que, naturalmente, pode atingir até 200 de mana com o uso de cristais de mana, cujos podem ser cirados utilizando 5 estrelas caída. As armaduras e acessórios do mago giram entorno do seu dano, e da sua gestão de mana, alguns aumentam o limite máximo de mana enquanto outro aumentam o dano bruto da classe em si.\n\n Todos os fatos listados acima criam um poder destrutivo enorme, porém limitado, uma vez que cabe ao jogador saber gerir sua mana corretamente, mas, mesmo com essa limitação a classe não fica atrás das outras em sua progessão, e uma certeza sempre haverá, durante todas as fases do jogo a classe do mago é a que mais possui armas, logo não possui uma progessão truncada e satisfaz todos os estilos de gameplay',
font= ('Andy Negrito', '14'),
wraplength=650,
justify='center')
textomage.pack(pady= 10)
textomage1.pack(pady= 15)

bt_guia_mage_boss = tk.Button(frame_mage, text='Boss', command= lambda: subirjanela(frame_guia_mage_boss_base))
bt_guia_mage_boss.pack(pady= 10)

bt_guia_mage_skeletron = tk.Button(frame_mage, text='Skeletron', command= lambda: subirjanela(frame_guia_mage_skeletron_base))
bt_guia_mage_skeletron.pack(pady= 10)

bt_guia_mage_parededecarne = tk.Button(frame_mage, text='Parede de Carne', command= lambda: subirjanela(frame_guia_mage_parededecarne_base))
bt_guia_mage_parededecarne.pack(pady= 10)


#personalizando a janela sumonner
textosumonner = tk.Label(frame_sumonner, text='Invocador', font= ('Andy Negrito', '20', 'bold', 'underline'))
textosumonner1 = tk.Label(frame_sumonner, text='O Invocador, famoso por usar lacaios para causar grande parte de seu dano. No terraria essa classe é responsável por usar cajados que podem invocar de criaturas mágicas ou até robôs!\n\n O invocador faz uso de dois diferentes tipos de cajados, os cajados de invocação e os cajados de sentinelas, as invocações batem automaticamente, e ao inciar desse quadriculado mundo você só pode ter apenas uma invocação, porém esse limite aumenta ao decorrer da progressão do jogo, devido à acesso a armaduras ou acessórios que expandem esse número, as sentinelas seguem o mesmo raciocínio, porém ficam estáticas em uma localização, o jogador só inicia podendo posicionar apenas uma sentila, podendo também ser expandido por meio de artefatos, mas de forma mais controlada. \n\n Os invocadores também fazem uso dos famigerados chicotes, que fazem as invocações terem como alvo os inimigos atingidos pelo chicote, além de aplicar, geralmente, duas melhorioas para o usuário, sendo uma acerca de seus ataques normais, melhorando seu dano ou aplicando debuffs como queimadura ou envenenamento, e a outra melhoria seria as marcas de invocações, que faz as invocações causarem mais dano quanto mais marcas você possui, cada chicote possui um limite máximo de marcas possível. \n\n A Progressão do summoner é bem baseada em eventos e em areás geralmente não muito visitadas pelos jogadores, porém é uma classe extremamente divertida e dinâmica, porém os desenvolvedores não gostam de verem seus jogadores felizes, a classe possui a defesa mais baixa de todo jogo, onde suas armaduras do harmode são inferiores a muitas armaduras de outras classes do pré-hardmode. Todos esses fatos culminam para tornar a classe mais divertida do jogo, também a mais desafiadora!',
font= ('Andy Negrito', '14'),
wraplength=650,
justify='center')
textosumonner.pack(pady= 10)
textosumonner1.pack(pady= 15)

bt_guia_sumonner_boss = tk.Button(frame_sumonner, text='Boss', command=lambda: subirjanela(frame_guia_sumonner_boss_base))
bt_guia_sumonner_boss.pack(pady= 10)

bt_guia_sumonner_skeletron = tk.Button(frame_sumonner, text='Skeletron', command=lambda: subirjanela(frame_guia_sumonner_skeletron_base))
bt_guia_sumonner_skeletron.pack(pady= 10 )

bt_guia_sumonner_parededecarne = tk.Button(frame_sumonner, text='Parede de Carne ', command=lambda: subirjanela(frame_guia_sumonner_parededecarne_base ))
bt_guia_sumonner_parededecarne.pack(pady= 10)



# Criando o menu principal
menu_principal = tk.Menu(janela)

# Menu "Início"
menu_inicio = tk.Menu(menu_principal, tearoff=0)
menu_inicio.add_command(label='Início', command= lambda: subirjanela(frame_inicial_base))
menu_principal.add_cascade(label='Início', menu=menu_inicio)

# Menu "Classes"
menu_classes = tk.Menu(menu_principal, tearoff=0)
menu_classes.add_command(label='Guerreiro', command=lambda: subirjanela(frame_melee_base))
menu_classes.add_command(label='Atirador', command=lambda: subirjanela(frame_ranged_base))
menu_classes.add_command(label='Mago', command=lambda: subirjanela(frame_mage_base))
menu_classes.add_command(label='Invocador', command=lambda: subirjanela(frame_sumonner_base))
menu_principal.add_cascade(label='Classes', menu=menu_classes)

#Menu "Chefes"
menu_boss = tk.Menu(menu_principal, tearoff=0)
menu_boss.add_command(label='Rei Slime', command= lambda: subirjanela(frame_boss_rei_slime_base))
menu_boss.add_command(label='Olho de Cthullhu', command= lambda: subirjanela(frame_boss_olho_base))
menu_boss.add_command(label='Devorador de Mundos', command= lambda: subirjanela(frame_boss_devorador_base))
menu_boss.add_command(label='Cerébro de Cthullhu', command= lambda: subirjanela(frame_boss_cerebro_base))
menu_boss.add_command(label='Abelha Rainha', command= lambda: subirjanela(frame_boss_abelha_base))
menu_boss.add_command(label='Skeletron', command= lambda: subirjanela(frame_boss_skeletron_base))
menu_boss.add_command(label='Parede de Carne', command= lambda: subirjanela(frame_boss_parede_base))
menu_principal.add_cascade(label='Chefes', menu=menu_boss)

#Menu "Biomas"
menu_biomas = tk.Menu(menu_principal, tearoff=0)
menu_biomas.add_command(label='Floresta', command= lambda: subirjanela(frame_bioma_floresta_base))
menu_biomas.add_command(label='Deserto', command= lambda: subirjanela(frame_bioma_deserto_base))
menu_biomas.add_command(label='Tundra', command= lambda: subirjanela(frame_bioma_tundra_base))
menu_biomas.add_command(label='Selva', command= lambda: subirjanela(frame_bioma_selva_base))
menu_biomas.add_command(label='Oceano', command= lambda: subirjanela(frame_bioma_oceano_base))
menu_biomas.add_command(label='Carmim', command= lambda: subirjanela(frame_bioma_carmim_base))
menu_biomas.add_command(label='Corrupção', command= lambda: subirjanela(frame_bioma_corrupcao_base))
menu_biomas.add_command(label='Submundo', command= lambda: subirjanela(frame_bioma_submundo_base))
menu_principal.add_cascade(label='Biomas', menu=menu_biomas)

# Aplicando o menu à janela
janela.config(menu=menu_principal)

frame_inicial_base.tkraise()

janela.mainloop()
