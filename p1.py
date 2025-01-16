import heapq
import random

# Define the grid dimensions and obstacles
grid_size = 10
obstacles = [(3, 3), (4, 4), (5, 5)]

# Generate random starting point and treasure location
start = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
treasure = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
print(f"Treasure is located at: {treasure}")

# BFS Implementation
def bfs(grid, start, target):
    from collections import deque
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        current = queue.popleft()
        if current == target:
            return True
        for neighbor in get_neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

# A* Search Implementation
def a_star(grid, start, target):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, target)}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == target:
            return reconstruct_path(came_from, current)
        for neighbor in get_neighbors(grid, current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, target)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return []

# Hill Climbing Implementation
def hill_climbing(grid, start, target):
    current = start
    while current != target:
        next_step = min(get_neighbors(grid, current), key=lambda x: heuristic(x, target))
        if heuristic(next_step, target) >= heuristic(current, target):
            break
        current = next_step
    return current

# Helper functions
def get_neighbors(grid, node):
    x, y = node
    neighbors = [(x+dx, y+dy) for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in obstacles]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path[::-1]

# Main Game Execution
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
for obs in obstacles:
    grid[obs[0]][obs[1]] = 1

path_to_treasure = a_star(grid, start, treasure)
print("Path to treasure:", path_to_treasure)