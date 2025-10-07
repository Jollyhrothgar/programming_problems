import sys
import re
from typing import List
import collections

class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    colors = {}

    for i in range(len(graph)):
      if i not in colors:
        colors[i] = 1

        # BFS
        deque = collections.deque([i]) # Add the first node to the deque.

        while deque:
          node = deque.popleft()
          for neighbor in graph[node]:
            if neighbor not in colors:
              colors[neighbor] = colors[node]*-1
              deque.append(neighbor)
            elif colors[neighbor] == colors[node]:
              return False

    return True


        

def main():
  sol = Solution()
  try:
    user_arg = sys.argv[1]
  except IndexError:
    print(f"Malformed input. Please use invocation with an adjacency list: {sys.argv[0]} [[..], ... [..]]")
    return 0
  if re.match(r'^\[((\[\d+(,\d+)*\])(,\[\d+(,\d+)*\])*)?\]$', user_arg):
    graph = eval(user_arg)
    print(graph)
    result = sol.isBipartite(graph)
    print(result)
  else:
    raise ValueError(f"{user_arg} does not match a supported adjacency list format")
  return 1


if __name__ == '__main__':
  main()
