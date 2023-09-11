def root(v, fork):
    for vertice in fork:
        for next_to in fork[vertice]:
            if next_to == v:
                return False
    return True

def visit(vertice, visited, ordenation, fork):
    if vertice not in visited:
        visited.add(vertice)
        for next_to in fork[vertice]:
            visit(next_to, visited, ordenation, fork)
        ordenation.insert(0, vertice)

def topDownOrdenation(fork):
    ordenation = [] 
    visited = set()
    for vertice in fork:
        if root(vertice, fork):
            visit(vertice, visited, ordenation, fork)
    return ordenation

fork = {
    '1': ['3'],
    '2': ['3', '4'],
    '3': [],
    '4': ['3', '5', '6'],
    '5': ['6'],
    '6': []
}
result = topDownOrdenation(fork)
print(result)