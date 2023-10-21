import sys


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        # path cost ?


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty Frountier")
        else:
            # -1 gives the last item in the list, like 0 gives the first
            node = self.fronties[-1]
            # from the begining till the last one(excluding)
            self.frontier = self.frontier[:-1]
            return node


# inherits Stackfrontiers, so does everything like other class, just one def is different
class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("Empty Frountier")
        else:
            # 0 gives the first
            node = self.fronties[0]
            # from 1st(inclusive, all the way)
            self.frontier = self.frontier[1:]
            return node


class Maze():
    def __init__(self, filename):

        # Read file and set height and width of maze
        with open(filename) as f:


def solve(self):
    """ Finds a solution to maze, if one exists """

    # Keep track of number of states explored
    self.num_explored = 0

    # Initialize frontier to just the starting position
    start = Node(state=self.start, parent=None, action=None)
    frontier = StackFrontier()
    frontier.add(start)

    # Initialize an empty explored set
    self.explored = set()

    # Keep looping until soln is found
    while True:

        # If nothing left in Frontier, then no path
        if frontier.empty():
            raise Exception("no solution")

        # Choose a node from the frontier
        node = frontier.remove()
        self.num_explored += 1

        # If node is the goal, then we have a solution
        if node.state == self.goal:
            actions = []
            cells = []

            # Follow parent nodes to find solution
            while node.parent is not None:
                action.append(node.action)
                cells.append(node.state)
                node = node.parent

            # inbuilt function which reverse the
            actions.reverse()
            cells.reverse()

            self.solution = (action, cells)
            return

        # Mark node as explored
        self.explored.add(node.state)

        # Add neighbours to frontier
        for action, state in self.neighbors(node.state):
            if not frontier.contains_state(state) and state not in self.explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)
