def binary_search(arr, target):

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

try:
    input_sequence = input("Введите числа через пробел: ")
    numbers = [int(x) for x in input_sequence.split()]
    user_number = int(input("Введите любое число: "))

    if not all(num <= user_number for num in numbers):
        print("Error: Некоторые числа не соответствуют условию.")

    insertion_sort(numbers)
    position = binary_search(numbers, user_number)

    print(f"Sort: {numbers}")
    print(f"Позиция элемента согласно условию: {position}")

except ValueError:
    print("Error: Введите корректные числа.")



