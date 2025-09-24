def mst(file_path):
    graph = {}
    with open(file_path) as f:
        for line in f:
            u, v, w = line.split()
            w = int(w)
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))
            graph[v].append((u, w))
    nodes = list(graph.keys())
    visited = set([nodes[0]])
    mst_edges = []
    while len(visited) < len(nodes):
        min_edge = None
        min_w = float('inf')
        for u in visited:
            for v, w in graph[u]:
                if v not in visited and w < min_w:
                    min_w = w
                    min_edge = (u, v, w)
        if min_edge:
            u, v, w = min_edge
            visited.add(v)
            mst_edges.append((u, v, w))
    return mst_edges
print(mst("edges.txt"))
