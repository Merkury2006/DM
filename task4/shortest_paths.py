import os

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


def save_shortest_paths_to_csv(G, source, target, lengths, paths, filename='n2.csv'):
    """Сохраняет пути в таблицу"""

    data = []
    for node in sorted(G.nodes()):
        if node == source:
            continue

        if node == target:
            path_str = ' → '.join(map(str, paths[node]))
            data.append(['T', lengths[node], path_str])

        elif node in lengths and lengths[node] != float('inf'):
            path_str = ' → '.join(map(str, paths[node]))
            data.append([node, lengths[node], path_str])

        else:
            data.append([node, 0, 'недостижима'])

    df = pd.DataFrame(data, columns=['Вершина', 'Длина', 'Путь'])

    df.to_csv(filename, sep=';', index=False, encoding='utf-8-sig')

    print(f"Таблица сохранена в '{filename}'")