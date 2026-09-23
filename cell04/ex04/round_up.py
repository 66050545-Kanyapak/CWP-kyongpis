import math

def main():
    try:
        user_input = input("Give me a number: ")
        num = float(user_input)
        print(math.ceil(num))
    except ValueError:
        pass

if __name__ == "__main__":
    main()