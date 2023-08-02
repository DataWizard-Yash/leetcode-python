class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next

# Helper function to convert list to linked list
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test the Solution class with input lists as arguments
sol = Solution()
list1 = list_to_linked_list([2, 4, 3])
list2 = list_to_linked_list([5, 6, 4])
result = sol.addTwoNumbers(list1, list2)
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst
print(linked_list_to_list(result))