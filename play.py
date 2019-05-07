# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
#
#
#
#
# print("5!= {:,}, 3!= {:,}, 11! = {:,}".format(
#     factorial(5),
#     factorial(3),
#     factorial(11)
# ))
#

def finbonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current  # tuple unpacking
        nums.append(current)

    return nums


print("via lists")
for n in finbonacci(1000):
    print(n, end=', ')

#
# def finbonacci_co(limit):
#     current = 0
#     next = 1
#
#     while True:
#         current, next = next, next + current  # tuple unpacking
#         yield current
#
#
# print("\n via yield")
#
# for n in finbonacci_co(100):
#     if n > 1000:
#         break
#     print(n, end=', ')
