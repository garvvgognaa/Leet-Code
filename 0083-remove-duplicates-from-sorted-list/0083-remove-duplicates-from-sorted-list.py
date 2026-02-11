class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Skip duplicate
                current.next = current.next.next
            else:
                # Move forward
                current = current.next
        
        return head
