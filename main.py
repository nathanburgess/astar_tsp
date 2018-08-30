from heapq import heappush, heappop, heapify
from node import Node
from grid import Grid


#
# My A* implementation
#
# Given an initial state, along with a starting point and an end goal, this
# algorithm will find the shortest path between two points that hasn't been
# used previously
#
def a_star(initial_state, start, finish):
    # Create the initial node and set it's tracking and start states
    state = Node(initial_state.board[:], initial_state.size)
    state.tracked = initial_state.board[:]
    state.set_start(start)

    # Instantiate an empty frontier
    frontier = []
    # Push our first state into the frontier
    heappush(frontier, state)
    # Instantiate an empty set to track explored states
    explored = set()

    # So long as there is something in the frontier, we have work to do
    while frontier:
        state = heappop(frontier)
        explored.add(state)
        state.curr_pos = start[1]

        # When we've reached the target position, return the state
        if finish[1] == state.current_position:
            return state

        # Create all possible children and iterate through them
        for child in state.expand(finish):
            # If this is a totally new child, push it onto the frontier
            if child not in frontier and child not in explored:
                heappush(frontier, child)
            # Otherwise, if it's on the frontier, it needs to be reordered
            elif child in frontier:
                # A* needs a priority queue, but heapq doesn't provide an implementation
                # So, this is using heapq as a priority queue
                # 1) Remove the child from the frontier
                frontier.remove(child)
                # 2) Update it's heuristic
                child.heuristic -= 1
                # 3) Push it back into the heap
                heappush(frontier, child)
                # 4) Run heapify to re-optimize the heap with the updated child
                heapify(frontier)

    print("Sorry, but a solution could not be found. :(");
    exit()


#
# Due to the need to change the path beginning and ending, this function
# simply loops over the list of stops and performs the A* search on each
# set of stops while preserving previous paths
#
def solve(grid):
    path = []

    # Get the stops as a properly ordered list
    stops = list(reversed(grid.stops.items()))

    # Get the start position
    start = stops.pop()

    # Loop over all the stops and find their paths
    while stops:
        # Get the stop position
        finish = stops.pop()

        # Run the A* algorithm on this set of points
        solution = a_star(grid, start, finish)

        # Backtrack through the solution tree and get the path
        temp = solution
        temp_path = [temp.direction]
        while temp.depth > 1:
            temp = temp.parent
            temp_path.append(temp.direction)

        # Merge the solution board with the original board to preserve the paths
        grid.merge_board(solution.board)
        # Add the path for this solution to the overall path
        path.append(list(reversed(temp_path)))

        # Move the starting position forward
        start = finish

    return grid, path


# Create a grid and add some stops
grid = Grid(10)
grid.add_stop((1, 1), 'A')
grid.add_stop((5, 3), 'B')
grid.add_stop((2, 8), 'C')
grid.add_stop((4, 1), 'D')

# Solve the grid
solution, path = solve(grid)

# Print the final solution and the path it took
print(solution)
print(path)
