def main():
    try:
        text = input()
        print(text.swapcase())
    except EOFError:
        pass

if __name__ == "__main__":
    main()
    