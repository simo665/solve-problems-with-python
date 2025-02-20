from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNums:
    def check_validations(self, l1, l2):
        if not isinstance(l1, list) or not all(isinstance(i, int) for i in l1):
            raise TypeError("Values must be a list of integers")
        if not isinstance(l2, list) or not all(isinstance(i, int) for i in l2):
            raise TypeError("Values must be a list of integers")

    def list_to_linked_list(self, lst: List[int]):
        listnode = ListNode()
        current = listnode
        for n in lst:
            current.next = ListNode(n)
            current = current.next
        return self.linked_list_to_list(listnode.next)
    
    def linked_list_to_list(self, node: ListNode) -> List[int]:
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    
    def get_add(self, l1: List[int], l2: List[int]):
        self.check_validations(l1, l2)
        # Convert the linked lists into actual integers.
        value1 = int("".join([str(n) for n in reversed(l1)]))
        value2 = int("".join([str(n) for n in reversed(l2)]))
        sum = value1 + value2 # Add the two integers.
        # Convert the sum back into a linked list (reversed order).
        sum_list = list(map(int, str(sum)))
        return self.list_to_linked_list(sum_list)

def main():
    print(AddTwoNums().get_add([1,3,4],[1,1,2]))

if __name__ == "__main__":
    main()