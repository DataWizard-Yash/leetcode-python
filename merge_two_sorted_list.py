class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1: return list2
        if not list2: return list1

        current = dummy = ListNode(0)

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2
        d = dummy.next
        return dummy.next


sol = Solution()
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# Test cases
list1 = list_to_linked_list([1, 2, 4])
list2 = list_to_linked_list([1, 3, 4])
merged_list = sol.mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]

list1 = list_to_linked_list([])
list2 = list_to_linked_list([])
merged_list = sol.mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_list))  # Output: []

list1 = list_to_linked_list([])
list2 = list_to_linked_list([0])
merged_list = sol.mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_list))  # Output: [0]
