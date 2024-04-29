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

resultado_busca_em_largura, cont = breadth_first_graph_search(problema)

solucao_busca_em_largura = resultado_busca_em_largura.solution()

solucao_busca_em_largura.insert(0, estado_inicial)

print("Solução em largura:", solucao_busca_em_largura)
print("Quantidade de caminhos em largura:", cont)

resultado_busca_em_profundidade_limitada = depth_limited_search(problema, 10)

solucao_busca_em_profundidade_limitada = resultado_busca_em_profundidade_limitada.solution()

solucao_busca_em_profundidade_limitada.insert(0, estado_inicial)

print("Solução em profundidade limitada:", solucao_busca_em_profundidade_limitada)

resultado_busca_em_profundidade_iterativa = iterative_deepening_search(problema)

solucao_busca_em_profundidade_iterativa = resultado_busca_em_profundidade_iterativa.solution()

solucao_busca_em_profundidade_iterativa.insert(0, estado_inicial)

print("Solução em profundidade iterativa:", solucao_busca_em_profundidade_iterativa)