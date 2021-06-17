import sys

def singleMotif(string, pattern):
    idx = []
    for i in range(len(string)):
        if string[i:i+len(pattern)] == pattern:
            idx.append(i+1)
    return idx

def FindMotif(num, string, pattern):
    res = []
    if num == 1:
        res = singleMotif(string, pattern)
        f = open('./dataset/Ex2_output.txt', 'w')
        f.write(' '.join(map(str, res)) + '\n')
        f.close()
    else:
        for i in range(num):
            res.append(singleMotif(string[i], pattern[i]))
        f = open('./dataset/Ex2_output.txt', 'w')
        for i in range(num):
            f.write(' '.join(map(str, res[i])) + '\n')
        f.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        with open(filename) as f:
            lines = f.read().splitlines()
            num = int(lines[0])
            string = []
            pattern = []
            for i in range(num):
                string.append(lines[2*i+1])
                pattern.append(lines[2*i+2])
    else:
        num = 1
        string = 'GATATATGCATATACTT'
        pattern = 'TAT'
    FindMotif(num, string, pattern)

