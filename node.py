class Node:
    def __init__(self, board, size, parent=None, direction="None"):
        self.board = board
        self.size = size
        self.parent = parent
        self.direction = direction
        self.depth = (parent.depth + 1) if parent else 0
        self.cost = 1
        self.heuristic = 0
        self.current_position = None
        self.tracked = []

    #
    # In order to check for whether or not this node already exists, there
    # must be a way to uniquely identify it without being too unique
    #
    def __hash__(self):
        return hash(str(self.board))

    #
    # In order to use this class in a heap, we must be able to perform equality
    # checks to determine sorting
    #
    def __lt__(self, other):
        return self.heuristic < other.heuristic

    #
    # This method allows the node's cost to be updated
    #
    def calculate_heuristic(self, value=0):
        self.heuristic = self.depth + value

    #
    # Set the board's start position
    #
    def set_start(self, start):
        self.board[start[1]] = '*'

    #
    # Figure out which directions are valid moves for the current position
    #
    def test_dir(self, d, pos):
        x = pos % self.size
        y = int(pos / self.size)

        if d == "n":
            if y - 1 >= 0:
                return pos - self.size
        elif d == "s":
            if y + 1 < self.size:
                return pos + self.size
        elif d == "e":
            if x + 1 < self.size:
                return pos + 1
        elif d == "w":
            if x - 1 >= 0:
                return pos - 1
        return -1

    #
    # Create a list of child nodes containing all possible moves from the
    # current position towards the target
    #
    def expand(self, target):
        children = []

        pos = self.board.index('*')
        t_sym = target[0]
        t_pos = target[1]

        for direction in ["n", "s", "e", "w"]:
            move = self.test_dir(direction, pos)

            # Can't do anything if the move isn't valid
            if not move or move < 0:
                continue

            # We have to make sure we're only considering blank positions to move
            # into, unless the move is our target
            if self.tracked[move] is not 0 and self.tracked[move] is not t_sym:
                continue

            # Copy the board
            board = self.board[:]
            # Update the symbols for pathing
            board[move], board[pos] = '*', 'X'

            # Create a new node
            node = Node(board, self.size, self, direction)
            # Track it's current_position
            node.current_position = move
            # Calculate it's heuristic cost using Manhattan Distance
            node.calculate_heuristic(self.manhattan_distance(move, t_pos))
            # Copy the tracked history
            node.tracked = self.tracked[:]

            # If there is a current_position, set it as tracked
            if self.current_position:
                node.tracked[self.current_position] = 'X'
            # Track the move
            node.tracked[move] = 'X'

            # Add this node to the children
            children.append(node)

        # Return those babies!
        return children

    #
    # Manhattan Distance is simply the distance between two cells on a grid
    #
    def manhattan_distance(self, p1, p2):
        x1 = p1 % self.size
        y1 = p1 / self.size
        x2 = p2 % self.size
        y2 = p2 / self.size
        return abs(x1 - x2) + abs(y1 - y2)
