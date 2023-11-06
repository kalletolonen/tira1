def find_factors(n):
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
    return factors

def build_graph(N):
    graph = {}
    for i in range(2, N + 1):
        factors = find_factors(i)
        graph[i] = factors
    return graph

def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def count_components(N):
    graph = build_graph(N)
    visited = set()
    components = 0

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            components += 1

    return components

if __name__ == "__main__":
    N = 10000
    components = count_components(N)
    print(f"Verkon komponenttien määrä N={N}: {components}")
