import re
import glob, os


cwd = os.getcwd()

# os.chdir(cwd)
# for file in glob.glob("*.srt"):
#     print(file)

def main():
    # read file line by line
    for file in glob.glob("*.srt"):
        file = open(file, "r")
        lines = print(file.read())
        file.close()

        text = ''
        
        for line in lines:
            if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
                text += ' ' + line.rstrip('\n')
            text = text.lstrip()
        
        sys.stdout = open(file+".txt", "w")
        print(text)
        sys.stdout.close()


main()