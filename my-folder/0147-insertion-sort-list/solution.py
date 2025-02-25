class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # Dummy node to hold the sorted list
        current = head  # Pointer to traverse the original list

        while current:  
            prev = dummy  # Start from the dummy node each time

            # Find the correct insertion point in the sorted list
            while prev.next and prev.next.val < current.val:
                prev = prev.next  # Move forward in sorted list
            
            # Insert the current node into the sorted list
            next_node = current.next  # Save reference to the next node
            current.next = prev.next  # Connect to the sorted list
            prev.next = current  # Place the node in the sorted list

            # Move to the next node in the original list
            current = next_node  

        return dummy.next  # Skip the dummy node and return the sorted list
