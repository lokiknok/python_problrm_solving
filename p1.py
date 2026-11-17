
# ==========================================
# PYTHON PROBLEM SOLVING PROGRAM
# Author: Lohith
# Description: Menu-driven coding challenges
# ==========================================

def reverse_number(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)


def palindrome_number(n):
    return str(n) == str(n)[::-1]


def armstrong_number(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == n


def prime_number(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def fibonacci(n):
    a, b = 0, 1
    result = []

    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    return result


def second_largest(arr):
    unique = list(set(arr))

    if len(unique) < 2:
        return "Second largest does not exist"

    first = second = float('-inf')

    for num in unique:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num

    return second


def missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(arr)


def character_frequency(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


def two_sum(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        difference = target - num

        if difference in seen:
            return [seen[difference], i]

        seen[num] = i

    return "No pair found"


def longest_consecutive(arr):
    numbers = set(arr)
    longest = 0

    for num in numbers:
        if num - 1 not in numbers:
            current = num
            count = 1

            while current + 1 in numbers:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n========== PYTHON PROBLEM SOLVING ==========")
        print("1. Reverse a Number")
        print("2. Check Palindrome")
        print("3. Check Armstrong Number")
        print("4. Check Prime Number")
        print("5. Fibonacci Series")
        print("6. Find Second Largest")
        print("7. Find Missing Number")
        print("8. Character Frequency")
        print("9. Two Sum Problem")
        print("10. Longest Consecutive Sequence")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":
                n = int(input("Enter number: "))
                print("Reversed Number:", reverse_number(n))

            elif choice == "2":
                n = int(input("Enter number: "))
                print("Palindrome:", palindrome_number(n))

            elif choice == "3":
                n = int(input("Enter number: "))
                print("Armstrong:", armstrong_number(n))

            elif choice == "4":
                n = int(input("Enter number: "))
                print("Prime:", prime_number(n))

            elif choice == "5":
                n = int(input("Enter number of terms: "))
                if n < 0:
                    print("Enter a non-negative number")
                else:
                    print("Fibonacci:", fibonacci(n))

            elif choice == "6":
                arr = list(map(int, input(
                    "Enter array elements: ").split()))
                print("Second Largest:", second_largest(arr))

            elif choice == "7":
                arr = list(map(int, input(
                    "Enter numbers from 1 to N with one missing: "
                ).split()))
                print("Missing Number:", missing_number(arr))

            elif choice == "8":
                text = input("Enter a string: ")
                print("Frequency:", character_frequency(text))

            elif choice == "9":
                arr = list(map(int, input(
                    "Enter array elements: ").split()))
                target = int(input("Enter target: "))
                print("Indices:", two_sum(arr, target))

            elif choice == "10":
                arr = list(map(int, input(
                    "Enter array elements: ").split()))
                print("Longest Consecutive Length:",
                      longest_consecutive(arr))

            elif choice == "0":
                print("Thank you for using the program!")
                break

            else:
                print("Invalid choice! Try again.")

        except ValueError:
            print("Invalid input! Please enter valid values.")


if __name__ == "__main__":
    main()
