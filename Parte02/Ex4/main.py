import readchar

def readAllUpTo(stop_char):
    print("I will now read all chars until you press X")
    c = -1
    while c != 'X':
        c = readchar.readchar()
        print(c)

def printAllCharsUpTo(stop_char):
    for i in range(32, ord(stop_char)):
        print(chr(i))

def countNumbersUpTo(stop_char):
    inputs = []
    numbers_list = []
    others_dict = {}

    while True:
        c = readchar.readchar()
        print(c)

        if c == "X":
            break

        inputs.append(c)
        if c.isnumeric():
            numbers_list.append(int(c))
        else:
            others_dict[len(others_dict) + 1] = c        

    print(numbers_list)
    print(others_dict)

    numbers_list.sort()
    print("Sorted: {}".format(numbers_list))
    print("List compreension: {}".format([i for i in inputs if i.isnumeric()]))
    
    total_numbers = len(numbers_list)
    total_others = len(others_dict)      

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')

def main():
    print("Choose you character!:")
    c = readchar.readchar()
    printAllCharsUpTo(c)
    readAllUpTo(c)
    countNumbersUpTo(c)

if __name__ == '__main__':
    main()