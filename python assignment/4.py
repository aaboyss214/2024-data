from collections import deque
import turtle

def read_map(filename):
    graph = []
    with open(filename, 'r') as file:
        for line in file:
            graph.append(list(line.strip('\n')))
    return graph

def bfs(graph, start, goal):
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),  # 상하좌우
        (1, 1), (1, -1), (-1, 1), (-1, -1) # 대각선
    ]
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    
    while queue:
        node = queue.popleft()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        
        row, col = node
        for dr, dc in directions:
            n_row, n_col = row + dr, col + dc
            if 0 <= n_row < len(graph) and 0 <= n_col < len(graph[0]):  # 유효한 범위 확인
                if graph[n_row][n_col] == ' ' and (n_row, n_col) not in visited:
                    queue.append((n_row, n_col))
                    parent[(n_row, n_col)] = node
                    visited.add((n_row, n_col))
    return None

def visualize_path_turtle(graph, path, width, height, image):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgpic(image)
    
    t = turtle.Turtle()
    t.speed(1)
    t.color('blue')
    t.penup()

    # 텍스트 좌표를 터틀 좌표로 변환하는 함수
    def text_to_turtle_coords(text_y, text_x, width, height):
        turtle_x = text_x - width // 2
        turtle_y = height // 2 - text_y
        return turtle_x, turtle_y
    t.shape('turtle')
    start_turtle_coords = text_to_turtle_coords(path[0][0], path[0][1], width, height)
    t.goto(start_turtle_coords)
    t.pendown()

    for node in path[1:]:
        turtle_coords = text_to_turtle_coords(node[0], node[1], width, height)
        t.goto(turtle_coords)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    filename = 'map.txt'
    image = '지도3.png'  # 지도 이미지 파일 경로
    width = 769  # 터틀 그래픽 창 너비 (이미지 너비와 일치시켜야 함)
    height = 757  # 터틀 그래픽 창 높이 (이미지 높이와 일치시켜야 함)
    
    # 예시 시작점과 목표점 (인덱스로 주어짐)
    start = (409, 334)  # 예시 시작점 (파일 내용에 맞게 변경)
    goal = (594, 696)  # 예시 목표점 (파일 내용에 맞게 변경)
    
    graph = read_map(filename)
    
    path = bfs(graph, start, goal)
    
    if path:
        print("최단 경로를 찾았습니다:")
        visualize_path_turtle(graph, path, width, height, image)
    else:
        print("목표 지점에 도달할 수 없습니다.")
