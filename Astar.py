class AStarGraph(object):
    def __init__(self):
        self.barriers=[]
        t=int(input("Enter total barriers"))
        for i in range(t):
            x=int(input("Enter row number for barrier point="))
            y=int(input("Enter column number for barrier point="))
            self.barriers.append([x,y])
            
    def heuristic(self, start,goal):
        D=1
        D2=1
        dx= abs(start[0]-goal[0])
        dy= abs(start[1]-goal[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
    
    def get_vertex_neighbours(self,pos):
        n = []
        for dx,dy in [(1,0), (-1,0), (0,1),(0,-1), (1,1)]:
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            if x2 < 0 or x2 > 5 or y2 < 0 or y2 > 5:
                continue
            n.append((x2,y2))
        return n
    def move_cost(self, a, b):
        for barrier in self.barriers:
            if b in barrier:
                return 100
        return 1
    
def AStarSearch(start, end, graph):
    G={}
    F={}
    
    
    G[start] = 0
    F[start] = graph.heuristic(start, end)
    
    closedVertices= set()
    openVertices = set([start])
    cameFrom = {}
    
    while len(openVertices) > 0:
        
        current = None
        currentFscore = None
        for pos in openVertices:
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos
        if current == end:
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            return path, F[end]
        openVertices.remove(current)
        closedVertices.add(current)
        
        
        for neighbour in graph.get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue
            candidateG= G[current] + graph.move_cost(current, neighbour)
            
            if neighbour not in openVertices:
                openVertices.add(neighbour)
            elif candidateG >= G[neighbour]:
                continue
            
            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H
            
    raise RuntimeError("A* failed to find a solution")
 
if __name__ == "main":
    
    graph = AStarGraph()
    s1= int(input("Enter row number for start point="))
    s2 = int(input("enter column number for start point="))
    g1 = int(input("Enter row number for goal point="))
    g2= int(input("Enter column number for goal point="))
    result, cost = AStarSearch((s1,s2),(g1,g2),graph)
    print("route", result)
    print("cost", cost)
    

                
    