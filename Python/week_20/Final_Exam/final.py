import re


def main():
    words = []
    with open('dictionary.txt', 'r') as f:
        for line in f:
            words.append(line.strip())

        print(words)
    words.sort()
    print("butterfly" in words)
    print("KEEPS" in words)

if __name__ == '__main__':
    main()


