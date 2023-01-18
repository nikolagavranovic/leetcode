
# Given the head of a linked list, return the list after sorting it in ascending order.

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Input: head = []
# Output: []

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        if head.next == None:
            return head

        length = self.get_len(head) 
        for i in range(length):
            prev, curr, succ = self.reinit_nodes(head)

            for j in range(0, length - i - 1):

                if succ.val < curr.val:
                    # swap elements
                    node, head = self.delete_node(head, prev, curr)
                    self.insert_node_after(succ, node)
                    # make updates for curr node and succ node
                    curr = succ
                    succ = node               

                prev = curr
                curr = succ
                succ = succ.next

        return head

    def get_len(self, head):
        i = 0
        while head != None:
            i += 1
            head = head.next
        return i

    def reinit_nodes(self, head):
        return None, head, head.next

    def insert_node_after(self, node, node_to_insert):
        temp = node.next
        node.next = node_to_insert
        node_to_insert.next = temp

    def delete_node(self, head, prev, node_to_delete):
        if prev == None:
            head = node_to_delete.next
            node_to_delete.next = None
            return node_to_delete, head
        if node_to_delete.next == None:
            prev.next = None
            return node_to_delete, head

        prev.next = node_to_delete.next
        node_to_delete.next = None
        return node_to_delete, head


    def get_list(self, head):
        retVal = []
        curr = head
        while curr != None:
            retVal.append(curr.val)
            curr = curr.next
        return retVal


