import math 
import string
# Conditions and Loops
def cal_sum(a, b):
    i = a
    sum = 0
    if a % 2 == 0:
        i += 1
        while(i < b):
            sum += i
            i += 2
    else:
        while(i < b):
            sum += i
            i += 2
    return sum 

# Dictionaries
def stat_string(s):
    res = {}
    for word in s.split(' '):
        if word not in res:
            res[word] = 1
        else:
            res[word] += 1
    return res

# Files 
def file_deal(input):
    f = open(input, 'r')
    i = 0
    list_line = []
    for line in f:
        if i % 2 != 0:
            list_line.append(line)
        i += 1
    f = open('output.txt', 'w')
    for line in list_line:
        f.write(str(line))
    f.close()

if __name__ == '__main__':
    a = 4420 
    b = 9372
    print(cal_sum(a, b))

    # Dictionaries 
    s = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
    dict = stat_string(s)
    for key,value in dict.items():
        print('%s %d'%(key, value))

    # Files
    input = 'INIT5.txt'
    file_deal(input)



