from task4.graph_generator import generate_planar_flow_network,create_set_graph
from task4.shortest_paths import calculate_shortest_paths, save_shortest_paths_to_csv
from task4.vizualization import visualize_graph_with_shortest_path


def main():
    # Параметры
    n = 8
    m = 11
    source = 0
    target = 7
    edges = [
        (0, 1, 5), (0, 2, 3), (1, 3, 2),
        (2, 3, 4), (3, 4, 6), (4, 5, 3),
        (5, 6, 2), (6, 7, 4), (1, 4, 3),
        (2, 5, 5), (3, 6, 4)
    ]

    # Начальный этап - генерация графа
    print("1. Генерация планарного орграфа")

    # G = generate_planar_flow_network(n, m, source, target)

    G = create_set_graph(edges, n)

    if G is None:
        print("Ошибка: не удалось сгенерировать граф")
        return

    print(f"Граф создан успешно")
    print(f"Вершин: {G.number_of_nodes()}")
    print(f"Рёбер: {G.number_of_edges()}")

    # Задание 2
    lengths, paths = calculate_shortest_paths(G, source)

    save_shortest_paths_to_csv(G, source, lengths, paths, 'shortest_paths.csv')

    # Задание 3
    visualize_graph_with_shortest_path(G, source, target, paths, lengths)

if __name__ == "__main__":
    main()