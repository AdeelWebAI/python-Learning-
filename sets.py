# s = {1,3,5,6,77,7}
# print(s)

# python sets don't folow the order of the elements

# info = {"align","order","size","doubles"}
# print(info)
# s = set()
# empty = print(type (s))
# print(empty)
# for value in s:
#     print(value)

s1 = {1,2,3,4}
s2 = {4,5,6,7}
# print(s1, s2)
# print(s1.union(s2))
# s3 = s1.update(s2)
# print(s1)
# s3 = s1.intersection(s2)

s3 = s1.intersection_update(s2)

print(s3)
