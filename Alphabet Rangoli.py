import string

def print_rangoli(size):
    width = (size -1)*4 +1
    height = (size -1)*2 +1
    side =0 
    center = 0
    sentence = ""
    alphabet = list(string.ascii_lowercase)
    for i in range (1, height+1):
        sentence = ""
        if i < size:
            center = (i - 1)*4 + 1
            side = (width - center)/2
        elif i == size:
            center = width
            side = 0
        else:
            center = (height - i)*4 + 1
            side = (width - center)/2
        sentence += "-"*side
        center = center/2 + 1
        center_of_center = center/2
        temp = size-1
        for j in range(center):
            if(j < center_of_center):
                sentence += alphabet[temp]+"-"
                temp -= 1
            elif(j == center_of_center):
                sentence += alphabet[temp]
                temp += 1
            else:
                sentence += "-" + alphabet[temp]
                temp += 1
        sentence += "-"*side
        print sentence



if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)