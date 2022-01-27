# def twoNumberSum(array, targetSum):
#     # Write your code here.
# 	new_list = []
# 	# for num in array:
# 	# 	for i in range(len(array)):
# 	# 		if i is not array.index(num):
#     #             result = num + array[i]
#     #             if result == targetSum:
#     #                 new_list.append(num)
#     #                 new_list.append(array[i])
#     # return new_list
def twoNumberSum(array,targetSum):
    new_list = []
    for num in array:
        for i in range(len(array)):
            index = array.index(num)
            if i is not index:
                result = num + array[i]
                if num not in new_list:
                    if result == targetSum:
                        new_list.append(num)
                        new_list.append(array[i])
    return new_list



print(twoNumberSum([3,5,-4,8,11,1,-1,6],10))