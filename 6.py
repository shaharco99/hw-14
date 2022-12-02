from time import sleep
while True:
    sleep(5)
    file.close()
    try:
        file = open("url.txt")
        read = file.readlines()
        for line in read:
            print(line)
    except FileNotFoundError:
        print("<url> is dead")
        break