def flatten_and_sort(arr):
    
    flattened = [num for sublist in arr for num in sublist]

    return sorted(flattened)

print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))
      
# Answers to the Functional Prompt Questions:
# 1. The solution ensures data immutability by not modifying the original array. Instead, a new array is returned.
# 2. Yes, this solution is a pure function. It always gives the same output for the same input without any side effects.
# 3. No, this solution is not a higher-order function as it doesn't take a function as an argument or return a function.
# 4. Depending on the person's familiarity with different paradigms, some might find the OOP approach or procedural programming easier.
# 5. Functional programming is helpful here because it allows for easy chaining of operations (flatten then sort) and ensures that original data remains unmodified.