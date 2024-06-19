import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(grafo, nodo_inicial):
    visitados = set()
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[nodo_inicial] = 0

    cola = [(0, nodo_inicial)]

    while cola:
        (dist, actual) = heapq.heappop(cola)
        if actual in visitados:
            continue
        visitados.add(actual)
        print(f'Recorrido: {actual}, Costo acumulado: {dist}')

        for siguiente, peso in grafo.get(actual, []):
            nueva_dist = dist + int(peso)
            if nueva_dist < distancias[siguiente]:
                distancias[siguiente] = nueva_dist
                heapq.heappush(cola, (nueva_dist, siguiente))

    return distancias

def graficar_grafo(grafo, distancias, nodo_inicial):
    G = nx.DiGraph()
    for nodo, adyacentes in grafo.items():
        for vecino, peso in adyacentes:
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', linewidths=1, font_size=15)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Resaltar el camino más corto
    for nodo, dist in distancias.items():
        if dist != float('inf') and nodo != nodo_inicial:
            path_edges = [(nodo_inicial, nodo)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

    plt.title("Recorrido del grafo usando Dijkstra")
    plt.show()

# Configuración del grafo
grafo = {
    'entrada': [('sala', 1), ('cuarto_PB', 1)],
    'sala': [('comedor', 2), ('escaleras', 2)],
    'cuarto_PB': [],
    'comedor': [('baño_PB', 2), ('cocina', 4)],
    'baño_PB': [],
    'cocina': [('cuarto_lavado', 5), ('patio_Tracero', 5)],
    'cuarto_lavado': [],
    'patio_Tracero': [],
    'escaleras': [('planta_Alta', 2)],
    'planta_Alta': [('Cuarto_PA_1', 9), ('vestibulo', 8), ('baño_PA', 9), ('cuarto_2_PA', 11)],
    'Cuarto_PA_1': [],
    'vestibulo': [],
    'baño_PA': [],
    'cuarto_2_PA': [('baño_cuarto', 11), ('valcon', 12)],
    'baño_cuarto': [],
    'valcon': []
}

# Solicitar el nodo inicial al usuario
nodo_inicial = input("Ingrese el nodo inicial: ")
if nodo_inicial not in grafo:
    print("Nodo inicial no válido")
else:
    distancias = dijkstra(grafo, nodo_inicial)
    graficar_grafo(grafo, distancias, nodo_inicial)
    print(f"Distancias desde '{nodo_inicial}': {distancias}")
