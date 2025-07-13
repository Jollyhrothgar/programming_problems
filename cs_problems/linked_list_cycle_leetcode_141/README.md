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

---

## Suggested Solution Analysis

### 1. User's Solution (`solution.py`)
-   **Approach:** This solution uses a hash set (`visited`) to store each node it encounters while traversing the linked list. Before visiting the next node, it checks if that node is already in the `visited` set. If it is, a cycle has been detected, and the function returns `True`. If it reaches the end of the list (`None`), it means there is no cycle, and it returns `False`.
-   **Time Complexity:** `O(n)`, where `n` is the number of nodes in the list. In the worst case (a list with no cycle), it has to visit every node once.
-   **Space Complexity:** `O(n)`. In the worst case (a list with no cycle), the `visited` set will store all `n` nodes, requiring space proportional to the size of the list.

### 2. Optimal Solution (`optimal_solution.py`)
-   **Approach:** This solution implements Floyd's Cycle-Finding Algorithm, also known as the "Tortoise and the Hare" algorithm. It uses two pointers, `slow` and `fast`, both starting at the head. The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps. If there is a cycle, the `fast` pointer will eventually lap the `slow` pointer, and they will meet at the same node. If there is no cycle, the `fast` pointer will reach the end of the list (`None`).
-   **Time Complexity:** `O(n)`. Although the fast pointer moves faster, the total number of steps is still proportional to the number of nodes in the list.
-   **Space Complexity:** `O(1)`. This is the key advantage. The solution only requires two pointers, using constant extra memory regardless of the list size. This meets the problem's challenge condition.

### Trade-Offs
The user's solution is a correct and common way to solve the problem. It is easy to understand but fails the "challenge mode" requirement of using `O(1)` memory. The optimal solution is a classic, more advanced algorithm that is both time-efficient and memory-efficient. It is the standard answer for this type of problem in interviews because it demonstrates knowledge of a clever, space-optimized algorithm.
