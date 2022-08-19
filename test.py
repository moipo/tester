# enumeration , sets, dictionaries, lambda, map, zip , рекурсия, iter, стандартные библиотеки,  LT
# pop, arr[:], s[::-1], s[1:-1], алгоритмы, декораторы, перегрузка, 100 способов использования генераторов
# вложенный генератор, arr.sort(key = func)   Use unusual contsructions: "It is %s%s" % ("John","Cena")
# !help(), dir() НЕВЕРНО: arr[1:len(arr)-1], ВЕРНО: arr[1:-1], dict.items(), sorted( key = (str.lower,2,3)) картеж значений
# проходка по вложенному файлам через рекурсию (применяется в каталогах)
# асинхронка библиотечные структуры данных (связный список и т.д.) алгоритмы ООП модуль collections
# https://habr.com/ru/company/vk/blog/506824/      yield(next)10
# yield (с next, иначе вернет генератор  ) - спродуцировать / уступить           codeforces, leetcode, asp
# alg: binary search , НОД, devisors(alg), recursion, linked lists
# отладчик , кст,н    try/catch        all, any(condition1, condition2, ...)
# Vis, all, any, rjust, декораторы, замыкания, in , not in
# использования(counter) iter, enum, decorators,  recursion, try/catch
# mystr.strip("482 3") - раздеть справа по этим символам.    mystr.zfill(20) - Дополняет до нулей длины
# области видимости: локальная, нелокальная, глобальная.
# T S     Counter, Json, openpyxl,   codewars collections, mystr.strip()
# генераторы словарей, генераторы множеств, defaultdict, deque, namedtuple
# Codeforces , Leetcode, file input output, Pandas, pickle , requests, reduce
#
# ToDo: Accept dots, dashes and spaces, return human-readable message
from collections import Counter
from collections import defaultdict
# from functools import reduce
# arr = [4,2,64,85,7]
# print(reduce(lambda x,y: x*y, arr)) "425"
from collections import deque


a = "hello"
print(str(a))
print(repr(a))
# print(eval(str(a)))
print(eval(repr(a)))



# mystr = """
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
#  aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
#   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
# """
#
# 27. Write a Python program to remove duplicate words from a given string use collections module.
# MORSE_CODE = { 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.',
#                     'F':'..-.', 'G':'--.', 'H':'....',
#                     'I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--', 'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                     '1':'.----', '2':'..---', '3':'...--',
#                     '4':'....-', '5':'.....', '6':'-....',
#                     '7':'--...', '8':'---..', '9':'----.',
#                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                     '?':'..--..', '/':'-..-.', '-':'-....-',
#                     '(':'-.--.', ')':'-.--.-'}
#
#
# [int(i) for i in list(str(123))]
# print(5//10)

# def decode_morse(morse_code):
#     # ToDo: Accept dots, dashes and spaces, return human-readable message
# #     print(MORSE_CODE)
# #     return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
#     res = ''
#     for word in morse_code.split('   '):
#         res += ''.join([MORSE_CODE[letter] for letter in word.split(' ')]) + ' '
#     return res[:-1]
#
# print(decode_morse('.... . -.--   .--- ..- -.. .'))

# class Solution(object):
#     def get_indexes(self,thestr,letter):
#         index = 0
#         listofindexes = []
#         while True:
#             index = thestr.find(letter, index)
#             if index == -1: break
#             else:
#                 listofindexes.append(index)
#                 index += 1
#         return tuple(listofindexes)
#
#     def isIsomorphic(self, s, t):
#         if len(s) == len(t):
#             myset = set()
#             for i in range(len(t)):
#                 if i not in myset:
#                     a = self.get_indexes(s,s[i])
#                     b = self.get_indexes(t,t[i])
#                     myset.update(a,b)
#                 if a!=b:
#                     return False
#             return True
#         return False
#
#
# obj = Solution()
# print(obj.isIsomorphic('badc','baba'))

















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