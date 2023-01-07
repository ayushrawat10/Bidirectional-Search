# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import time
from game import Directions
direction = {'North': 'South', 'East': 'West', 'South': 'North', 'West': 'East'}

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    fringe.push(problem.getStartState())
    closedSet = set()
    parentDict = {}
    goalState = ()

    while fringe.isEmpty != 1:
        stateToExplore = fringe.pop()
        closedSet.add(stateToExplore)
        if problem.isGoalState(stateToExplore):
            goalState = stateToExplore
            break

        successors = problem.getSuccessors(stateToExplore)
        for successor in successors:
            (pos, action, cost) = successor
            if(pos in closedSet):
                continue
            fringe.push(pos)
            parentDict[pos] = (stateToExplore, action)

    actions = []
    while goalState!=problem.getStartState():
        (goalState, action) = parentDict[goalState]
        actions.append(action)

    actions.reverse()
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    fringe = util.Queue()
    fringe.push(problem.getStartState())
    closedSet = set()
    parentDict = {}
    goalState = ()

    while fringe.isEmpty != 1:
        stateToExplore = fringe.pop()
        closedSet.add(stateToExplore)
        if problem.isGoalState(stateToExplore):
            goalState = stateToExplore
            break

        successors = problem.getSuccessors(stateToExplore)
        for successor in successors:
            (pos, action, cost) = successor
            if(pos in closedSet):
                continue
            fringe.push(pos)
            closedSet.add(pos)
            parentDict[pos] = (stateToExplore, action)

    actions = []
    while goalState!=problem.getStartState():
        (goalState, action) = parentDict[goalState]
        actions.append(action)

    actions.reverse()
    return actions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), 0), 0)
    closedSet = set()
    parentDict = {}
    goalState = ()

    while fringe.isEmpty != 1:
        stateToExplore, pathCost = fringe.pop()
        closedSet.add(stateToExplore)
        if problem.isGoalState(stateToExplore):
            goalState = stateToExplore
            break

        successors = problem.getSuccessors(stateToExplore)
        for successor in successors:
            (pos, action, cost) = successor
            if(pos in closedSet and not problem.isGoalState(pos)):
                continue
            fringe.push((pos, cost + pathCost), cost + pathCost)
            closedSet.add(pos)
            parentDict[pos] = (stateToExplore, action)

    actions = []
    while goalState!=problem.getStartState():
        (goalState, action) = parentDict[goalState]
        actions.append(action)

    actions.reverse()
    return actions


def nullHeuristic(state, problem=None, goal=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), 0), 0)
    closedSet = set()
    parentDict = {}
    goalState = ()

    while fringe.isEmpty != 1:
        stateToExplore, pathCost = fringe.pop()
        closedSet.add(stateToExplore)
        if problem.isGoalState(stateToExplore):
            goalState = stateToExplore
            break

        successors = problem.getSuccessors(stateToExplore)
        for successor in successors:
            (pos, action, cost) = successor
            if(pos in closedSet and not problem.isGoalState(pos)):
                continue
            h = heuristic(pos, problem)
            fringe.push((pos, cost + pathCost), cost + pathCost + h)

            closedSet.add(pos)
            parentDict[pos] = (stateToExplore, action)

    actions = []
    while goalState!=problem.getStartState():
        (goalState, action) = parentDict[goalState]
        actions.append(action)

    actions.reverse()
    return actions


def biDirectionalSearchMM(problem, heuristic):
    """
    This function will perform A* search in both directions by using Priority Queues
    """
    start = time.time()
    # Priority queues arrange the order so we don't have to compare values later for the 
    # problem state and their respective cost function f(n) = g(n)+h(n)
    frontier1, frontier2 = util.PriorityQueue(), util.PriorityQueue()

    # This dictionary saves the positions have visited as we perform the search 
    position_explored1, position_explored2 = {}, {}
    # The initial states need to be added to the dictionary first.
    position_explored1[problem.getStartState()] = []
    position_explored2[problem.goal] = []

    # Priority queues are used to store states in the fringe along with their respective cost function. 
    # Sorted by the value of f(n) = g(n)+h(n) where g(n)=problem.getCostOfActions() and h(n)=heuristic(state, problem)
    frontier1.push((problem.getStartState()), (heuristic(problem.getStartState(), problem, "goal") + problem.getCostOfActions({})))
    frontier2.push((problem.goal), (heuristic(problem.goal, problem, "start") + problem.getCostOfActions({})))

    # We run both the searches simultaneously while both fringes are not empty.
    while not frontier1.isEmpty() and not frontier2.isEmpty():

        # 'position1' variable stores the state with the lowest cost function first from the agent's direction
        position1 = frontier1.pop()

        # Performs a goal state check
        if problem.isGoalState(position1, position_explored2):
            end = time.time()
            print(end-start)
            return position_explored1[position1] + [direction[x] for x in position_explored2[position1]][::-1]

        # Gets the successor states for the state with lowest cost in frontier1 and stores them in the 'successors' variable
        successors = problem.getSuccessors(position1)

        # Move through the successor states
        for st in successors:  
            if st[0] in position_explored1:
                continue

            # Add the new successor states to the dictionary that stores all the states visited during forward search.
            position_explored1[st[0]] = list(position_explored1[position1]) + [st[1]]
            # Pushing the value of the successor states along with its respective cost g(n)+h(n)
            frontier1.push(st[0], (problem.getCostOfActions(position_explored1[st[0]]) + heuristic(st[0], problem, "goal")))

        # 'position2' variable stores the state with the lowest cost function first in the reverse direction from goal
        position2 = frontier2.pop()

        # Performs a goal state check
        if problem.isGoalState(position2, position_explored1):
            end = time.time()
            print(end-start)
            return position_explored1[position2] + [direction[x] for x in position_explored2[position2]][::-1]
        
        # Gets the successor states from state position2 and stores them in the 'successors' variable
        successors = problem.getSuccessors(position2)

        # Move through the successor states
        for st in successors: 
            if st[0] in position_explored2:
                continue

            # Add the new successor states to the dictionary that stores all the states visited from backward search
            position_explored2[st[0]] = list(position_explored2[position2]) + [st[1]]
            # Pushing the value of the successor states explored while performing backward search along with its respective cost g(n)+h(n)
            frontier2.push(st[0], (problem.getCostOfActions(position_explored2[st[0]]) + heuristic(st[0], problem, "start")))
    
    return []
   
# Abbreviations
bfs = breadthFirstSearch
ucs = uniformCostSearch
dfs = depthFirstSearch
astar = aStarSearch
bd = biDirectionalSearchMM
