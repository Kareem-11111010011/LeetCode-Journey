# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = ListNode()
        head = sorted_list

        while True:
            if list1 is None and list2 is None:
                return head.next
            if list1 is None:
                while list2 is not None:
                    sorted_list.next = list2
                    sorted_list = sorted_list.next
                    list2 = list2.next
                return head.next
            if list2 is None:
                while list1 is not None:
                    sorted_list.next = list1
                    sorted_list = sorted_list.next
                    list1 = list1.next
                return head.next
            if list1.val < list2.val:
                sorted_list.next = list1
                sorted_list = sorted_list.next
                list1 = list1.next
            else:
                sorted_list.next = list2
                sorted_list = sorted_list.next
                list2 = list2.next
