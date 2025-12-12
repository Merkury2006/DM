import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph_with_shortest_path(G, source, target, paths, lengths, filename='vizualization.png'):
    """Визуализирует граф с кратчайшим путём source-target"""

    # Создаём фигуру
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # Левый график: весь граф
    G_undir = G.to_undirected()
    pos = nx.planar_layout(G_undir)

    # Рисуем весь граф
    nx.draw_networkx_nodes(G, pos, ax=ax1, node_color='lightblue', node_size=400)
    nx.draw_networkx_edges(G, pos, ax=ax1, edge_color='gray', arrows=True, arrowsize=15)

    # Выделяем исток и сток
    nx.draw_networkx_nodes(G, pos, ax=ax1, nodelist=[source], node_color='green', node_size=400)
    nx.draw_networkx_nodes(G, pos, ax=ax1, nodelist=[target], node_color='red', node_size=400)

    # Подписи вершин
    node_labels = {i: str(i) for i in range(G.number_of_nodes())}
    node_labels[source] = 'S'
    node_labels[target] = 'T'
    nx.draw_networkx_labels(G, pos, ax=ax1, labels=node_labels, font_size=10)

    # Веса рёбер
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, ax=ax1, edge_labels=edge_labels,
                                 font_size=8, label_pos=0.5,
                                 bbox=dict(boxstyle='round,pad=0.4',
                                          facecolor='white',
                                          alpha=0.8))

    ax1.set_title(f"Планарный орграф ({G.number_of_nodes()} вершин, {G.number_of_edges()} рёбер)", fontsize=12)
    ax1.axis('off')

    # Правый график: только кратчайший путь до стока
    if target in paths:
        path_nodes = paths[target]
        path_edges = list(zip(path_nodes, path_nodes[1:]))

        # Рисуем все узлы и рёбра светлым
        nx.draw_networkx_nodes(G, pos, ax=ax2, node_color='lightblue', node_size=400)
        nx.draw_networkx_edges(G, pos, ax=ax2, edge_color='lightgray', arrows=True, arrowsize=15)

        # Выделяем путь
        nx.draw_networkx_nodes(G, pos, ax=ax2, nodelist=path_nodes, node_color='orange', node_size=400)
        nx.draw_networkx_edges(G, pos, ax=ax2, edgelist=path_edges, edge_color='red',
                              width=3, arrows=True, arrowsize=15)

        # Подписи всех вершин
        node_labels = {i: str(i) for i in range(G.number_of_nodes())}
        node_labels[source] = 'S'
        node_labels[target] = 'T'
        nx.draw_networkx_labels(G, pos, ax=ax2, labels=node_labels, font_size=10)

        # Расстояния
        for i, node in enumerate(path_nodes):
            ax2.text(pos[node][0], pos[node][1] + 0.04,
                     f"d={lengths[node]}",
                     bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7),
                     ha='center', fontsize=9)

        # Подписи рёбер пути
        path_edge_labels = {(u, v): G[u][v]['weight'] for (u, v) in path_edges if v in G[u]}
        nx.draw_networkx_edge_labels(G, pos, ax=ax2, edge_labels=path_edge_labels,
                                     font_size=8, label_pos=0.5,
                                     bbox=dict(boxstyle='round,pad=0.4',
                                              facecolor='white',
                                              alpha=0.9))

        ax2.set_title(f"Кратчайший путь S → T\nДлина = {lengths[target]}", fontsize=12)
    else:
        ax2.text(0.5, 0.5, "Путь S → T не существует",
                 ha='center', va='center', fontsize=14)
        ax2.set_title("Путь не найден")

    ax2.axis('off')

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"График сохранён как '{filename}'")
    plt.show()