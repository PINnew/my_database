def process_numbers(numbers):
    """Преобразует список чисел в строку, разделенную запятыми."""
    return ",".join(map(str, numbers))

if __name__ == '__main__':
    numbers = [541, 3532, 65434, 66535]
    result = process_numbers(numbers)
    print(result)  # Выведет: "541,3532,65434,66535"
