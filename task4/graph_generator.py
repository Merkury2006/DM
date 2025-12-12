import networkx as nx
import random


def get_planar_graph_with_requirements(n=8, m=11, source=0, target=7, max_attempts=1000):
    """
    Генерирует планарный граф с нужными для нас свойствами
    """
    for attempt in range(1, max_attempts + 1):
        try:
            # ШАГ 1: Начинаем с простого пути со случайным порядком вершин
            g = nx.path_graph(n)
            nodes = list(range(n))
            random.shuffle(nodes)
            mapping = {i: nodes[i] for i in range(n)}
            g = nx.relabel_nodes(g, mapping)

            # ШАГ 2: Удаляем прямое ребро source-target если оно есть
            if g.has_edge(source, target):
                g.remove_edge(source, target)
                # Добавляем другое ребро для компенсации
                for u in range(n):
                    for v in range(u + 1, n):
                        if not g.has_edge(u, v) and u != source and v != target:
                            g.add_edge(u, v)
                            break

            # ШАГ 3: Гарантируем минимальные соединения target и source
            if g.degree(source) == 0:
                for v in g.nodes():
                    if v != source and v != target:
                        g.add_edge(source, v)
                        break

            if g.degree(target) == 0:
                for v in g.nodes():
                    if v != target and v != source and not g.has_edge(target, v):
                        g.add_edge(target, v)
                        break

            # ШАГ 4: Корректируем количество рёбер до m
            current = g.number_of_edges()

            if current < m:
                edges_needed = m - current
                added = 0

                # Список всех возможных рёбер (кроме source-target)
                possible_edges = []
                for u in range(n):
                    for v in range(u + 1, n):
                        if (not g.has_edge(u, v) and
                                not (u == source and v == target) and
                                not (v == source and u == target)):
                            possible_edges.append((u, v))

                random.shuffle(possible_edges)

                for u, v in possible_edges:
                    if added >= edges_needed:
                        break

                    g_test = g.copy()
                    g_test.add_edge(u, v)

                    if nx.check_planarity(g_test)[0]:
                        g.add_edge(u, v)
                        added += 1

            elif current > m:
                # Удаляем лишние рёбра (кроме критических)
                to_remove = current - m

                for _ in range(to_remove * 2):  # Даём несколько попыток
                    if to_remove <= 0:
                        break

                    # Находим безопасное для удаления ребро
                    safe_edges = []
                    for u, v in g.edges():
                        # Не удаляем если это единственное соединение source/target
                        if ((u == source or v == source) and g.degree(source) == 1) or \
                                ((u == target or v == target) and g.degree(target) == 1):
                            continue
                        safe_edges.append((u, v))

                    if not safe_edges:
                        break

                    # Удаляем случайное безопасное ребро
                    u, v = random.choice(safe_edges)
                    g.remove_edge(u, v)
                    to_remove -= 1

            # ШАГ 5: Финальная проверка
            if check_graph_requirements(g, m, source, target):
                return g

        except Exception:
            continue

    print(f"Не удалось создать граф за {max_attempts} попыток")
    return None


def check_graph_requirements(g, m, source, target):
    """Проверяет требования к графу"""
    if g is None:
        return False
    if g.number_of_edges() != m:
        print(f"  Неправильное число рёбер: {g.number_of_edges()} вместо {m}")
        return False
    if not nx.is_connected(g):
        print(f"  Граф не связный")
        return False
    if g.degree(source) == 0:
        print(f"  Source изолирован")
        return False
    if g.degree(target) == 0:
        print(f"  Target изолирован")
        return False
    if g.has_edge(source, target):
        print(f"  Есть прямое ребро source-target")
        return False
    try:
        if not nx.check_planarity(g)[0]:
            print(f"  Граф непланарен")
            return False
    except:
        print(f"  Ошибка проверки планарности")
        return False
    return True


def orient_graph(undirected_g, source, target):
    """Ориентирует граф"""
    if undirected_g is None:
        return None

    G = nx.DiGraph()
    G.add_nodes_from(undirected_g.nodes())

    for u, v in undirected_g.edges():
        if u == source or v == source:
            # От source
            start = source
            end = v if u == source else u
        elif u == target or v == target:
            # К target
            start = v if u == target else u
            end = target
        else:
            # Случайное направление
            start, end = (u, v) if random.choice([True, False]) else (v, u)

        G.add_edge(start, end, weight=random.randint(1, 20))

    return G


def generate_planar_flow_network(n=8, m=11, source=0, target=7):
    """
    Генерирует ориентированный планарный граф
    """
    # Генерируем неориентированный граф
    undirected = get_planar_graph_with_requirements(n, m, source, target)

    if undirected is None:
        print("Не удалось сгенерировать базовый граф")

    # Ориентируем
    directed = orient_graph(undirected, source, target)

    return directed


def create_set_graph(edges=None, n=8):
    """Создаёт ориентированный граф из заданного списка рёбер."""
    if edges is None:
        edges = [
            (0, 1, 5), (0, 2, 3), (1, 3, 2),
            (2, 3, 4), (3, 4, 6), (4, 5, 3),
            (5, 6, 2), (6, 7, 4), (1, 4, 3),
            (2, 5, 5), (3, 6, 4)
        ]

    G = nx.DiGraph()
    G.add_nodes_from(range(n))

    for edge in edges:
        u, v, weight = edge
        G.add_edge(u, v, weight=weight)
    return G