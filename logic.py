def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    return text == text[::-1]


def fibonacci(n):
    if n < 0:
        raise ValueError("zła liczba")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1

    for _ in range(n - 1):
        a, b = b, a + b

    return b


def count_vowels(text):
    vowels = "aeiouyąęó"
    count = 0

    for letter in text.lower():
        if letter in vowels:
            count += 1

    return count


def calculate_discount(price, discount):
    if discount < 0 or discount > 1:
        raise ValueError("zły rabat")

    return price - price * discount


def flatten_list(data):
    result = []

    for element in data:
        if isinstance(element, list):
            result = result + flatten_list(element)
        else:
            result.append(element)

    return result


def word_frequencies(text):
    text = text.lower()

    for znak in ".,!?":
        text = text.replace(znak, "")

    words = text.split()
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
