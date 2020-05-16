st = input()
print(any(ch.isalnum() for ch in st))
print(any(ch.isalpha() for ch in st))
print(any(ch.isdigit() for ch in st))
print(any(ch.islower() for ch in st))
print(any(ch.isupper() for ch in st))

#                       Any
# Returns true if any of the items is True. It returns False 
# if empty or all are false. Any can be thought of as a sequence 
# of OR operations on the provided iterables.
# It short circuit the execution i.e. stop the execution as soon 
# as the result is known.

# Syntax : any(list of iterables)
