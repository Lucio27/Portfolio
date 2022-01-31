from collections import Counter

def solution(array):
    return max(tuple(Counter(array).values()))

Given_A = ["Cardiology","Orthopaedics","Neurology","Cardiology","Orthopaedics","Cardiology"]
# Given_A = ["Oncology","Gynaecology","Orthopaedics","Oncology","Gynaecology","Orthopaedics"]
# Given_A = ["Neutology","Cardiology","Oncology"]
print(solution(Given_A))



    



