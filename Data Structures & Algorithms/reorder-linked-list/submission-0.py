class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Collect all nodes
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        # Use two pointers to re-link
        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            if l == r: break # Handle odd middle node
            nodes[r].next = nodes[l]
            r -= 1
            
        nodes[l].next = None # Terminate the list