from search_recipiente import *


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
estado_final = [(4,3),(4,0)]

problema = Problem(estado_inicial, estado_final, grafo)

print("Estado inicial:", estado_inicial)
print("Estado final:", estado_final)


resultado_busca_em_profundidade, quantidade_de_caminhos = depth_first_graph_search(problema)

solucao_busca_em_profundidade = resultado_busca_em_profundidade.solution()

solucao_busca_em_profundidade.insert(0, estado_inicial)

print("Solução em profundidade:", solucao_busca_em_profundidade)
print("Quantidade de caminhos em profundidade:", quantidade_de_caminhos)

