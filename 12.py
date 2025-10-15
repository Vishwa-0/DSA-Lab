def dijkstra(graph, src, dest):
    n = len(graph)
    sptSet = [False] * n         
    dist = [float('inf')] * n    
    dist[src] = 0                
    prev = [-1] * n             

    for _ in range(n):
        u = -1
        min_dist = float('inf')
        for i in range(n):
            if not sptSet[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:
            break
        sptSet[u] = True        
        for v in range(n):
            if graph[u][v] > 0 and not sptSet[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    prev[v] = u
    path = []
    current = dest
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()

    if dist[dest] == float('inf'):
        print("No path found from city", src, "to city", dest)
    else:
        print("Shortest path:", ' -> '.join(map(str, path)))
        print("Distance:", dist[dest])
n = int(input("Enter number of cities: "))
print("Enter adjacency matrix (0 if no direct path):")
graph = [list(map(int, input().split())) for _ in range(n)]
src = int(input(f"Enter source city (0 to {n-1}): "))
dest = int(input(f"Enter destination city (0 to {n-1}): "))
dijkstra(graph, src, dest)
''''
Enter number of cities: 5
Enter adjacency matrix (0 if no direct path):
0 10 0 30 100
10 0 50 0 0
0 50 0 20 10
30 0 20 0 60
100 0 10 60 0
Enter source city (0 to 4): 0
Enter destination city (0 to 4): 4
'''