
arr=  [3,45,6,5,6,4,3,7,2,3,4,6,2,2]

length =len(arr)
i = 0
while i < length:
    arr.pop()
    i+=1
    length -=1
    print(arr[i])

text = "asdf"
text.isu
[text[i+1].upper() if text[i] =='-' else text[i] for i in range(len(text))]




























# success
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#     def __str__(self):
#         return str(self.val)
#
#
#
# arr = deque([4,5,6,3,4,4,2,6,12,3,4,51,6,9])
#
#
#
#
# #1) поместить всё в список
# #2) считать всё из списка.
#
# arr_of_nodes = []
# def create_linked_list(arr:deque):
#     if len(arr) == 1:
#         return ListNode()
#     new_node = ListNode(arr.popleft(), create_linked_list(arr))
#     arr_of_nodes.append(new_node)
#     return new_node
#
# create_linked_list(arr)
#
# first_node = arr_of_nodes[0]
# # print(arr_of_nodes)
# arr_of_nodes.reverse()
# for node in arr_of_nodes:
#     print(node.val, node.next.val)






























# def show_linked_list(node:ListNode):
#     print(show_linked_list(node.next))
#
#
# show_linked_list(first_node)


    # if len(arr) == 1:
    #     return



# create_linked_list()
# print(arr_of_nodes)
#
#
#









# head_node = ListNode()
#
#
#
# arr_of_nodes = []
#
# def create_linkedlist(arr):
#     if len(arr) == 1
#     return ListNode(arr[-1])
#         arr.pop()
#     arr_of_nodes
#     return create_linkedlist(,create_linkedlist())
#
#
# for i in arr:
#     head_node.next = ListNode(arr[0],ListNode(arr[1]))








#
# class Solution(object):
#
#     def get_values(self, list1, arr):
#         while list1.next != None:
#             arr.append(list1.val)
#             list1 = list1.next
#         arr.append(list1.val)
#
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         arr = []
#         Solution.get_values(self, list1, arr)
#         Solution.get_values(self, list2, arr)
#         if not arr: return ListNode(0)
#
#         arr.sort()
#         arr.append(None)  # не подходит
#         arr_of_listnodes
#         for i in range(len(arr) - 1):
#             node = ListNode(arr[i], ListNode(arr[i + 1], ListNode()))
#             print(node.val)
#         return ListNode(arr[0], ListNode(arr[1]))
#
#
# elem3 = ListNode(24, None)
# elem2 = ListNode(53, elem3)
# elem1 = ListNode(11, elem2)
#
# elem3x = ListNode(32, None)
# elem2x = ListNode(11, elem3)
# elem1x = ListNode(17, elem2)
#
# solution = Solution()
# leading_node = solution.mergeTwoLists(elem1x,elem1)
# print("\n\n\n")
# while leading_node.next != None:
#     print(leading_node)
#     leading_node = leading_node.next
# print(leading_node)