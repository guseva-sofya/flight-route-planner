def main() -> None:
    print("hello conda!")

    x: int = sum(3, 5)
    my_func(2)


def my_func(x: int) -> None:
    print(x + 2)


def sum(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    main()
