#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        a, b = l1, l2
        arr1 = []
        arr2 = []

        while a:
            arr1.append(a.val)
            a = a.next

        while b:
            arr2.append(b.val)
            b = b.next

        arr1.reverse()
        arr2.reverse()

        inta = int("".join(str(x) for x in arr1))
        intb = int("".join(str(x) for x in arr2))

        c = list(str(inta + intb))

        head = l3 = ListNode(c.pop())

        c.reverse()

        for i in c:
            l3.next = ListNode(i)
            l3 = l3.next

        return head


if __name__ == '__main__':
    s = Solution();
    l1 = ListNode(2)
    l1.next = ListNode(4,3)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6,4)
    l2.next.next = ListNode(4)

    l3 = s.addTwoNumbers(l1,l2)
    print(l3.val, l3.next.val, l3.next.next.val)
