from functools import reduce
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
list4 = [10,11,12]
list_all = [list1,list2,list3,list4]
print(list_all)
#[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
new_list = reduce(lambda x,y:x+y, list_all)
print(new_list)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]