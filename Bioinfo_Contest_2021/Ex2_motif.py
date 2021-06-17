import sys

def FindMotif(num, string, pattern):
    

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

