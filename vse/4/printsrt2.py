import re

def main():
    # read file line by line
    file = open( "/Users/jzhang/git-repos/hdclass/vse/4/02-1 慧灯禅修课24 加行的修法-菩提心1.srt", "r")
    lines = file.readlines()
    file.close()

    text = ''
    for line in lines:
        if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
            text += ' ' + line.rstrip('\n')
        text = text.lstrip()
    print(text)

main()