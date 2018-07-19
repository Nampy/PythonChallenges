import urllib.request
import re

if __name__ == '__main__':
    file = (urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode())
    print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", file)))
