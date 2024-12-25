def function_with_uncommon_error(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return function_with_uncommon_error(n-1) + function_with_uncommon_error(n-2)

# This will work fine for smaller values of n
print(function_with_uncommon_error(5)) # Output: 5

# But for larger values of n, it will cause RecursionError
print(function_with_uncommon_error(100)) # Output: RecursionError: maximum recursion depth exceeded