# print factorial numbers

def factor(n):
    if n == 0 or n == 0:
        return 1
    return n * factor(n - 1)
nums = int(input("Enter what you want to find the factorial of: "))
print(f"your factorial is {factor(nums)}")