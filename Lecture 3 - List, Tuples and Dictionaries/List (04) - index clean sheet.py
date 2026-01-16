students = ["Ali", "Sara", "John", "Maya", "Tom"]

# ✅ Basic Indexing
# students[0] → "Ali" (first element, index starts at 0)
# students[1] → "Sara" (second element)
# students[2] → "John" (third element)

# ✅ Negative Indexing (from the end)
# students[-1] → "Tom" (last element)
# students[-2] → "Maya" (second to last)

# ✅ Printing the Whole List
# print(students) → ['Ali', 'Sara', 'John', 'Maya', 'Tom']

# ✅ Slicing (sub-lists)
# students[0:3] → ['Ali', 'Sara', 'John'] (from index 0 up to, but not including, 3) 
# students[:2] → ['Ali', 'Sara'] (default start = 0)
# students[2:] → ['John', 'Maya', 'Tom'] (default end = last)
# students[:] → whole list (same as print(students))

# 👉 [0:3] means process starts from index [0] until index [2]. INDEX [3] is not included.
# 👉 [:2] means process starts from default start [0] until index [1]. INDEX [2] is not included.
# 👉 [2:] means process starts from index [2] until default end [last item].
# 👉 [:] means process starts from default start [0] until default end [last item].

# ✅ Step (skip values)
# students[::2] → ['Ali', 'John', 'Tom'] (every 2nd element)
# students[::-1] → ['Tom', 'Maya', 'John', 'Sara', 'Ali'] (reversed list)

# ✅ Rule of thumb:
# list[i] → 1 element
# list[start:end] → a slice
# list[start:end:step] → slice with skipping 👉 Default start until default end but skip between n elements/item.