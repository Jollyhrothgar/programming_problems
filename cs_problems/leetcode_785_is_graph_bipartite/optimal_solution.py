import collections

class Solution:
  def isBipartite(self, graph: list[list[int]]) -> bool:
    # 1. This dictionary will store the "color" for each node we visit.
    # We can use 1 and -1 to represent the two different colors.
    colors = {}

    # 2. We loop through every node in the graph. This is necessary
    # because the graph might have disconnected components.
    for i in range(len(graph)):

      # 3. If the current node `i` hasn't been colored yet, it means
      # we've found a new, unvisited part of the graph.
      if i not in colors:
        
        # 4. Start a new traversal (BFS) for this component.
        # We create a queue and add our starting node `i` to it.
        queue = collections.deque([i])
        # We assign it the first color (1).
        colors[i] = 1

        # 5. Process the queue until it's empty.
        while queue:
          node = queue.popleft() # Get the next node to check.

          # 6. Look at all of its neighbors.
          for neighbor in graph[node]:
            
            # 7. If the neighbor hasn't been colored yet...
            if neighbor not in colors:
              # ...color it with the opposite color of the current node.
              colors[neighbor] = -colors[node]
              # Add it to the queue to visit its neighbors later.
              queue.append(neighbor)
              
            # 8. If the neighbor IS already colored, check for a conflict.
            # A conflict happens if the neighbor has the same color.
            elif colors[neighbor] == colors[node]:
              return False # This means the graph is not bipartite.
    
    # 9. If the loops complete without any conflicts, the graph is bipartite.
    return True
