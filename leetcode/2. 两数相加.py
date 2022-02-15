# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        numList1 = []
        numList2 = []
        #先把链表的val都分别放到两个list里
        while l1:
            numList1.append(l1.val)
            l1 = l1.next
        while l2:
            numList2.append(l2.val)
            l2 = l2.next
        #反转list，转换为int直接相加，再把int转换为str
        numList1 = [str(x) for x in numList1][::-1]
        numList2 = [str(x) for x in numList2][::-1]
        numList1 = "".join(numList1)
        numList2 = "".join(numList2)
        sumList = str(int(numList1) + int(numList2))
        #生成最后一个节点
        ans = ListNode(int(sumList[0]), None)
        #如果是个位数，直接return答案，如果是两位数以上，把后续链表逐个链接
        if len(sumList) >= 2:
            for i in range(1,len(sumList)):
                tmp = ListNode(int(sumList[i]),ans)
                ans = tmp
            return ans
        else:
            return ans