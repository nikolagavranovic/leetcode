from solution_bubblesort import Solution, ListNode

class Test(object):
    def make_list(self, input):
        if len(input) == 0:
            return
        head = ListNode(input[0], None)
        curr = head
        for i, el in enumerate(input[1:]):  
            curr.next = ListNode(el, None)
            curr = curr.next
        
        return head

    def compare(self, vals, expected):
        s = Solution()
        input = self.make_list(vals)
        expected_output = self.make_list(expected)
        output = s.sortList(input)
        while output != None:
            if expected_output == None:
                return False
            if output.val != expected_output.val:
                return False
            output = output.next
            expected_output = expected_output.next

        if expected_output != None:
            return False
        else:
            return True


if __name__ == '__main__':

    # test case one
    vals = [4,2,1,3]
    expected = [1,2,3,4]
    t = Test()
    if t.compare(vals, expected):
        print("Solution for test 1 is correct!")


    vals = [-1,5,3,4,0]
    expected = [-1,0,3,4,5]
    if t.compare(vals, expected):
        print("Solution for test 2 is correct!")


