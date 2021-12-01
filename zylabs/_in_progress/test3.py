# def selection_sort_descend_trace(numbers):
#
#     i=len(numbers)
#
#     print('Output: ')
#
#     for num in range(0,i-1):# traversing from 0 to N-2, total N-1 iterations
#
#         val=numbers[num]
#
#         start=num+1
#
#         end=i
#
#         t=0
#
#         for j in range(start,end):
#
#             if(val<numbers[j]):
#
#                 remember=j
#
#                 val=numbers[j]
#
#                 t=1
#
#             if(t==1):# swaping onlf if greater number is available
#
#                 temp=numbers[num]
#
#                 numbers[num]=val
#
#                 numbers[remember]=temp
#
#     for p in range(i):# printing
#
#         print(numbers[p],end=' ')
#
#         print("\n")
#
# if __name__ == "__main__":
#
#     print("Enter the integers separated by space: ")
#
#     numbers=[int(x) for x in input().split(' ')]
#
#     selection_sort_descend_trace(numbers)

def selection_sort_descend_trace(a):
    i = 0
    while i<len(a):
        y = a
        #smallest element in the sublist
        x = max(a[i:])
        #index of smallest element
        index = a.index(x)
        #swapping
        a[i],a[index] = a[index],a[i]
        y = (a[i],a[index])
        # for i in y:
        #     if i in a:
        #         z = a.remove(i)
        for i in y:
            print(i, end=' ')
        for i in a:
            # if a.index(i) > 2:
            print(i, end=' ')
        i=i+1
    print(a)
    for i in a:
        # if a.index(i) > 2:
        print(i, end=' ')

if __name__ == "__main__":

    print("Enter the integers separated by space: ")

    numbers=[int(x) for x in input().split(' ')]

    selection_sort_descend_trace(numbers)
#FIXME TESTING STUFF HERE FOR 16.10