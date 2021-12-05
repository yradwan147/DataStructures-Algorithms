import math

def shortest_path(M,start,goal):
    print("shortest path called")
    res = [start]
    if start == goal:
        return res
    total_cost = {}
    frontier = []
    explored = []
    frontier.extend(M.roads[start])
    node = start
    while goal not in explored:
        options_f = []
        for option in frontier:
            options_f.append(calculate_f(node, option, goal, M, total_cost))
            print(str(option) + ":" + str(calculate_f(node, option, goal, M, total_cost)))
        current_node = frontier[options_f.index(min(options_f))]
        res.append(current_node)
        explored.append(current_node)
        frontier.remove(current_node)
        new_front = M.roads[current_node]
        for path in new_front:
            if path not in explored and path not in frontier:
                frontier.append(path)
                total_cost[path] = calc_g(path, node, M)
        if node in frontier:
            frontier.remove(node)
        node = current_node
        total_cost[start] = 0
        print("I'm on " + str(node) + "\nFrontier is:\n" + str(frontier) + "\nExplored is:\n" + str(explored)+ "\nResult:\n" + str(res))
    #print(res)
    for x in range(1,len(res)):
        if res[-x] == start:
            res = res[-x:]
            break
    return res

def calculate_f(node, neighbor, goal, M, total_cost):
    g = shortest_distance(M, node, neighbor) + total_cost.get(node,0)
    h = shortest_distance(M, neighbor, goal)
    print("g:{}".format(g))
    print("h:{}".format(h))
    return g + h

def calc_g(node, neighbor, M):
    return shortest_distance(M, node, neighbor)

def shortest_distance(M, node1, node2):
    #print(M.intersections[node1], M.intersections[node2])
    return math.sqrt((M.intersections[node1][0]-M.intersections[node2][0])**2 + (M.intersections[node1][1]-M.intersections[node2][1])**2)