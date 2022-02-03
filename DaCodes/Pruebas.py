# %% Task 1 
'''
Write a function "solution()" that, gien strings "name" and "surname" and integer "age", returns a string
composed of the first two letters fromn each of "name" and "surname" followed by "age". For example,
given name = "John", surname = "Firelord " and age = 8, your function should return "JoFi8".

You can assume the length of "name" and "surname" is between 2 and 20, and "age" is between 1 and 200.


'''
def solution(name: str,suername: str,age: int):
   return '%s%s%d' % (name[:2], suername[:2], age)

print(solution('John','Firelord',8))

# %% Task 2
'''
Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns the sum of all integers which are multiples 
of 4.

For example, given array A as follows:

    [-6, -91, 1011, -100, 84, -22, 0, 1, 473]

the function should return -16

Assume that:
    * N is an integer within the range [1..1,000]
    * each element of array A is an integer within the range [-10,000..10,000]
    * there is at least one element in array A which satisfies the condition in the task statement.

In your solution, focus on correctness. The performance of your solution will not be focus of the
assessment.
'''
def solution(A):
    return sum([num for num in A if num % 4 == 0])

print(solution([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))

# %% Task 3
'''
A hospital has five departments: Cardiology, Neurology, Orthopaedics, Gynaecology and Oncology. 
There are N patients numbered from 0 to N-1, and the K-th of them is in department represented by a 
string A[K].

Write a function:

    def solution(A)

that, given an array A consisting of N strings, returns the maximum number of patients 
in one department.

Examples: 
1. Given A = ["Cardiology","Orthopaedics","Neurology","Cardiology","Orthopaedics","Cardiology"]
the function should return 3. The department of Cardiology is occupied by three patients.

2. Given A = ["Oncology", "Gynaecology", "Orthopaedics", "Oncology", "Gynaecology", "Orthopaedics"]
the function should return 2.

3. Given A = ["Neurology","Cardiology","Oncology"], the function should return 1

Write a efficient algorithm for the following assumptions:

    * N is an integer within the range [1..100,000]
    * each element of array A is an integer that can have one  of the following values: Cardiology,
    Neurology, Orthopaedics, Gynaecology, Oncology.

'''
from collections import Counter

def solution(array):
    return max(tuple(Counter(array).values()))
