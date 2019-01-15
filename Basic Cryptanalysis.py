import string

def isomorphic(string1, string2):
    m = len(string1) 
    n = len(string2) 
    if m != n: 
        return False
    marked = [False] * 256 
    map = [-1] * 256 
    for i in xrange(n): 
        if map[ord(string1[i])] == -1: 
            if marked[ord(string2[i])] == True: 
                return False
            marked[ord(string2[i])] = True 
            map[ord(string1[i])] = string2[i] 
        elif map[ord(string1[i])] != string2[i]: 
            return False
    return True

def check_if_correct(cipher, plain):
    for k in range (len(cipher)):
        tem = ord(plain[k])-97;
        if alphabet[tem] == None:
            continue 
        elif alphabet[tem] == cipher[k]:
            return True
        else:
            return False

def update_check():
    for i in range (len(alphabet_check)-1, -1, -1):
        if alphabet_check[i]  not in cipher.lower():
            alphabet_check.remove(alphabet_check[i])

def update_alphabet(cipher, plain):
    for x in range (len(plain)):
        if alphabet[ord(plain[x])-97] == None:
                alphabet[ord(plain[x])-97] = cipher[x]
                alphabet_check.remove(cipher[x])

def  search(times):
    for i in range(len(count)):
        if count[i][0] == times:
            tem = count[i][2]
            ciphertext = count[i][1]
            if times != 1:
                for j in range (len(tem)):
                    if check_if_correct(list(ciphertext), list(tem[j])):
                        update_alphabet(list(ciphertext), list(tem[j]))
                        break
            else:
                update_alphabet(list(ciphertext), list(tem[0]))
        if alphabet_check:
            pass
        else:
            break

#initialize
cipher = raw_input()
cipher_word = cipher.split(" ")
cipher_length = len(cipher_word)
alphabet = [None]*26
alphabet_check = list(string.ascii_lowercase)
count = []
for i in range(cipher_length):
    count.append([0,'',[]])
f = open("dictionary.lst", "r")
lines = f.readlines()

# find all isomorphic words between cipher and dictionary
for i in range (cipher_length):
    for line in lines:
        words = line.rstrip().lower()
        if isomorphic(cipher_word[i], words):
            count[i][0] += 1
            count[i][1] = cipher_word[i]
            count[i][2].append(words)
del f, lines, cipher_word, cipher_length

update_check()

#check all alphabets
for i in range (len(alphabet_check)):
    if alphabet_check:
        search(i)
    else:
        break

#transfer cipher to plain
answer=''
for i in cipher:
    if i == ' ':
        answer+= i
    else:
        try:
            tem = alphabet.index(i) +97
            answer+= chr(tem)
        except:
            answer+= str("?")

print answer
