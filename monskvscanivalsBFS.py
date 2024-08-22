from collections import deque

# Función para verificar si un estado es válido
def is_valid_state(state):
    monks_left, canivals_left, _ = state
    monks_rigth = 3 - monks_left
    canivals_rigth = 3 - canivals_left
    
    # Verificar si la cantidad de monjes no es superada por los caníbales en cualquier lado del río
    if (monks_left >= canivals_left or monks_left == 0) and (monks_rigth >= canivals_rigth or monks_rigth == 0):
        return True
    return False

# Función para obtener los estados sucesores válidos
def get_successors(state):
    monks_left, canivals_left, boat_position = state
    successors = []
    
    directions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for m, c in directions:
        if boat_position:  # La barca está en el lado izquierdo
            new_state = (monks_left - m, canivals_left - c, not boat_position)
        else:  # La barca está en el lado derecho
            new_state = (monks_left + m, canivals_left + c, not boat_position)
        
        if is_valid_state(new_state):
            successors.append(new_state)
    
    return successors

# Implementación de BFS para encontrar la solución
def bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        if current_state == (0, 0, False):  # Estado objetivo: todos están del lado derecho
            return path + [current_state]

        for successor in get_successors(current_state):
            queue.append((successor, path + [current_state]))
    
    return None  # Si no se encuentra solución

# Función para imprimir el estado actual en ASCII art
def print_state(monks_left, canivals_left, boat_position):
    monks_rigth = 3 - monks_left
    canivals_rigth = 3 - canivals_left
    left = f"{'M'*monks_left}{'C'*canivals_left}"
    right = f"{'M'*monks_rigth}{'C'*canivals_rigth}"
    boat = "<B" if boat_position else "B>"
    print(f"{left:6} |{boat}| {right}")

# Función para visualizar la solución paso a paso
def visualize_solution(solution):
    for state in solution:
        monks_left, canivals_left, boat_position = state
        print_state(monks_left, canivals_left, boat_position)
        print("-----RIVER-----")

# Estado inicial: 3 monjes y 3 caníbales en el lado izquierdo y la barca también.
initial_state = (3, 3, True)
solution = bfs(initial_state)

# Ejecutar y visualizar la solución
if solution:
    print("Solucion encontrada con BFS:")
    visualize_solution(solution)
else:
    print("No se encontró ninguna solución.")
