from typing import List

class AddTwoNums:
    def check_validations(self, l1, l2):
        if not isinstance(l1, list) or not all(isinstance(i, int) for i in l1):
            raise TypeError("Values must be a list of integers")
        if not isinstance(l2, list) or not all(isinstance(i, int) for i in l2):
            raise TypeError("Values must be a list of integers")
 
    def get_add(self, l1: List[int], l2: List[int]):
        self.check_validations(l1, l2)
        # Convert the linked lists into actual integers.
        value1 = int("".join([str(n) for n in reversed(l1)]))
        value2 = int("".join([str(n) for n in reversed(l2)]))
        sum = value1 + value2 # Add the two integers.
        # Convert the sum back into a linked list (reversed order).
        sum_list = list(map(int, str(sum)))
        return sum_list[::-1]

def main():
    print(AddTwoNums().get_add([1,3,4],[1,1,2]))

if __name__ == "__main__":
    main()