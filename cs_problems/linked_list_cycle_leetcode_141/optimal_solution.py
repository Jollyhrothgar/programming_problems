"""Solution linked list cycles problem"""

from lib.linked_list_tools import ListNode
from typing import Optional


def has_cycle(head: Optional[ListNode]) -> bool:
  # The runners start at the same line.
  slow = head
  fast = head

  # The race continues as long as the fast runner can take two steps
  # without falling off the end of the track (reaching None).
  while fast and fast.next:
    # The slow runner takes one step.
    slow = slow.next
    # The fast runner takes two steps.
    fast = fast.next.next

    # Check if they are on the same node.
    if slow == fast:
      # They met! It must be a cycle.
      return True
      
  # If the loop finishes, the fast runner reached the end. No cycle.
  return False