def greet(name: str):
    print(f"hello, {name}")
    print("nice to meet you!")
    username = 'abc'
    password = 'abc'
    api_key = 'abcd'


def main():
    for name in "James", "Subscriber", "other":
        greet(name)


if __name__ == "__main__":
    main()
