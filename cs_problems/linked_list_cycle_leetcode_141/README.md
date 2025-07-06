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

# Solution

The solution uses the approach of tracking visited nodes. The optimal solution
implements an interesting "fast walker vs slow walker" approach which is also
O(1) in memory. This is important because based on the topology of linked lists
themselves, we're guaranteed that the "fast walker" will eventually lap the slow
walker, thus telling us that there's a cycle. In the case where there IS no
cycle, the fast walker gets to the end of the list quickly which tells us that
tehre IS NO cycle.
