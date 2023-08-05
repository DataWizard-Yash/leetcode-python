class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        dummy = ListNode(0)
        current = head
        new_list = dummy

        while current:
            new_list.next = ListNode(current.val)
            new_list = new_list.next
            if current.next:
                gcd_val = self.gcd(current.val, current.next.val)
                new_list.next = ListNode(gcd_val)
                new_list = new_list.next
            current = current.next

        return dummy.next

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example 1
head1 = ListNode(18)
head1.next = ListNode(6)
head1.next.next = ListNode(10)
head1.next.next.next = ListNode(3)

s = Solution()
result1 = s.insertGreatestCommonDivisors(head1)
print_linked_list(result1)  # Output: 18 -> 6 -> 6 -> 2 -> 10 -> 1 -> 3 -> None
