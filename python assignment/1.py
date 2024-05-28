import turtle
import heapq
from PIL import Image

# Step 1: Read the text file and convert it into a 2D list
def read_map(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    array = [[1 if char != ' ' else 0 for char in line.strip()] for line in lines]
    return array

# Step 2: Implement A* algorithm for pathfinding including diagonal moves
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(array, start, goal):
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []
    
    heapq.heappush(oheap, (fscore[start], start))
    
    while oheap:
        current = heapq.heappop(oheap)[1]
        
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            data.append(start)
            return data[::-1]
        
        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + 1
            
            if 0 <= neighbor[0] < len(array):
                if 0 <= neighbor[1] < len(array[0]):                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
    
    return False

# Step 3: Draw the path using Turtle graphics
def draw_path_on_image(image_path, path, scale=10):
    screen = turtle.Screen()
    screen.setup(width=769, height=757)
    screen.bgpic(image_path)
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    
    for (x, y) in path:
        t.goto(x * scale - 384, 378 - y * scale)
        t.pendown()
    
    screen.mainloop()

# Example usage
array = read_map('map.txt')
start = (409, 334)  # Replace with actual start indices
goal = (594, 696)  # Replace with actual goal indices

path = astar(array, start, goal)
if path:
    draw_path_on_image('지도3.png', path)
else:
    print("No path found")
