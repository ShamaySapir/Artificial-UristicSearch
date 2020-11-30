import pandas as pd
from queue import PriorityQueue


# The function initializes and returns open
def init_open():
    return PriorityQueue()


# The function inserts s into open
def insert_to_open(open_list, s):  # Should be implemented according to the open list data structure
    open_list.put(s)


# The function returns the best node in open (according to the search algorithm)
def get_best(open_list):
    return open_list.get()


# The function checks out of boundaries
def out_of_boundaries(shape, location):
    rows = shape[0]
    cols = shape[1]
    x = location[0]
    y = location[1]
    if x > rows - 1 or x < 0:
        return True
    elif y > cols - 1 or y < 0:
        return True
    else:
        return False


# The function checks blocked location
def blocked_location(grid, location):
    return grid.item(location) == '@'


# The function checks if the location is legal
def is_legal(grid, location):
    if out_of_boundaries(grid.shape, location) or blocked_location(grid, location):
        return False
    return True


# The function returns neighboring locations of s_location
def get_neighbors(grid, s_location):
    neighbors = []
    x = s_location[0]
    y = s_location[1]
    potential_neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for potential_neighbor in potential_neighbors:
        if is_legal(grid, potential_neighbor):
            neighbors.append(potential_neighbor)
    return neighbors


# The function returns whether or not s_location is the goal location
def is_goal(s_location, goal_location):
    s_x = s_location[0]
    s_y = s_location[1]
    goal_x = goal_location[0]
    goal_y = goal_location[1]
    return s_x == goal_x and s_y == goal_y


# The function calculates manhattan distance
def manhattan_distance(s_x, s_y, g_x, g_y):
    return abs(s_x - g_x) + abs(s_y - g_y)


# The function estimates the cost to get from s_location to goal_location
def calculate_heuristic(s_location, goal_location):
    s_x = s_location[0]
    s_y = s_location[1]
    g_x = goal_location[0]
    g_y = goal_location[1]
    return manhattan_distance(s_x, s_y, g_x, g_y)


# Locations are tuples of (x, y)
def astar_search(grid, start_location, goal_location):
    # State = (f, g, h, x, y, s_prev) # f = g + h (For Priority Queue)
    # Start_state = (0, 0, 0, x_0, y_0, False)
    start = (0, 0, 0, start_location[0], start_location[1], False)
    open_list = init_open()
    closed_list = set()
    # Mark the source node as
    # visited and enqueue it
    insert_to_open(open_list, start)
    while not open_list.empty():
        # Dequeue a vertex from
        # queue and print it
        s = get_best(open_list)
        s_location = (s[3], s[4])
        if s_location in closed_list:
            continue
        if is_goal(s_location, goal_location):
            print("The number of states visited by AStar Search:", len(closed_list))
            return s
        neighbors_locations = get_neighbors(grid, s_location)
        for n_location in neighbors_locations:
            if n_location in closed_list:
                continue
            h = calculate_heuristic(n_location, goal_location)
            g = s[2] + 1
            f = g + h
            n = (f, h, g, n_location[0], n_location[1], s)
            insert_to_open(open_list, n)
        closed_list.add(s_location)


def print_route(s):
    for r in s:
        print(r)


def get_route(s):
    route = []
    while s:
        s_location = (s[3], s[4])
        route.append(s_location)
        s = s[5]
    route.reverse()
    return route


def print_grid_route(route, grid):
    for location in route:
        grid[location] = 'x'
    print(pd.DataFrame(grid))
