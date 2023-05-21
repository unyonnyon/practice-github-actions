def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def times(a: int, b: int) -> int:
    return a * b

def double(a: int) -> int:
    """Return the double of a.
    """
    return times(a, 2)

if __name__ == "__main__":
    a = 3
    b = 4
    print(add(a, b), sub(a, b))
    print("double of", a, "is", double(a))
