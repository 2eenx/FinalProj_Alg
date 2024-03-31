import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def recommend_route(distances, previous_nodes, charging_stations):
    recommended_routes = {}
    sorted_stations = sorted(charging_stations, key=lambda x: distances[x])

    for station in sorted_stations:
        path = []
        current_node = station
        while current_node:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        path.reverse()
        recommended_routes[station] = (path, distances[station])

    return recommended_routes

def get_valid_node(prompt, valid_nodes):
    while True:
        node = input(prompt).upper()
        if node in valid_nodes:
            return node
        else:
            print("Invalid node. Please enter a valid node.")

def main():
    graph = {
        'A': {'B': 6, 'F': 5},
        'B': {'A': 6, 'C': 5, 'G': 6},
        'C': {'B': 5, 'D': 7, 'H': 5},
        'D': {'C': 7, 'I': 8, 'E': 7},
        'E': {'D': 7, 'I': 6, 'N': 15},
        'F': {'A': 5, 'G': 8, 'J': 7},
        'G': {'F': 8, 'B': 6, 'H': 9, 'K': 8},
        'H': {'G': 9, 'C': 5, 'I': 12},
        'I': {'H': 12, 'D': 8, 'E': 6, 'M': 10},
        'J': {'F': 7, 'K': 5, 'O': 7},
        'K': {'J': 5, 'G': 8, 'L': 7},
        'L': {'K': 7, 'M': 7, 'P': 7},
        'M': {'L': 7, 'I': 10, 'N': 9},
        'N': {'M': 9, 'E': 15, 'R': 7},
        'O': {'J': 7, 'P': 13, 'S': 9},
        'P': {'O': 13, 'L': 7, 'Q': 8, 'U': 11},
        'Q': {'P': 8, 'R': 9},
        'R': {'Q': 9, 'N': 7, 'W': 10},
        'S': {'O': 9, 'T': 9},
        'T': {'S': 9, 'U': 8},
        'U': {'T': 8, 'P': 11, 'V': 8},
        'V': {'U': 8 , 'W': 5},
        'W': {'V': 5 , 'R': 10},
    }

    valid_nodes = graph.keys()
    starting_node = get_valid_node("Enter the starting node: ", valid_nodes)
    charging_stations = {'H', 'K', 'Q', 'T'}

    distances, previous_nodes = dijkstra(graph, starting_node)
    recommended_routes = recommend_route(distances, previous_nodes, charging_stations)
    
    print("Recommended routes:")
    for station, (route, distance) in recommended_routes.items():
        print(f"To station {station} (Distance: {distance}): {route}")

if __name__ == "__main__":
    main()
