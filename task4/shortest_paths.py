import csv

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


def save_shortest_paths_to_csv(G, source, lengths, paths, filename='shortest_paths.csv'):
    """Сохраняет кратчайшие пути в CSV файл"""
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Вершина', 'Длина', 'Путь'])

        for node in sorted(G.nodes()):
            if node == source:
                continue
            elif node in lengths and lengths[node] != float('inf'):
                path_str = ' → '.join(map(str, paths[node]))
                writer.writerow([node, lengths[node], path_str])
            else:
                writer.writerow([node, 0, 'недостижима'])

    print(f"Таблица сохранена в '{filename}'")