import random
import time

class RPGGame:
    def __init__(self):
        self.player_name = "Alexandro"
        self.player_hp = 40
        self.monster_hp = 60

    def story_intro(self):
        print("Alexandro está indo em direção a Floresta amaldiçoada ele fala consigo mesmo: Hoje eu me reúno com meus amigos em frente a floresta amaldiçoada, tomara que a beatriz esteja lá...")
        time.sleep(7)
        print("Alexsandro, Gabriel, Rogério e Beatriz estão na entrada da Floresta Amaldiçoada. Gabriel provoca Alexssandro para entrar.")
        time.sleep(5)
        print("Gabriel: (rindo) — Vamos lá, Alex! Você não vai amarelar, né? Dizem que quem entra nessa floresta nunca sai... mas você parece corajoso.")
        time.sleep(5)
        print("Rogério: (tentando disfarçar a própria hesitação) — É só uma lenda boba. Nada demais! Ou você tem medo de um monte de árvores?")
        time.sleep(5)
        print("Beatriz: (preocupada) — Não precisa provar nada para eles, Alex. Às vezes, coragem é saber dizer 'não'.")
        time.sleep(5)
        self.story_continue()
    
    def story_continue(self):
        print("Alexandro se encontra num impasse...")
        time.sleep(3)
        print("1. Alexandro entra imediatamente no labirinto.")
        print("2. Recusar entrar no labirinto.")
        choice = input("\nO que ele faz? (1/2): ")
        if choice == "1":
            print("\nAlexssandro caminha para o labirinto, levando consigo o peso da dúvida e a pressão social.")
            time.sleep(5)
            self.story_continue2()
        elif choice == "2":
            print("\nBeatriz fica aliviada, mas Gabriel e Rogério zombam dele. Ele decide entrar sozinho mais tarde, para provar algo a si mesmo.")
            time.sleep(5)
            self.story_continue2()
        else:
            print("\nEscolha inválida! Tente novamente.")
            self.story_continue()

    def story_continue2(self):
        print("Alexssandro encontra um viajante preso em uma vinha no caminho que implora por ajuda.")
        time.sleep(5)
        print("Viajante Perdido: (desesperado)-Por favor, me ajude! Estou preso aqui há tanto tempo... Se você me tirar daqui, posso te mostrar um atalho para sair do labirinto!")
        time.sleep(5)
        print("1. Alexandro ajuda o viajante.")
        print("2. Alexandro passa direto.")
        choice = input("\nO que ele faz? (1/2): ")
        if choice == "1":
            print("\nAlexssandro ajuda o viajante, que revela um atalho.")
            time.sleep(5)
            print("Viajante:Aqui está pequeno gafanhoto... só tome cuidado com um possível encontro com o Lobo Mau, ele é extremamente perigoso.")
            time.sleep(5)
            self.story_continue3()
        elif choice == "2":
            print("\nAlexandro não ajuda o viajante, assim o deixando com peso na consciência e se perdendo várias vezes nos diversos caminhos do labirinto.")
            time.sleep(5)
            self.story_continue3()
        else:
            print("\nEscolha inválida! Tente novamente.")
            self.story_continue2()

    def story_continue3(self):
        print("Numa clareira, Alexandro encontra uma figura com estatura e físico intimidador, com um olhar e tom de voz que o garoto suspeita de primeira.")
        time.sleep(5)
        print("Lobo Humanoide: (em tom sedutor) — Ora, ora... O que temos aqui? Um jovem perdido, tentando brincar de herói? Eu posso te mostrar a saída... se você confiar em mim.")
        time.sleep(5)
        print("1. Alexandro confia no Lobo.")
        print("2. Alexandro joga areia na cara do Lobo e sai correndo.")
        print("3. Alexandro tenta atacar o Lobo com um pedaço de madeira que pegou do chão.")
        choice = input("\nO que ele faz? (1/2/3): ")
        if choice == "1":
            print("Ele aceita um atalho enganoso, mas fica preso em um ciclo infinito dentro do labirinto.")
            time.sleep(5)
            print("Alexssandro percebe tarde demais que cedeu ao medo e à dúvida, tornando-se parte da lenda da floresta.")
            time.sleep(5)
            print("Alexandro se encontra no começo do labirinto, como se algo tivesse o salvo do ciclo infinito...")
            time.sleep(5)
            self.story_intro()
        elif choice == "2":
            print("Alexandro consegue fugir do Lobo.")
            time.sleep(3)
            self.story_continue4()
        elif choice == "3":
            print("Alexandro entra em um combate com o Lobo.")
            time.sleep(3)
            self.combat1()

    def combat1(self):
        print(f"\nUPrepare-se para lutar, Alexandro!")
        while self.player_hp > 0 and self.monster_hp > 0:
            print(f"\nSua vida: {self.player_hp} | Vida do monstro: {self.monster_hp}")
            print("1. Atacar com seu galho de madeira.")
            #print("2. Defender-se e recuperar energia.")
            print("2. Fugir.")
            action = input("\nO que você faz? (1/2): ")
            
            if action == "1":
                damage = random.randint(2, 5)
                self.monster_hp -= damage
                print(f"\nVocê ataca o monstro e causa {damage} de dano!")
            #elif action == "2":
                #heal = random.randint(5, 15)
                #self.player_hp += heal
                #print(f"\nVocê se defende e recupera {heal} de vida.")
            elif action == "2" and self.player_hp >= 30:
                print("\nVocê tenta fugir, mas o monstro não permite!")
            elif action == "2" and self.player_hp <= 30:
                print("\nVocê consegue fugir com muita dificuldade.")
                self.story_continue4()
            
            # Monstro ataca
            if self.monster_hp > 0:
                monster_damage = random.randint(5, 10)
                self.player_hp -= monster_damage
                print(f"O monstro ataca e causa {monster_damage} de dano!")

        if self.player_hp <= 0:
            print("\nVocê foi derrotado! O monstro vence.")
            print("Algo ajuda Alexandro a voltar...")
            self.player_hp += 40
            self.story_continue3()
            time.sleep(5)
        elif self.monster_hp <= 0:
            print("\nParabéns! Você derrotou o monstro!")
            time.sleep(5)
        else:
            print("\nO combate terminou inesperadamente.")



    def story_continue4(self):
        print("Alexandro se encontra com um caçador.")
        time.sleep(5)
        print("Caçador: (em tom calmo) — Jovem, o labirinto não é o que parece. Cada escolha molda o seu destino. Você pode ouvir meus conselhos ou seguir sozinho.")
        time.sleep(5)
        print("1. Alexandro ouve os conselhos do caçador.")
        print("2. Alexandro não ouve os conselhos do caçador.")
        choice = input("\nO que ele faz? (1/2): ")
        if choice == "1":
            print("O Caçador dá um amuleto que brilha quando o caminho certo está próximo... e um companheiro de viagem.")
            time.sleep(5)
            self.story_continue6()
        elif choice == "2":
            print("Alexandro não ouve os conselhos do caçador.")
            time.sleep(5)
            self.story_continue5()

    def story_continue5(self):
        print("Alexandro se aproxima de um lago e vê seu próprio reflexo.")
        time.sleep(5)
        print("Ele repensa algumas das escolhas... será que ele fez o certo?")
        time.sleep(5)
        print("1. Alexandro está satisfeito com suas escolhas e segue seu rumo.")
        print("2. Alexandro não aceita suas escolhas...")
        choice = input("\nO que ele faz? (1/2): ")
        if choice == "1":
            self.combat2()
        elif choice == "2":
            print("Alexandro se vê no começo do labirinto de novo...")
            time.sleep(5)
            self.story_continue2()

    def combat2(self):
        print("Lobo Humanoide: (furioso) — Você ainda não entendeu? Eu sou o dono deste labirinto. Você nunca vai escapar sem me derrotar.")
        time.sleep(5)
        print(f"\nUPrepare-se para lutar, Alexandro!")
        time.sleep(5)
        while self.player_hp > 0 and self.monster_hp > 0:
            print(f"\nSua vida: {self.player_hp} | Vida do monstro: {self.monster_hp}")
            print("1. Atacar com seu galho de madeira.")
            # print("2. Defender-se e recuperar energia.")
            print("2. Fugir.")
            action = input("\nO que você faz? (1/2): ")

            if action == "1":
                damage = random.randint(2, 5)
                self.monster_hp -= damage
                print(f"\nVocê ataca o monstro e causa {damage} de dano!")
            # elif action == "2":
            # heal = random.randint(5, 15)
            # self.player_hp += heal
            # print(f"\nVocê se defende e recupera {heal} de vida.")
            elif action == "2" and self.player_hp >= 30:
                print("\nVocê tenta fugir, mas o monstro não permite!")
            elif action == "2" and self.player_hp <= 30:
                print("\nVocê consegue fugir com muita dificuldade.")
                self.story_continue4()

            # Monstro ataca
            if self.monster_hp > 0:
                monster_damage = random.randint(5, 10)
                self.player_hp -= monster_damage
                print(f"O monstro ataca e causa {monster_damage} de dano!")
                continue

        if self.player_hp <= 0:
            print("\nVocê foi derrotado! Alexandro sente uma sensação estranha e se depara em frente ao caçador...")
            time.sleep(5)
            self.story_continue4()
        elif self.monster_hp <= 0:
            print("\nParabéns! Você derrotou o monstro!")
            time.sleep(5)
        else:
            print("\nO combate terminou inesperadamente.")

    def story_continue6(self):
        print("Alexandro se aproxima de um lago e vê seu próprio reflexo, o Caçador se aproxima também e olha com um sorriso para o reflexo do garoto.")
        time.sleep(5)
        print("Ele repensa algumas das escolhas... será que ele fez o certo?")
        time.sleep(5)
        print("1. Alexandro está satisfeito com suas escolhas e segue seu rumo.")
        print("2. Alexandro não aceita suas escolhas...")
        choice = input("\nO que ele faz? (1/2): ")
        if choice == "1":
            self.combat3()
        elif choice == "2":
            print("Alexandro se vê no começo do labirinto de novo...")
            time.sleep(5)
            self.story_continue2()

    def combat3(self):
        print("Lobo Humanoide: (furioso) — Você ainda não entendeu? Eu sou o dono deste labirinto. Você nunca vai escapar sem me derrotar.")
        time.sleep(5)
        print("Caçador: (ofegante) Eu te ajudo garoto, pegue esse porrete!")
        time.sleep(5)
        print(f"\nUPrepare-se para lutar, Alexandro!")
        time.sleep(5)
        while self.player_hp > 0 and self.monster_hp > 0:
            print(f"\nSua vida: {self.player_hp} | Vida do Lobo: {self.monster_hp}")
            print("1. Atacar com seu porrete.")
            print("2. Defender-se e recuperar energia.")
            action = input("\nO que você faz? (1/2): ")

            if action == "1":
                damage = random.randint(2, 5)
                self.monster_hp -= damage
                print(f"\nVocê ataca o Lobo e causa {damage} de dano!")
                hunter_damage = random.randint(2, 5)
                self.monster_hp -=hunter_damage
                print(f"\nO Caçador ataca o Lobo e causa {hunter_damage} de dano!")


            elif action == "2":
                heal = random.randint(5, 15)
                self.player_hp += heal
                print(f"\nVocê se defende e recupera {heal} de vida.")
                hunter_damage = random.randint(2, 5)
                self.monster_hp -=hunter_damage
                print(f"\nO Caçador ataca o Lobo e causa {hunter_damage} de dano!")

            # Monstro ataca
            if self.monster_hp > 0:
                monster_damage = random.randint(5, 10)
                self.player_hp -= monster_damage
                print(f"O Lobo ataca e causa {monster_damage} de dano!")
                continue

        if self.player_hp <= 0:
            print("\nVocê foi derrotado! Alexandro sente uma sensação estranha e se depara em frente ao caçador...")
            time.sleep(5)
            self.story_continue4()
        elif self.monster_hp <= 0:
            print("\nParabéns! Você derrotou o Lobo Mau!")
            time.sleep(5)
            self.story_continue7()
        else:
            print("\nO combate terminou inesperadamente.")

    def story_continue7(self):
        print("Ele usa as lições e ferramentas adquiridas para derrotar o Lobo Mau, abrindo o portal para a liberdade.")
        time.sleep(5)
        print("Alexssandro sai do labirinto mais sábio, tendo aprendido a confiar em si mesmo e nos conselhos certos.")
        time.sleep(5)
        self.end_game()

    def end_game(self):
        print("\nObrigado por jogar! Até a próxima aventura.")

# Iniciar o jogo
game = RPGGame()
game.story_intro()
