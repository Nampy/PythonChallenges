if __name__ == '__main__':
    char_strings = ""
    for line in open("challenge3SpecialChar.txt"):
        print (char_strings.count("@"))
        char_strings += line
    print(min(char_strings))