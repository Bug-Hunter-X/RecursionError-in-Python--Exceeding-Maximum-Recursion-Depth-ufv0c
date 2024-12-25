def function_with_uncommon_error_solution(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# This will work for larger values of n
print(function_with_uncommon_error_solution(5))  # Output: 5
print(function_with_uncommon_error_solution(100)) # Output: 354224848179261915075