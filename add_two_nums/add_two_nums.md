# Add Two Numbers 

so i hvave to add two numbers represented as linked lists, where the digits are stored in reverse order. Each node in the linked list represents a single digit.

#### For more understanding
Each number is stored in reverse order in the linked list. This means:
[2,4,3] represents 342 (not 243).
[5,6,4] represents 465 (not 564).
When we add them: 342 + 465 = 807.

The result [7,0,8] represents 807, stored in reverse order.

#### Steps to Solve the Problem
1. Convert the linked lists into actual integers.
2. Add the two integers.
3. Convert the sum back into a linked list (reversed order).
4. Return the new linked list.