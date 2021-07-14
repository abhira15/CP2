two_vertex = [[2, 1], [2, 2], [3, 4], [3, 1], [2, 4]]

# counterList = []
# for smallerList in two_vertex:
#     for index, number in enumerate(smallerList):
#         if number in counterList:
#             smallerList[index] = smallerList[index]-1
#         else:
#             smallerList[index] = smallerList[index]-1
#             counterList.append(number)
# print(two_vertex)


for smallerList in two_vertex:
    for index, number in enumerate(smallerList):
        smallerList[index] = smallerList[index]-1
print(two_vertex)        


# counterList = []
# 
# for index, eachList in enumerate(two_vertex):
#     if eachList in counterList:
#         two_vertex[index] = counterList.index(eachList)
#     else:
#         two_vertex[index] = len(counterList)
#         counterList.append(eachList)
# 
# print(two_vertex)

# counter = []
# 
# for smallerList in two_vertex:
#     for number in smallerList:
#         if number in CounterList:
            