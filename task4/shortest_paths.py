import pandas as pd

import networkx as nx


def calculate_shortest_paths(G, source):
    """Вычисляет кратчайшие пути алгоритмом Дейкстры"""
    try:
        lengths = nx.single_source_dijkstra_path_length(G, source=source, weight='weight')
        paths = nx.single_source_dijkstra_path(G, source=source, weight='weight')
        return lengths, paths
    except nx.NetworkXNoPath:
        print("Нет пути из истока в некоторые вершины")
        return {}, {}


def save_shortest_paths_to_table(G, source, target, lengths, paths, filename='n2.xlsx'):
    """Сохраняет в таблицу"""
    data = []

    for node in sorted(G.nodes()):
        if node == source:
            continue

        if node in paths:
            # Заменяем 0 на S, 7 на T
            path_list = []
            for v in paths[node]:
                if v == source:
                    path_list.append('S')
                elif v == target:
                    path_list.append('T')
                else:
                    path_list.append(str(v))
            path_str = ' → '.join(path_list)
        else:
            path_str = 'недостижима'

        # Имя вершины
        if node == target:
            vertex_name = 'T'
        else:
            vertex_name = str(node)

        # Длина
        if node in lengths and lengths[node] != float('inf'):
            path_len = lengths[node]
        else:
            path_len = 0

        data.append([vertex_name, path_len, path_str])

    df = pd.DataFrame(data, columns=['Вершина', 'Длина', 'Путь'])

    df.to_excel(filename, index=False)
    print(f"Файл сохранен в '{filename}'")