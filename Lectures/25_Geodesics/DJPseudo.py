def Dijsktra(Graph, source):
    list dists
    list prev
    dist[source] = 0
    Queue Q
    for vertex v in Graph:
        if v not source:
            dists[v] = Infinity
            prev[v] = Undefined
        Q.add(v, dists[v])
    while len(Q) > 0:
        u = Q.getMin()
        for v in neighbors(u):
            d = dists[u] + length(u, v)
            if d < dists[v]:
                dists[v] = d
                prev[v] = u
                Q.decreasePriority(v, d)
    return (dist, prev)
