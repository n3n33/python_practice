graph_dict = {}
graph_dict['A'] = 'B', 'C'
graph_dict['B'] = 'A', 'D'
graph_dict['C'] = 'A', 'G', 'H', 'I'
graph_dict['D'] = 'B', 'E', 'F'
graph_dict['E'] = 'D'
graph_dict['F'] = 'D'
graph_dict['G'] = 'C'
graph_dict['H'] = 'C'
graph_dict['I'] = 'C', 'J'
graph_dict['J'] = 'I'

def dfsFunc(graph, start):
    visited = []
    needVisit = []
    needVisit.append(start)

    while needVisit:
        node = needVisit.pop()
        if node not in visited:
            visited.append(node)
            needVisit.extend(graph[node])

    return visited

print(dfsFunc(graph_dict, 'A'))