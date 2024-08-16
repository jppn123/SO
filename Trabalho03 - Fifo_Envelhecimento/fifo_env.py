import random
from fila import Queue

class Fifo:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = Queue()
        self.pag_falta = 0

    def paginar(self, pag):
        #se não estiver na lista, verifica o tamanho do quadro, caso menor, insere, caso maior remove o primeiro da fila e adiciona a página nova
        if not self.frames.isInQueue(pag):
            if self.frames.len() < self.num_frames:
                self.frames.push(pag)
            else:
                self.frames.remove()
                self.frames.push(pag)
            self.pag_falta += 1
        self.frames.printQueue()
        

class Envelhecimento:
    def __init__(self, num_pags):
        self.num_pags = num_pags
        self.frames = {}
        self.pag_falta = 0

    def paginar(self, pag_nova):
        #deslocar os bits para a esquerda 10000000 -> 01000000
        for p in self.frames:
            self.frames[p] >>= 1
        if pag_nova not in self.frames:
            #vai inserindo no dicionario ate chegar no numero de paginas, quando encher, vai cair no else que vai pegar o menor e remover
            if len(self.frames) < self.num_pags:
                self.frames[pag_nova] = 0b10000000
            else:
                pagina_antiga = min(self.frames, key=self.frames.get)
                del self.frames[pagina_antiga]
                self.frames[pag_nova] = 0b10000000
            self.pag_falta += 1
        else:
            self.frames[pag_nova] |= 0b10000000
        
        
        
'''
    def paginar(self, pag):
        #deslocar os bits para a esquerda 10000000 -> 01000000
        while self.frames.len() != 0:
            pagina, valor = self.frames.remove()
            valor >>= 1
            self.aux.append((pagina, valor))
        if self.frames.len() != 0:
            for tup in self.aux:
                self.frames.push((tup[0],tup[1]))
        if self.frames.isInQueue(pag):
            while self.frames.len() != 0:
                pagina, valor = self.frames.remove()
                if pagina == pag:
                    pagina = pag
                    valor |= 0b10000000
                    self.frames.push((pagina, valor))
                    break
        else:
            if self.frames.len() >= self.num_pags:
                pagina_antiga = min(self.aux, key=lambda tup: tup[1])
                while not self.frames.len() != 0:
                    pagina, valor = self.frames.remove()
                    if pagina == pagina_antiga:
                        pagina = pag
                        valor = 0b10000000
                        self.frames.push((pagina, valor))
                        break
            else:
                pagina = pag
                valor = 0b10000000
                self.frames.push((pagina, valor))
            self.pag_falta += 1
        self.frames.printQueue()
'''


"""
total_frames: simulação da quantidade de frames (quantas vezes vai rodar)
num_ender: referencias de memoria (tamanho da sequencia)
paginas: sequencia na qual as páginas A,...,Z aparecem
alfa: alfabeto usado para definir a sequencia
num_pags: total de páginas por frame (como estou usando alfabeto, o ideal é ser < 15 pra ter um resultado legal, 
                                        se 26, terão apenas 26 faltas de página)
"""

num_pags = 10
num_ender = 1000
total_frames = 20
faltas = []
alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nome_pag_frame = "pags_frame.txt"

with open("faltas_pag.txt", "w") as falta_file:
    falta_file.write("Frame\tFifo\tEnvelhecimento\n")
    with open(nome_pag_frame, "w") as clear_file:
        clear_file.write("")
        clear_file.close()

    for num_frame in range(1, total_frames + 1):
        paginas.clear()
        for _ in range(num_ender):
            paginas.append(random.choice(alfa))

        fifo = Fifo(num_pags)
        env = Envelhecimento(num_pags)

        for pagina in paginas:
            fifo.paginar(pagina)
            env.paginar(pagina)
        
        falta_file.write(f"{num_frame}\t{fifo.pag_falta}\t{' '*5}{env.pag_falta}\n")

        if fifo.pag_falta > env.pag_falta:
            faltas.append("fifo")
        else:
            faltas.append("env")

        with open(nome_pag_frame, "a") as pag_frame_file:
            pag_frame_file.write(f"Páginas do frame {str(num_frame)}:" + '\n')
            pag_frame_file.write(' '.join(paginas) + '\n\n\n')
            
    tot_faltas = "Fifo" if faltas.count("fifo") > faltas.count("env") else "Envelhecimento" 
    tot_faltas = "Igual" if faltas.count("fifo") == faltas.count("env") else tot_faltas
    falta_file.write(f"\nMais faltas:\t{tot_faltas}")

pag_frame_file.close()
falta_file.close()  
            
