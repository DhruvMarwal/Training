# s = "racecar"

# def is_palindrome(s):
#     return s == s[::-1]

# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1
#     while left <= right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1
#     flag = False
#     while left <= right:
#         if s[left] != s[right]:
#             flag = False
#         else:
#             flag = True
#         left += 1
#         right -= 1
#     return flag

# print(is_palindrome(s))

#------------------------------------------------------

# a = [1, 2, 3, 4, 5]
# b = [6,7,8,9]

# a = [1, 9, 13, 8, 5]
# b = [6, 17, 8, 9]

# def merge(a, b):
#     merged = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             merged.append(a[i])
#             i += 1
#         else:
#             merged.append(b[j])
#             j += 1
#     while i < len(a):
#         merged.append(a[i])
#         i += 1
#     while j < len(b):
#         merged.append(b[j])
#         j += 1
#     return merged

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left, right)

# print("sorted", merge_sort(merge(a,b)))
# print("sorted", merge(a,b))

#------------------------------------------------------

# s = [1,3,4,6,2,4,3,7,8,6,9]

# def remove_dub(s):
#     for ref in range(len(s)):
#         check = ref + 1
#         while check < len(s):
#             if s[ref] == s[check]:
#                 s.pop(check) 
#             check += 1
#     return s
    
# def remove_dub(s):
#     ref = 0
#     for check in range(1, len(s)):
#         if s[check] not in s[:ref + 1]:
#         # if s[check] != s[ref]:
#             ref += 1
#             s[ref] = s[check]
#     return s[:ref + 1]

# print("Unique List:", remove_dub(s))

#------------------------------------------------------

def max_avg(s,n):    # sliding window
    w = 0
    for i in range(n):
        w += s[i]
    max_s = w
    for i in range(n,len(s)):
        w += s[i] - s[i - n]
        if w > max_s:
            max_s = w
    return max_s/n

# def max_avg(s, k):
#     i = 0
#     j = k
#     mA = sum(s[i:j])
#     while j <= len(s):
#         w = sum(s[i:j])
#         mA = max(mA, w)
#         i += 1
#         j += 1
#     return mA / k

s = [1, 12, -5, -6, 50, 3]
k = 4
print("Max_avg",max_avg(s,k))


    


