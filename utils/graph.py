from typing import List, Dict

def isDag(nodes: List[Dict], edges: List[Dict]) -> bool:
    adjacencyList = {node.id: [] for node in nodes}
    inDegree = {node.id: 0 for node in nodes}
    
    for edge in edges:
        source = edge.source
        target = edge.target
        adjacencyList[source].append(target)
        inDegree[target] += 1
    
    zeroInDegree = [nodeId for nodeId in inDegree if inDegree[nodeId] == 0]
    
    count = 0
    while zeroInDegree:
        current = zeroInDegree.pop()
        count += 1
        
        for neighbor in adjacencyList[current]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                zeroInDegree.append(neighbor)
    
    return count == len(nodes)
