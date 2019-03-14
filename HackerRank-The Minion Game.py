def minion_game(word):
    Stuart = 0
    Kevin = 0
    vowels = ["A", "E", "I", "O", "U"]
    wordlist = list(word)
    length = len(word)
    for i in range(len(word)):
        if wordlist[i] in vowels:
            Kevin += length - i 
        else:
            Stuart += length - i 

    if (Stuart > Kevin):
        print "Stuart " + str(Stuart)
    elif (Stuart == Kevin):
        print "Draw"
    else:
        print "Kevin " + str(Kevin)


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)