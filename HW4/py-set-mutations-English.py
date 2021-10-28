my_input = int(input())
my_set = set(map(int, input().split()))

operation_length = int(input())

for i in range(operation_length):
    operation_name, operation_num = input().split()
    operation_set = set(map(int, input().split()))
    if operation_name == "intersection_update":
        my_set.intersection_update(operation_set)
    elif operation_name == "update":
        my_set.update(operation_set)
    elif operation_name == "symmetric_difference_update":
        my_set.symmetric_difference_update(operation_set)
    elif operation_name == "difference_update":
        my_set.difference_update(operation_set)

print(sum(my_set))
