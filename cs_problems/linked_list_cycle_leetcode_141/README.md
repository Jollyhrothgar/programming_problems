# Question - Linked List Cycle - 141

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

```
( 3 ) --> ( 2 ) --> ( 0 ) --> ( -4 )
            ^                    |
            |____________________|
```

In the above example, we see that the node with the value of -4 links to the node with a value of 2,
which creates a cycle. Cycles can be any length.

Challenge mode: solve with 0(1) constant memory.

# Thinking

- A linked list is a data structure where nodes are connected in one direction. There's a head node
  that stores some data and also stores a reference to another node. A linked list with a cycle must
  end with a cycle - there's no option for branching paths, since that turns the linked list into a
  directed graph, not a linked list.
- A very simple solution is to walk the linked list until we find ourselves at a node that we've
  already visited.

---

## Solution Analysis

### 1. Standard Solution (`solution.py`)
-   **Approach:** This solution uses a hash set to keep track of visited nodes. It iterates through the list, adding each node to the set. If a node is encountered that is already in the set, a cycle is detected.
-   **Time Complexity:** `O(n)` - as we visit each of the n nodes at most once.
-   **Space Complexity:** `O(n)` - as in the worst case, the hash set will store all n nodes.

### 2. Optimal Solution (`optimal_solution.py`)
-   **Approach:** The optimal solution uses the 'Tortoise and Hare' (Floyd's Cycle-Finding) algorithm. It uses two pointers, a slow pointer that moves one step at a time and a fast pointer that moves two steps. If the pointers ever meet, a cycle exists.
-   **Time Complexity:** `O(n)` - Although the fast pointer moves twice as fast, the overall complexity is still proportional to the number of nodes, as the slow pointer will traverse at most `n` nodes.
-   **Space Complexity:** `O(1)` - as it only uses two pointers and requires no extra data structures. This meets the challenge requirement.

### Trade-Offs
The standard solution is intuitive and easy to understand but uses extra memory that scales with the input size. The optimal solution is more clever and uses constant memory, making it far more efficient for very large inputs and fulfilling the problem's challenge condition.
