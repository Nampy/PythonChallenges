import collections

if __name__ == '__main__':
    char_strings = ""
    for line in open("challenge3SpecialChar.txt"):
        char_strings += line.strip("\n")
    list_occ = collections.Counter(char_strings).most_common()
    print(collections.Counter(char_strings).most_common())