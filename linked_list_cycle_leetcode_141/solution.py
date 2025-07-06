"""Solution linked list cycles problem"""

from lib.linked_list_tools import ListNode
from typing import Optional

def has_cycle(head: Optional[ListNode])-> bool:
  visited = set()
  
  if head == None:
    return False

  visited.add(head)

  while True:
    if head.next in visited:
      return True
    else:
      head = head.next
      visited.add(head)
    if head is None:
      return False
    if head.next == None:
      return False

