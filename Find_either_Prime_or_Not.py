
# n        = int(input('Enter A Number: '))
# values   = [ i for i in range(2, n+1) ] # List Comprehension: Similar to Mathematical Set Builder Notation
# bool_map = [ True for i in range(2, n+1) ]

# for i in range(len(values)):
#     curr_num = values[i]

#     for j in range(i+1, len(values)):
#         if bool_map[j] and values[j] % curr_num == 0:
#                 bool_map[j] = False

# res = []
# for i in range(len(values)):
#     if bool_map[i]:
#         res.append(values[i])

# print("yes" if n in res else "no" )


# n        = int(input('Enter A Number: '))
# values   = [ i for i in range(2, n+1) ] # List Comprehension: Similar to Mathematical Set Builder Notation
# bool_map = [ True for i in range(2, n+1) ]
# is_valid = True

# for i in range(len(values)):
#     curr_num = values[i]

#     for j in range(i+1, len(values)):
#         if bool_map[j] and values[j] % curr_num == 0:
#                 bool_map[j] = False
#                 if values[j] == n:
#                     is_valid = False
#                     break

# print("yes" if is_valid else "no" )


n        = int(input('Enter A Number: '))
is_valid = True

for i in range(2, n):
    is_valid = not n % i == 0

print("yes, it's a prime" if is_valid else "no, it's not a prime" )

