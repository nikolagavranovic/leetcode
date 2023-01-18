# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]




# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        end_of_odd = head
        if head.next != None:
            begining_of_even = head.next
        i = 1
        prev = head
        curr = head.next
        while curr != None:
            i += 1
            if i % 2 == 1:
                node = self.delete_node(prev, curr)
                self.insert_between(node, end_of_odd, begining_of_even)
                end_of_odd = end_of_odd.next
                curr = prev # because current node is now moved in the end of odd list, this sets
                # current node to previous and in the next lines of code initial node that was
                # succesor of current node will become current. Otherwise, current node would be
                # beggining of even list.
            
            prev = curr
            curr = curr.next
        return head

    def get_list(self, head):
        retVal = []
        curr = head
        while curr != None:
            retVal.append(curr.val)
            curr = curr.next
        return retVal


    def delete_node(self, prev, curr):
        if curr.next == None:
            prev.next = None
            return curr
        
        prev.next = curr.next
        curr.next = None
        return curr
    
    def insert_between(self, node, prev, succ):
        temp = prev.next
        prev.next = node
        node.next = succ


