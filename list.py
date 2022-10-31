# data type list
shopping_list = []
item = input('Enter item name: ')
# use while loop because we don't know how many time to iterate
# while item is something it will be True
while item:
    shopping_list.append(item)
    item = input('Enter item name: ')
# print list
print(shopping_list)
# print length of list
print(len(shopping_list))
# loop over list printing each item in list
for item in shopping_list:
    print(item)