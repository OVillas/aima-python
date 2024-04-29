from asyncio import sleep
import tkinter as tk
from search_recipiente import *

quantidade_primeiro_recipiente = 5
quantidade_segundo_recipiente = 3


class WaterJugProblemGUI:
    def __init__(self, root: tk.Tk, problema: Problem):
        self.root = root
        self.root.title("Problema do copinho")
        self.primeiro_recipiente = 0
        self.segundo_recipiente = 0
        self.solucao = []
        self.problema = problema
        
      
        self.estado_recipiente_um = 0  
        self.estado_recipiente_dois = 0  
        
        
        self.canvas = tk.Canvas(root, width=200, height=300)
        self.canvas.grid(row=0, column=0, columnspan=2)
        
        
        self.desenhar_recipiente(50, 50, 40, 200, self.estado_recipiente_um)
        self.desenhar_recipiente(120, 50, 40, 200, self.estado_recipiente_dois)
        
        self.solve_bfs_button = tk.Button(root, text="Busca em largura", command=self.busca_em_largura)
        self.solve_bfs_button.grid(row=4, column=0)
        
        self.solve_dfs_button = tk.Button(root, text="Busca em profundidade", command=self.busca_em_profundidade)
        self.solve_dfs_button.grid(row=4, column=1)
        self.solve_dfs_button = tk.Button(root, text="Busca em profundidade Limitada", command=self.busca_em_profundidade_limitada)
        self.solve_dfs_button.grid(row=6, column=0)
        
        self.solve_dfs_button = tk.Button(root, text="Busca em profundidade Interativa", command=self.busca_em_profundidade)
        self.solve_dfs_button.grid(row=6, column=1)
        
        
    def encher_primeiro_recipiente(self, qtd):
        self.primeiro_recipiente = qtd
        if (self.primeiro_recipiente <= quantidade_primeiro_recipiente):
            self.inserir_agua_no_primeiro_recipiente()
        
    def encher_segundo_recipiente(self, qtd):
        self.segundo_recipiente = qtd
        if (self.segundo_recipiente <= quantidade_segundo_recipiente):
            self.inserir_agua_no_segundo_recipiente()
        
    def desenhar_recipiente(self, x, y, width, height, water_level):
        self.canvas.create_rectangle(x, y, x + width, y + height, fill="gray", outline="black")
        for i in range(water_level):
            self.canvas.create_rectangle(x + 5, y + height - (i + 1) * 20 - i * 2, x + width - 5, y + height - i * 20 - i * 2, fill="blue", outline="")
    
    def inserir_agua_no_primeiro_recipiente(self):
        self.estado_recipiente_um = self.primeiro_recipiente
        self.canvas.delete("jug_4")
        self.desenhar_recipiente(50, 50, 40, 200, self.estado_recipiente_um)
    
    def inserir_agua_no_segundo_recipiente(self):
        self.estado_recipiente_dois = self.segundo_recipiente
        self.canvas.delete("jug_3")
        self.desenhar_recipiente(120, 50, 40, 200, self.estado_recipiente_dois)
    
    def esvaziar_primeiro_recipiente(self):
        self.primeiro_recipiente = 0
        self.estado_recipiente_um = 0
        self.canvas.delete("jug_4")
        self.desenhar_recipiente(50, 50, 40, 200, self.estado_recipiente_um)
    
    def esvaziar_segundo_recipiente(self):
        self.segundo_recipiente = 0
        self.estado_recipiente_dois = 0
        self.canvas.delete("jug_3")
        self.desenhar_recipiente(150, 50, 40, 150, self.estado_recipiente_dois)
    
    def busca_em_largura(self):
        resultado, _ = breadth_first_graph_search(problem)
        self.solucao = resultado.solution()
        print(self.solucao)
        self.executar_solucao()
    
    def busca_em_profundidade(self):
        resultado, _ = depth_first_graph_search(self.problema)
        self.solucao = resultado.solution()
        print(self.solucao)
        self.executar_solucao()
    
    def busca_em_profundidade_limitada(self):
        resultado = depth_limited_search(self.problema, 10)
        self.solucao = resultado.solution()
        print(self.solucao)
        self.executar_solucao()
        
    def executar_solucao(self):
         for i in range(len(self.solucao)):
            tupla = self.solucao[i]
            self.encher_primeiro_recipiente(tupla[0])
            self.root.update()  
            self.encher_segundo_recipiente(tupla[1])
            self.root.update()  
            self.root.after(1000)


grafo = {
    (0,0): [(5,0), (0,3)],
    (5,0): [(0,0), (5,3), (2,3)],
    (0,3): [(0,0), (5,3), (3,0)],
    (5,3): [(0,3), (5,0)],
    (2,3): [(0,3), (2,0), (5,3), (5,0)],
    (3,0): [(0,0), (3,3), (0,3)],
    (2,0): [(0,0), (5,0), (2,3), (0,2)],
    (3,3): [(0,3), (3,0), (5,3), (5,1)],
    (0,2): [(0,0), (5,2), (0,3), (2,0)],
    (5,1): [(0,1), (5,0), (5,3), (3,3)],
    (5,2): [(0,2), (5,0), (5,3), (4,3)],
    (0,1): [(0,0), (5,1), (0,3), (1,0)],
    (4,3): [(0,3), (4,0), (5,3), (5,2)],
    (1,0): [(0,0), (5,0), (1,3), (0,1)],
    (4,0): [(0,0), (5,0), (4,3), (1,3)],
    (1,3): [(0,3), (1,0), (5,3), (4,0)],  
}

estado_inicial = (0,0)
estado_final = [(4,0), (4,3)]

problem = Problem(estado_inicial, estado_final, grafo)

root = tk.Tk()
app = WaterJugProblemGUI(root, problem)
root.mainloop()
