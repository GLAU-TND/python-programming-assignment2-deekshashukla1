'''
This problem was asked by Twitter.

Given a list of numbers, create an program that arranges
them in order to form the largest possible integer.
For example,
given [10, 7, 76, 415], you should print 77641510

sample input
[10, 7, 76, 415]
sample output
77641510
'''

lst = eval(input())
# string list
lst_new = list(map(str, lst))

# lst_new.sort(reverse=True)
# print(lst_new)
lst_new.sort(key=len)
print(lst_new)

lst_new.sort(reverse=True, key=lambda x:x[0])
print(lst_new)

out = ''.join(lst_new)
print(out)


