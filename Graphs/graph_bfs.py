def graph(test_graph, start):
    queue = [start]
    visited_nodes = []
    while queue:
        i = queue.pop(0)
        if i not in visited_nodes:
            visited_nodes.append(i)
            for node in test_graph[i]:
                queue.append(node)
    print(visited_nodes)


if __name__ == '__main__':
    graph({1: [2, 3], 2: [1, ], 3: [1, 4, 5], 4: [3, ], 5: [3, ]}, 5)
