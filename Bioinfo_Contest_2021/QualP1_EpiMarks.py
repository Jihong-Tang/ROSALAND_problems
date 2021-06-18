import sys

def EpicMarker(num, input):
    res = []
    for i in range(num):
        res.append(MarkerSearch())
if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = './dataset/QualP1_test.txt'
    
    with open(filename) as f:
        lines = f.read().splitlines()
    num = int(lines[0])
    idxline = 1
    input = []
    for i in range(num):
        idx = lines[idxline].split()
        row = int(idx[0])
        col = idx[1]
        matrix = []
        for j in range(row):
            matrix.append(lines[idxline+1+j])
        input.append(matrix)

    EpicMarker(num, input)
